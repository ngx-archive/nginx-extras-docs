# *geoip*: NGINX GeoIP dynamic modules


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-geoip
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

```nginx
load_module modules/ngx_http_geoip_module.so;
```
```nginx
load_module modules/ngx_stream_geoip_module.so;
```

<hr />


## Directives

You may find information about configuration directives for this module at the following links:        

*   http://nginx.org/en/docs/http/ngx_http_geoip_module.html#directives