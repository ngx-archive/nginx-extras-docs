# _cookie-limit_: NGINX module to limit the number of malicious ip forged cookies


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-cookie-limit
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

```nginx
load_module modules/ngx_http_cookie_limit_req_module.so;
```


This document describes nginx-module-cookie-limit [v1.1](https://github.com/limithit/ngx_cookie_limit_req_module/releases/tag/1.1){target=_blank} 
released on Feb 25 2020.
    
<hr />
﻿# ngx_cookie_limit_req_module
 
## Introduction

The *ngx_cookie_limit_req_module* module not only limits the access rate of cookies but also limits the number of malicious ip forged cookies.

## Donate
The developers work tirelessly to improve and develop ngx_cookie_limit_req_module. Many hours have been put in to provide the software as it is today, but this is an extremely time-consuming process with no financial reward. If you enjoy using the software, please consider donating to the devs, so they can spend more time implementing improvements.

 ### Alipay:
![Alipay](https://github.com/limithit/shellcode/blob/master/alipay.png)

Author
Gandalf zhibu1991@gmail.com

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-cookie-limit](https://github.com/limithit/ngx_cookie_limit_req_module){target=_blank}.