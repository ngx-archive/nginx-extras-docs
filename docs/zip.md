# _zip_: Streaming ZIP archiver for NGINX


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-zip
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

    load_module modules/ngx_http_zip_module.so;

<hr />


mod\_zip assembles ZIP archives dynamically. It can stream component
files from upstream servers with nginx's native proxying code, so that
the process never takes up more than a few KB of RAM at a time, even
while assembling archives that are (potentially) gigabytes in size.

mod\_zip supports a number of "modern" ZIP features, including large
files, UTC timestamps, and UTF-8 filenames. It allows clients to resume
large downloads using the "Range" and "If-Range" headers, although these
feature require the server to know the file checksums (CRC-32's) in
advance. See "Usage" for details.

To unzip files on the fly, check out
[nginx-unzip-module](https://github.com/youzee/nginx-unzip-module).

## Usage

The module is activated when the original response (presumably from an
upstream) includes the following HTTP header:

    X-Archive-Files: zip

It then scans the response body for a list of files. The syntax is a
space-separated list of the file checksum (CRC-32), size (in bytes),
location (properly URL-encoded), and file name. One file per line. The
file location corresponds to a location in your nginx.conf; the file can
be on disk, from an upstream, or from another module. The file name can
include a directory path, and is what will be extracted from the ZIP
file. Example:

    1034ab38 428    /foo.txt   My Document1.txt
    83e8110b 100339 /bar.txt   My Other Document1.txt

Files are retrieved and encoded in order. If a file cannot be found or
the file request returns any sort of error, the download is aborted.

The CRC-32 is optional. Put "-" if you don't know the CRC-32; note that
in this case mod\_zip will disable support for the `Range` header.

## Re-encoding filenames

To re-encode the filenames as UTF-8, add the following header to the
upstream response:

    X-Archive-Charset: [original charset name]

The original charset name should be something that iconv understands.
(This feature only works if iconv is present.)

If you set original charset as `native`:

    X-Archive-Charset: native;

filenames from the file list are treated as already in the system native
charset. Consequently, the ZIP general purpose flag (bit 11) that
indicates UTF-8 encoded names will not be set, and archivers will know
it's a native charset.

Sometimes there is problem converting UTF-8 names to native(CP866)
charset that causes popular archivers to fail to recognize them. And at
the same time you want data not to be lost so that smart archivers can
use Unicode Path extra field. You can provide you own, adapted
representation of filename in native charset along with original UTF-8
name in one string. You just need to add following header:

    X-Archive-Name-Sep: [separator];

So your file list should look like:

    <CRC-32> <size> <path> <native-filename><separator><utf8-filename>
    ...

then filename field will contatin `native-filename` and Unicode Path
extra field will contain `utf8-filename`.

## Tips

1.  Add a header "Content-Disposition: attachment; filename=foobar.zip"
    in the upstream response if you would like the client to name the
    file "foobar.zip"

2.  To save bandwidth, add a "Last-Modified" header in the upstream
    response; mod\_zip will then honor the "If-Range" header from
    clients.

3.  To wipe the X-Archive-Files header from the response sent to the
    client, use the headers\_more module:
    <http://wiki.nginx.org/NginxHttpHeadersMoreModule>

4.  To improve performance, ensure the backends are not returning
    gzipped files. You can achieve this with `proxy_set_header
    Accept-Encoding "";` in the location blocks for the component files.

Questions/patches may be directed to Evan Miller, <emmiller@gmail.com>.

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-zip](https://github.com/evanmiller/mod_zip).
