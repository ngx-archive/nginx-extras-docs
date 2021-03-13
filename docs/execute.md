# NginxExecute

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
