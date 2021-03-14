# _execute_: NGINX Execute module


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-execute
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

    load_module modules/ngx_http_execute_module.so;

<hr />

## Introduction

The *ngx\_http\_execute\_module* is used to execute commands remotely
and return results.

Configuration example：

    worker_processes  1;
    events {
        worker_connections  1024;
    }
    http {
        include       mime.types;
        default_type  application/octet-stream;
        sendfile        on;
        keepalive_timeout  65;
        server {
            listen       80;
            server_name  localhost;
            location / {
                root   html;
                index  index.html index.htm;
                command on;
            }
            error_page   500 502 503 504  /50x.html;
            location = /50x.html {
                root   html;
            }
        }
    }

Usage: `view-source:http://192.168.18.22/?system.run[command]` The
`command` can be any system command. The command you will want to use
depends on the permissions that nginx runs with.

    view-source:http://192.168.18.22/?system.run[ifconfig]

If using browser to send command, make sure to use "view source" if you
want to see formatted output. Alternatively, you can also use some tools
such as Postman, Fiddler.

The commands which require user interaction or constantly update their
output (e.g. `top`) will not run properly, so do not file a bug for
this.

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-execute](https://github.com/limithit/NginxExecute).
