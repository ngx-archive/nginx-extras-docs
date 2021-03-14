# _upstream-fair_: The fair load balancer module for NGINX


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-upstream-fair
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

    load_module modules/ngx_http_upstream_fair_module.so;

<hr />
Nginx Upstream Fair Proxy Load
Balancer

## \*\*( compatible with nginx 1.11.6+ & with dynamic module capability ) \*\*

## Description:

The Nginx fair proxy balancer enhances the standard round-robin load
balancer provided with Nginx so that it will track busy back end servers
(e.g. Thin, Ebb, Mongrel) and balance the load to non-busy server
processes.

Further information can be found on <http://nginx.localdomain.pl/>

Ezra Zygmuntowicz has a good writeup of the fair proxy load balancer and
how to use it here:
<http://brainspl.at/articles/2007/11/09/a-fair-proxy-balancer-for-nginx-and-mongrel>

## Usage:

Change your Nginx config file's upstream block to include the 'fair'
directive:

upstream mongrel { fair; server 127.0.0.1:5000; server 127.0.0.1:5001;
server 127.0.0.1:5002; }

If you encounter any issues, please report them using the bugtracker at
<http://nginx.localdomain.pl/>

## Contributing:

Git source repositories:
<http://github.com/gnosek/nginx-upstream-fair/tree/master>
<http://git.localdomain.pl/?p=nginx-upstream-fair.git;a=summary>

Please feel free to fork the project at GitHub and submit pull requests
or patches.

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-upstream-fair](https://github.com/itoffshore/nginx-upstream-fair).
