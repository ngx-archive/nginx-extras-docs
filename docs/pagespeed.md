# _pagespeed_: PageSpeed dynamic module for NGINX


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-pagespeed
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

    load_module modules/ngx_pagespeed.so;

<hr />
![ngx\_pagespeed](https://lh6.googleusercontent.com/-qufedJIJq7Y/UXEvVYxyYvI/AAAAAAAADo8/JHDFQhs91_c/s401/04_ngx_pagespeed.png)


ngx\_pagespeed speeds up your site and reduces page load time by
automatically applying web performance best practices to pages and
associated assets (CSS, JavaScript, images) without requiring you to
modify your existing content or workflow. Features include:

  - Image optimization: stripping meta-data, dynamic resizing,
    recompression
  - CSS & JavaScript minification, concatenation, inlining, and
    outlining
  - Small resource inlining
  - Deferring image and JavaScript loading
  - HTML rewriting
  - Cache lifetime extension
  - and
    [more](https://developers.google.com/speed/docs/mod_pagespeed/config_filters)

To see ngx\_pagespeed in action, with example pages for each of the
optimizations, see our <a href="http://ngxpagespeed.com">demonstration
site</a>.

## How to use

Follow the steps on <a
href="https://developers.google.com/speed/pagespeed/module/configuration">PageSpeed
configuration</a>.

For feedback, questions, and to follow the progress of the project:

  - [ngx-pagespeed-discuss mailing
    list](https://groups.google.com/forum/#!forum/ngx-pagespeed-discuss)
  - [ngx-pagespeed-announce mailing
    list](https://groups.google.com/forum/#!forum/ngx-pagespeed-announce)

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-pagespeed](https://github.com/apache/incubator-pagespeed-ngx).
