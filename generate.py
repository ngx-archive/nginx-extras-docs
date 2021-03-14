import base64
import glob
import os
import re
import pandoc

import yaml
from pathlib import Path
from lastversion import lastversion
import logging as log

from tabulate import tabulate

work_dir = os.path.dirname(__file__) or '.'
print(work_dir)
os.chdir(work_dir)
import lastversion

print(lastversion.__file__)


def enrich_with_yml_info(md, module_config, release):
    handle = module_config['handle']
    repo = module_config['repo']
    new_title = f"# _{handle}_: {module_config['summary']}"
    upstream_name = module_config['repo'].split('/')[-1]
    sonames = module_config['soname']
    lines = md.splitlines()
    first_line = lines[0]
    if first_line.startswith('#'):
        lines.pop(0)
    if 'ref' in module_config:
        intro = f"""
## Installation

CentOS/RHEL 6, 7, 8 and Amazon Linux 2 are supported.

### OS-specific complete installation and configuration guides available:

"""
        if 'el7' in module_config['ref']:
            intro += f"*   [CentOS/RHEL 7]({module_config['ref']['el7']})\n"
        if 'el8' in module_config['ref']:
            intro += f"*   [CentOS/RHEL 8]({module_config['ref']['el8']})\n"
        if 'amzn2' in module_config['ref']:
            intro += f"*   [Amazon Linux 2]({module_config['ref']['amzn2']})\n"

        intro += f"""
### Other supported operating systems        
```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-{handle}
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

"""
    else:
        intro = f"""

## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-{handle}
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

"""

    print(sonames)
    if isinstance(sonames, str):
        sonames = [sonames]
    print(sonames)
    for s in sonames:
        intro += f"```nginx\nload_module modules/{s}.so;\n```\n"
    intro += f"""

This document describes nginx-module-{handle} [v{release['version']}](https://github.com/{repo}/releases/tag/{release['tag_name']}){{target=_blank}} 
released on {release['tag_date'].strftime("%b %d %Y")}.
    """
    intro += "\n<hr />\n"



    out = [new_title] + intro.splitlines()
    bad_lines = (
        '[back to toc](#table-of-contents)',
        'this module is not distributed',
        'installation instructions](#installation).',
        '[![build',
        'status]',
        '[![travisci build',
        '![ngx\_pagespeed]'
    )
    for l in lines:
        check_l = l.strip().lower().lstrip('*_')
        if check_l not in bad_lines and not check_l.startswith(bad_lines):
            out.append(l)
    return "\n".join(out)


# only support GitHub flavored markdown
# so we preprocess files with pandoc docs/modulesupsync.md -o docs/modulesupsync.md -t gfm
def remove_md_sections(md, titles):
    out = []
    # marks that we are "within" target section
    section_level = None

    for line in md.splitlines():
        # remove that stuff:
        line = line.lstrip('\u200c')
        if not line.startswith('#'):
            # if not in target section, proceed adding stuff
            if not section_level:
                out.append(line)
            continue
        # we are reading section title now
        cur_sec_level = 0
        cur_sec_title = ''
        seen_whitespace = False
        for c in line:
            if c == '#':
                cur_sec_level = cur_sec_level + 1
            else:
                cur_sec_title = cur_sec_title + c
        cur_sec_title = cur_sec_title.strip().rstrip(':')
        if cur_sec_title.lower() in titles:
            section_level = cur_sec_level
            # do not add this target section title
        elif section_level:
            # already in target section
            if cur_sec_level <= section_level:
                # found same/higher level with different title, unmark so we know we're out
                section_level = None
                out.append(line)
            else:
                # level under target section, we skip
                pass
        else:
            # some other section
            out.append(line)
    return "\n".join(out)


def ensure_one_h1(md):
    # It is crucial for there to be only one heading or else TOC is not properly generated
    out = []
    seen_h1 = False
    lines = md.splitlines()
    for line in lines:
        if line.startswith('# '):
            if not seen_h1:
                seen_h1 = True
            else:
                line = "## " + line.lstrip('# ')
        out.append(line)
    return "\n".join(out)


all_modules = []
table = []
headers = ["Package Name", "Description"]


def normalize_md_headings(readme_contents):
    out = []
    lines = readme_contents.splitlines()
    total = len(lines)
    skip_next = False
    for i in range(total):
        line = lines[i]
        if line.strip() == "```" and i < (total - 1) and lines[i+1].strip().startswith(('http ', 'location ', 'server ', 'map ')):
            line = '```nginx'
        if skip_next is True:
            skip_next = False
            continue

        # check if next line is heading, then normalize current, and skip +1
        if i + 1 == total:
            out.append(line)
        else:
            if lines[i + 1].startswith('====') and '|' not in lines[i + 1]:
                out.append(f"# {line}")
                skip_next = True
            elif lines[i + 1].startswith('----') and '|' not in lines[i + 1]:
                out.append(f"## {line}")
                skip_next = True
            else:
                out.append(line)
    return "\n".join(out)


def normalize_to_md(readme_contents, file_name):
    # normalize to Github flavored markdown
    doc = pandoc.Document()
    if file_name.endswith('.rst'):
        doc.rst = readme_contents.encode('utf-8')
    elif file_name.endswith('.textile'):
        doc.textile = readme_contents.encode('utf-8')
    else:
        # doc.gfm = readme_contents.encode('utf-8')
        return normalize_md_headings(readme_contents)
    return doc.gfm.decode("utf-8")


def process_modules_glob(g):
    for module_file_name in glob.glob(g):
        print(f"Processing {module_file_name}")
        handle = Path(module_file_name).stem
        with open(module_file_name) as f:
            all_modules.append(handle)
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            module_config = yaml.load(f)
            module_config['handle'] = handle
            print(f"Fetching release for {module_config['repo']}")
            release = lastversion.latest(module_config['repo'], output_format='dict')
            if 'readme' not in release:
                continue
            readme_contents = base64.b64decode(release['readme']['content']).decode("utf-8")
            readme_contents = normalize_to_md(readme_contents, release['readme']['name'])
            readme_contents = remove_md_sections(readme_contents, [
                'installation',
                'install',
                'installing',
                'build',
                'how to install',
                'how to build',
                'building as a dynamic module',
                'installation:',
                'compilation',
                'how to install',
                'patch to collect ssl_cache_usage, ssl_handshake_time content_time, gzip_time, '
                'upstream_time, upstream_connect_time, upstream_header_time graphs (optional)',
                'table of contents',
                'install in centos 7',
                'c macro configurations',
                'requirements',
                'building',
                'compatibility',
                'toc',
                'dependencies',
                'installation for stable nginx',
                'version'
            ])

            readme_contents = enrich_with_yml_info(readme_contents, module_config, release)

            readme_contents = readme_contents + f"""

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-{handle}](https://github.com/{module_config['repo']}){{target=_blank}}.
"""
            readme_contents = ensure_one_h1(readme_contents)
            # print(readme_contents)
            with open(f"docs/modules/{handle}.md", "w") as module_md_f:
                module_md_f.write(readme_contents)
            table.append(
                [f'[nginx-module-{handle}](modules/{handle}.md)', module_config['summary']])
        # break


process_modules_glob("../nginx-extras/modules/*.yml")
process_modules_glob("../nginx-extras/modules/others/*.yml")

with open(f"docs/modules.md", "w") as index_md_f:
    index_md_f.write(
        tabulate(table, headers, tablefmt="github")
    )

all_modules.sort()
print(all_modules)
final_all_modules = []
for m in all_modules:
    final_all_modules.append({m: f"modules/{m}.md"})
# write nav:
with open("mkdocs.yml") as mkdocs_f:
    mkdocs_config = yaml.load(mkdocs_f)
    nav = [
        {'Overview': 'index.md'},
        {'Modules': final_all_modules},
        {'RPM Repository': 'https://www.getpagespeed.com/redhat'}
    ]
    mkdocs_config['nav'] = nav
    print(mkdocs_config)
with open("mkdocs.yml", "w") as f:
    yaml.dump(mkdocs_config, f)

print('Done generation')
