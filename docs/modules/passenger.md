# _passenger_: Passenger module


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install nginx-module-passenger
```

Enable the module by adding the following at the top of `/etc/nginx/nginx.conf`:

```nginx
load_module modules/ngx_http_passenger_module.so;
```


This document describes nginx-module-passenger [v6.0.7](https://github.com/phusion/passenger/releases/tag/release-6.0.7){target=_blank} 
released on Nov 18 2020.
    
<hr />
[![Gem Version](https://badge.fury.io/rb/passenger.svg)](https://badge.fury.io/rb/passenger)
## <img src="images/passenger_logo.svg" alt="passenger logo" style="margin-bottom: -.2em; width: 1.4em"> Phusion Passenger
<h3>Supercharge your Ruby, Node.js and Python apps</h3>

[Phusion Passenger™](https://www.phusionpassenger.com/) is a web server and application server, designed to be fast, robust and lightweight. It takes a lot of complexity out of deploying web apps, adds powerful enterprise-grade features that are useful in production, and makes administration much easier and less complex. Phusion Passenger supports Ruby, Python, Node.js and Meteor, and is being used by high-profile companies such as **Apple, Pixar, New York Times, AirBnB, Juniper** etc as well as [over 650.000 websites](http://trends.builtwith.com/Web-Server/Phusion-Passenger).

<a href="https://vimeo.com/224923750"><img src="https://github.com/phusion/passenger/blob/stable-5.2/images/justin.png" height="400"></a><br><em>Phusion Passenger - the smart app server</em>

<p>What makes Passenger so fast and reliable is its <strong>C++</strong> core, its <strong>zero-copy</strong> architecture, its <strong>watchdog</strong> system and its <strong>hybrid</strong> evented, multi-threaded and multi-process design.</p>

## Fuse Panel - GUI for Passenger
The <strong>smarter</strong> and <strong>simpler command center</strong> for your applications. <strong><a href="https://www.phusionpassenger.com/fuse-panel" target="_blank">Fuse Panel</a></strong> monitors your apps in near real-time, offers insights in your logs and enables analyzing and troubleshooting issues. New and exclusively available in the Fuse Panel is much-requested feature <strong>per-application log viewing and splitting</strong>.

Regardless of if you’re running Passenger open source or you’re one of our enterprise customers, the Fuse Panel is available for free while in beta. <a href="https://www.phusionpassenger.com/fuse-panel" target="_blank">Give it a try</a>.

<img src="https://github.com/phusion/passenger/blob/stable-5.2/images/spark.png" align="left" width="300">

### Learn more:
- [Website](https://www.phusionpassenger.com/)
- [Fuse Panel](https://www.phusionpassenger.com/fuse-panel)
- [Documentation &amp; Support](https://www.phusionpassenger.com/support)
- [Consultancy](https://www.phusion.nl/consultancy)
- [Twitter](https://twitter.com/phusion_nl)
- [Blog](http://blog.phusion.nl/)

<br/><br/><br/><br/><br/>

## Further reading

 * The `doc/` directory.
 * [Contributors Guide](https://github.com/phusion/passenger/blob/master/CONTRIBUTING.md)
 * [Phusion Passenger support page](https://www.phusionpassenger.com/support)
 * [Phusion Passenger release notes](https://blog.phusion.nl/tag/passenger-releases/)

## Legal

"Passenger" and "Phusion Passenger" are registered trademarks of Phusion Holding B.V.

## GitHub

You may find additional configuration tips and documentation in the [GitHub repository for 
nginx-module-passenger](https://github.com/phusion/passenger){target=_blank}.