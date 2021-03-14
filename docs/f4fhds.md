# _f4fhds_: NGINX module for Adobe f4f format


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-f4fhds
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

    load_module modules/ngx_http_f4fhds_module.so;

<hr />

Nginx module for Adobe f4f format.

This module implements handling of HTTP Dynamic Streaming requests in
the “/videoSeg1-Frag1” form — extracting the needed fragment from the
videoSeg1.f4f file using the videoSeg1.f4x index file. This module is an
alternative to the Adobe’s f4f module (HTTP Origin Module) for Apache.

It is open-source equivalent for commercial
[ngx\_http\_f4f\_module](http://nginx.org/en/docs/http/ngx_http_f4f_module.html#f4f_buffer_size)
module.

## Synopsis

    location /video/ {
        f4fhds;
        ...
    }

## Limitations

  - The assumption is that all files contain a single (first) segment,
    e.g. Seg1
  - The files should reside in a local non-networked filesystem, due to
    use of `mmap(2)`.

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-f4fhds](https://github.com/GetPageSpeed/f4fhds).
