# f4fhds

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