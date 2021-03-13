# FIPS status check module for NGINX

## Introduction

This module applies to NGINX builds that use OpenSSL for SSL/TLS crypto.
It runs after NGINX startup and queries the OpenSSL library, reporting
if the library is in FIPS mode or not.

``` sh
sudo tail /var/log/nginx/error.log
2020/04/03 07:45:54 [notice] 11250#11250: using the "epoll" event method
2020/04/03 07:45:54 [notice] 11250#11250: OpenSSL FIPS Mode is enabled
2020/04/03 07:45:54 [notice] 11250#11250: nginx/1.17.6 (nginx-plus-r20)
2020/04/03 07:45:54 [notice] 11250#11250: built by gcc 4.8.5 20150623 (Red Hat 4.8.5-36) (GCC)
2020/04/03 07:45:54 [notice] 11250#11250: OS: Linux 3.10.0-1062.el7.x86_64
```

For more information on using NGINX in FIPS mode, see the [NGINX Plus
FIPS
documentation](https://docs.nginx.com/nginx/fips-compliance-nginx-plus/),
which applies to both NGINX open source builds and NGINX Plus. To
determine which TLS ciphers NGINX offers, the [nmap
ssl-enum-ciphers](https://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html)
script is useful.