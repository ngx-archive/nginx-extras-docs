# *image-filter*: NGINX image filter dynamic module


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-image-filter
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

```nginx
load_module modules/ngx_http_image_filter_module.so;
```

<hr />


## Directives

You may find information about configuration directives for this module at the following links:        

*   https://nginx.org/en/docs/http/ngx_http_image_filter_module.html#directives