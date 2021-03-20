# _radixtree_: Adaptive Radix Trees implemented in Lua / LuaJIT


## Installation

### CentOS/RHEL 6, 7, 8 or Amazon Linux 2

```bash
yum -y install https://extras.getpagespeed.com/release-latest.rpm
yum -y install lua-resty-radixtree
```



This document describes lua-resty-radixtree [v2.7.0](https://github.com/api7/lua-resty-radixtree/releases/tag/v2.7.0){target=_blank} 
released on Mar 10 2021.
    
<hr />

### Install Dependencies

```shell
make deps
```

## Benchmark

We wrote some simple benchmark scripts.
Machine environment: MacBook Pro (16-inch, 2019), CPU 2.3 GHz Intel Core i9.

```shell
$ make
cc -O2 -g -Wall -fpic -std=c99 -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -DBUILDING_SO -c src/rax.c -o src/rax.o
cc -O2 -g -Wall -fpic -std=c99 -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -DBUILDING_SO -c src/easy_rax.c -o src/easy_rax.o
cc -shared -fvisibility=hidden src/rax.o src/easy_rax.o -o librestyradixtree.so

$ make bench
resty -I=./lib -I=./deps/share/lua/5.1 benchmark/match-parameter.lua
matched res: 1
route count: 100000
match times: 10000000
time used  : 3.3849999904633 sec
QPS        : 2954209
each time  : 0.33849999904633 ns

resty -I=./lib -I=./deps/share/lua/5.1 benchmark/match-prefix.lua
matched res: 500
route count: 100000
match times: 1000000
time used  : 0.4229998588562 sec
QPS        : 2364066

resty -I=./lib -I=./deps/share/lua/5.1 benchmark/match-static.lua
matched res: 500
route count: 100000
match times: 10000000
time used  : 0.78799986839294 sec
QPS        : 12690357

resty -I=./lib -I=./deps/share/lua/5.1 benchmark/match-hosts.lua
matched res: 500
route count: 1000
match times: 100000
time used  : 1.6989998817444 sec
QPS        : 58858

resty -I=./lib -I=./deps/share/lua/5.1 benchmark/match-wildcard-hosts.lua
matched res: 500
route count: 1000
match times: 50000
time used  : 1.2469999790192 sec
QPS        : 40096
```


## GitHub

You may find additional configuration tips and documentation for this module in the [GitHub repository for 
nginx-module-radixtree](https://github.com/api7/lua-resty-radixtree){target=_blank}.