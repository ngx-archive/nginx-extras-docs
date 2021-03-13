# Name

[ngx\_http\_html\_sanitize\_module](https://github.com/youzan/ngx_http_html_sanitize_module)
- It's base on google's
[gumbo-parser](https://github.com/google/gumbo-parser) as HTML5 parser
and hackers-painters's
[katana-parser](https://github.com/hackers-painters/katana-parser) as
inline CSS parser to sanitize HTML with whitelisted elements,
whitelisted attributes and whitelisted CSS
        property.

# TOC

  - [Name](#name)
  - [Status](#status)
  - [Example](#example)
  - [Description](#description)
  - [Benchrmark](#benchmark)
  - [TODO](#todo)
  - [Directive](#directive)
      - [html\_sanitize](#html_sanitize)
      - [html\_sanitize\_hash\_max\_size](#html_sanitize_hash_max_size)
      - [html\_sanitize\_hash\_bucket\_size](#html_sanitize_hash_bucket_size)
      - [html\_sanitize\_element](#html_sanitize_element)
      - [html\_sanitize\_attribute](#html_sanitize_attribute)
      - [html\_sanitize\_url\_protocol](#html_sanitize_url_protocol)
      - [html\_sanitize\_url\_domain](#html_sanitize_url_domain)
      - [html\_sanitize\_iframe\_url\_protocol](#html_sanitize_iframe_url_protocol)
      - [html\_sanitize\_iframe\_url\_domain](#html_sanitize_iframe_url_domain)
  - [Querystring](#querystring)
      - [document](#document)
      - [html](#html)
      - [script](#script)
      - [style](#style)
      - [namespace](#namespace)
      - [context](#context)
      - [element](#element)
      - [attribute](#attribute)
      - [style\_property](#style_property)
      - [style\_property\_value](#style_property_value)
      - [url\_protocol](#url_protocol)
      - [url\_domain](#url_domain)
      - [iframe\_url\_protocol](#iframe_url_protocol)
      - [iframe\_url\_domain](#iframe_url_domain)
  - [Copyright](#copyright)

# Status

[![Build
Status](https://travis-ci.org/youzan/ngx_http_html_sanitize_module.svg?branch=master)](https://travis-ci.org/youzan/ngx_http_html_sanitize_module)

Production Ready :-)

# Example

There is a example of [nginx](https://nginx.org/) configuration
according to the <https://dev.w3.org/html5/html-author/#the-elements> as
the following:

``` nginx
server {
    listen 8888;

    location = /sanitize {
        # Explicitly set utf-8 encoding
        add_header Content-Type "text/html; charset=UTF-8";

        client_body_buffer_size 10M;
        client_max_body_size 10M;

        html_sanitize on;

        # Check https://dev.w3.org/html5/html-author/#the-elements

        # Root Element
        html_sanitize_element html;

        # Document Metadata
        html_sanitize_element head title base link meta style;

        # Scripting
        html_sanitize_element script noscript;

        # Sections
        html_sanitize_element body section nav article aside h1 h2 h3 h4 h5 h6 header footer address;

        # Grouping Content
        html_sanitize_element p hr br pre dialog blockquote ol ul li dl dt dd;

        # Text-Level Semantics
        html_sanitize_element a q cite em strong small mark dfn abbr time progress meter code var samp kbd sub sup span i b bdo ruby rt rp;

        # Edits
        html_sanitize_element ins del;

        # Embedded Content
        htlm_sanitize_element figure img iframe embed object param video audio source canvas map area;

        # Tabular Data
        html_sanitize_element table caption colgroup col tbody thead tfoot tr td th;

        # Forms
        html_sanitize_element form fieldset label input button select datalist optgroup option textare output;

        # Interactive Elements
        html_sanitize_element details command bb menu;

        # Miscellaneous Elements
        html_sanitize_element legend div;

        html_sanitize_attribute *.style;
        html_sanitize_attribute a.href a.hreflang a.name a.rel;
        html_sanitize_attribute col.span col.width colgroup.span colgroup.width;
        html_sanitize_attribute data.value del.cite del.datetime;
        html_sanitize_attribute img.align img.alt img.border img.height img.src img.width;
        html_sanitize_attribute ins.cite ins.datetime li.value ol.reversed ol.stasrt ol.type ul.type;
        html_sanitize_attribute table.align table.bgcolor table.border table.cellpadding table.cellspacing table.frame table.rules table.sortable table.summary table.width;
        html_sanitize_attribute td.abbr td.align td.axis td.colspan td.headers td.rowspan td.valign td.width;
        html_sanitize_attribute th.abbr th.align th.axis th.colspan th.rowspan th.scope th.sorted th.valign th.width;

        html_sanitize_style_property color font-size;

        html_sanitize_url_protocol http https tel;
        html_sanitize_url_domain *.google.com google.com;

        html_sanitize_iframe_url_protocol http https;
        html_sanitize_iframe_url_domain  facebook.com *.facebook.com;
    }
}
```

And It's recommanded to use the below commnand to sanitize
HTML5:

``` bash
$ curl -X POST -d "<h1>Hello World </h1>" http://127.0.0.1:8888/sanitize?element=2&attribute=1&style_property=1&style_property_value=1&url_protocol=1&url_domain=0&iframe_url_protocol=1&iframe_url_domain=0

<h1>Hello World </h1>
```

This querystring
`element=2&attribute=1&style_property=1&style_property_value=1&url_protocol=1&url_domain=0&iframe_url_protocol=1&iframe_url_domain=0`
is the as following:

  - element=2: output whitelisted element by
    [html\_sanitize\_element](#html_sanitize_element)
  - attribute=1: output any attribute by
    [html\_sanitize\_attribute](#html_sanitize_attribute)
  - style\_property=1: output any style property by
    [html\_sanitize\_style\_property](#html_sanitize_style_property)
  - style\_property\_value=1: check the style value for
    [url](https://developer.mozilla.org/en-US/docs/Web/CSS/url) function
    and
    [expression](https://msdn.microsoft.com/en-us/library/ms537634\(v=vs.85\).aspx)
    function to avoid XSS inject by
    [style\_property\_value](#style_property_value)
  - url\_protocol=1: check whitelisted url\_protocol for absoluted URL
    by [html\_sanitize\_url\_protocol](#html_sanitize_url_protocol)
  - url\_domain=0: do not check url domain for absoluted URL
  - iframe\_url\_protocol=1: is the same as
    [url\_protocol](#url_protocol) but only for `iframe.src` by
    [html\_sanitize\_iframe\_url\_protocol](#html_sanitize_iframe_url_protocol)
  - iframe\_url\_domain=0: is the same as [url\_domain](#url_domain) but
    only for `iframe.src` by
    [html\_sanitize\_iframe\_url\_domain](#html_sanitize_iframe_url_domain)

With
[ngx\_http\_html\_sanitize\_module](https://github.com/youzan/ngx_http_html_sanitize_module),
we have the ability to specify whether output HTML5's element 、attribute
and inline CSS's property by [directive](#directive) and
[querystring](#querystring) as the following:

## whitelisted element

  - disable element:
    
    if we do not want to output any element, we can do this as the
    following:

<!-- end list -->

``` bash
curl -X POST -d "<h1>h1</h1>" http://127.0.0.1:8888/sanitize?element=0

```

  - enable element:
    
    if we want to output any element, we can do this as the
following:

<!-- end list -->

``` bash
$ curl -X POST -d "<h1>h1</h1><h7>h7</h7>" http://127.0.0.1:8888/sanitize?element=1

<h1>h1</h1><h7>h7</h7>

```

  - enable whitelisted element:
    
    if we want to output whitelisted element, we can do this as the
    following

<!-- end list -->

``` bash
$ curl -X POST -d "<h1>h1</h1><h7>h7</h7>" http://127.0.0.1:8888/sanitize?element=1

<h1>h1</h1>
```

## whitelisted attribute

  - disable attribute:
    
    if we do not want to output any attribute, we can do this as the
    following:

<!-- end list -->

``` bash
curl -X POST -d "<h1 ha=\"ha\">h1</h1>" "http://127.0.0.1:8888/sanitize?element=1&attribute=0"

<h1>h1</h1>
```

  - enable attribute:
    
    if we want to output any attribute, we can do this as the
following:

<!-- end list -->

``` bash
$ curl -X POST -d "<h1 ha=\"ha\">h1</h1>" "http://127.0.0.1:8888/sanitize?element=1&attribute=1"

<h1 ha="ha">h1</h1>

```

  - enable whitelisted attribute:
    
    if we want to output whitelisted element, we can do this as the
    following:

<!-- end list -->

``` bash
$ curl -X POST -d "<img src=\"/\" ha=\"ha\" />" "http://127.0.0.1:8888/sanitize?element=1&attribute=2"

<img src="/" />
```

## whitelisted style property

  - disable style property:
    
    if we do not want to output any style property, we can do this as
    the following:

<!-- end list -->

``` bash
# It will do not output any style property
curl -X POST -d "<h1 style=\"color:red;\">h1</h1>" "http://127.0.0.1:8888/sanitize?element=1&attribute=1&style_property=0"

<h1>h1</h1>
```

  - enable style property:
    
    if we want to output any style property, we can do this as the
    following:

<!-- end list -->

``` bash
$ curl -X POST -d "<h1 style=\"color:red;text-align:center;\">h1</h1>" "http://127.0.0.1:8888/sanitize?element=1&attribute=1&style_property=1"

<h1 style="color:red;text-align:center">h1</h1>
```

  - enable whitelisted style property:
    
    if we want to output whitelisted style property, we can do this as
    the
following:

<!-- end list -->

``` bash
$ curl -X POST -d "<h1 style=\"color:red;text-align:center;\" >h1</h1>" "http://127.0.0.1:8888/sanitize?element=1&attribute=1&style_property=2"

<h1 style="color:red;">h1</h1>
```

# Description

Now the implement of
[ngx\_http\_html\_sanitize\_module](https://github.com/youzan/ngx_http_html_sanitize_module)
is based on [gumbo-parser](https://github.com/google/gumbo-parser) and
[katana-parser](https://github.com/hackers-painters/katana-parser). And
we make the combo upon it then run it on [nginx](https://nginx.org/) to
as a center web service maintained by professional security people for
discarding language-level difference. If we want to gain more higher
performance (here is the [brenchmark](#benchmark)), it's recommanded to
write language-level library wrapering above pure c library to overcome
the overhead of network transmission.

# Benchmark

Testing with `wrk -s benchmarks/shot.lua -d 60s "http://127.0.0.1:8888"`
on Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz and 64GB
memory

| Name                                                          | Size  | Avg Latency |     QPS |
| ------------------------------------------------------------- | :---: | ----------: | ------: |
| [hacker\_news.html](/benchmarks/hacker_news.html)             | 30KB  |      9.06ms | 2921.82 |
| [baidu.html](/benchmarks/baidu.html)                          | 76KB  |     13.41ms | 1815.75 |
| [arabic\_newspapers.html](/benchmarks/arabic_newspapers.html) | 78KB  |     16.58ms | 1112.70 |
| [bbc.html](/benchmakrs/bbc.html)                              | 115KB |     17.96ms |  993.12 |
| [xinhua.html](/benchmarks/xinhua.html)                        | 323KB |     33.37ms |  275.39 |
| [google.html](/benchmakrs/google.html)                        | 336KB |     26.78ms |  351.54 |
| [yahoo.html](/benchmakrs/yahoo.html)                          | 430KB |     29.16ms |  323.04 |
| [wikipedia.html](/benchmakrs/wikipedia.html)                  | 511KB |     57.62ms |  160.10 |
| [html5\_spec.html](/benchmarks/html5_spec.html)               | 7.7MB |       1.63s |    2.00 |

# TODO

  - gumbo-parser (hard): Improvement with SSE-4.2 to speed up string
    processing
  - gumbo-parser (hard): Additional performance improvements with
    algorithm level
  - katana-parser (hard): Improvement with SSE-4.2 to speed up string
    processing
  - katana-parser (hard): Additional performance improvements with
    algorithm level
  - directive (optional): Add mode directives to carefully control HTML5
    and inline CSS output
  - html\_sanitize\_attribute (hard): Add new algorithm instead of
    current hash find to reduce memory allocation
  - tests (easy): Pass more xss security tests
  - querystring (optional): Allow foreign whitelisted querystring to
    control whitelisted elements、attributes、style\_properties.

A tips to optimize performance is learn from the On-CPU Flamegraph as
the
following:

<https://cdn.rawgit.com/youzan/ngx_http_html_sanitize_module/master/flamegraphs/html_sanitize_gumbo_parse.svg>

# Directive

## html\_sanitize

**syntax:** *html\_sanitize on | off*

**default:** *html\_sanitize on*

**context:** *location*

Specifies whether enable html sanitize handler on location context

## html\_sanitize\_hash\_max\_size

**syntax:** *html\_sanitize\_hash\_max\_size size*

**default:** *html\_sanitize\_hash\_max\_size 2048*

**context:** *location*

Sets the maximum size of the
element、attribute、style\_property、url\_protocol、url\_domain、iframe\_url\_protocol、iframe\_url\_domain
hash tables.

## html\_sanitize\_hash\_bucket\_size

**syntax:** *html\_sanitize\_hash\_bucket\_size size*

**default:** *html\_sanitize\_hash\_bucket\_size 32|64|128*

**context:** location

Sets the bucket size for
element、attribute、style\_property、url\_protocol、url\_domain、iframe\_url\_protocol、iframe\_url\_domain.
The default value depends on the size of the processor’s cache line.

## html\_sanitize\_element

**syntax:** *html\_sanitize\_element element ...*

**default:** -

**context:** location

Set the whitelisted HTML5 elements when enable whitelisted element by
setting the querystring [element](#element) whitelist mode as the
following:

``` nginx
html_sanitize_element html head body;
```

## html\_sanitize\_attribute

**syntax:** *html\_sanitize\_attribute attribute ...*

**default:** -

**context:** location

Set the whitelisted HTML5 attributes when enable whitelisted element by
setting the querystring [attribute](#attribute) whitelist mode as the
following:

``` nginx
html_sanitize_attribute a.href h1.class;
```

PS: attribute format must be the same as `element.attribute` and support
`*.attribute` (prefix asterisk) and `element.*` (suffix asterisk)

## html\_sanitize\_style\_property

**syntax:** *html\_sanitize\_style\_property property ...*

**default:** -

**context:** location

Set the whitelisted CSS property when enable whitelisted element by
setting the querystring [style\_property](#style_property) whitelist
mode as the following:

``` nginx
html_sanitize_style_property color background-color;
```

## html\_sanitize\_url\_protocol

**syntax:** *html\_sanitize\_url\_protocol \[protocol\] ...*

**default:** -

**context:** location

Set the allowed URL protocol at [linkable
attribute](#linkable_attribute) when only the URL is absoluted rahter
than related and enable URL protocol check by setting the querystring
[url\_protocol](#url_protocol) check mode as the following:

``` nginx
html_sanitize_url_protocol http https tel;
```

## html\_sanitize\_url\_domain

**syntax:** *html\_sanitize\_url\_domain domain ...*

**default:** -

**context:** location

Set the allowed URL domain at [linkable attribute](#linkable_attribute)
when only the URL is absoluted rahter than relatived and enable URL
protocol check、URL domain check by setting the querystring
[url\_protocol](#url_protocol) check mode and the querystring
\[url\_domain\]\[\#url\_domain\] check mode as the following:

``` nginx
html_sanitize_url_domain *.google.com google.com;
```

## html\_sanitize\_iframe\_url\_protocol

**syntax:** *html\_sanitize\_iframe\_url\_protocol \[protocol\] ...*

**default:** -

**context:** location

is the same as
[html\_sanitize\_url\_protocol](#html_sanitize_url_protocol) but only
for `iframe.src` attribute

``` nginx
html_sanitize_iframe_url_protocol http https tel;
```

## html\_sanitize\_iframe\_url\_domain

**syntax:** *html\_sanitize\_iframe\_url\_domain \[protocol\] ...*

**default:** -

**context:** location

is the same as [html\_sanitize\_url\_domain](#html_sanitize_url_domain)
but only for `iframe.src` attribute

``` nginx
html_sanitize_iframe_url_domain *.facebook.com facebook.com;
```

# linkable\_attribute

The linkable attribute is the following:

  - a.href
  - blockquote.cite
  - q.cite
  - del.cite
  - img.src
  - ins.cite
  - iframe.src
  - CSS URL function

# Querystring

the querystring from request URL is used to control the
[ngx\_http\_html\_sanitize\_module](https://github.com/youzan/ngx_http_html_sanitize_module)
internal action.

## document

**value:** *0 or 1*

**default:** *0*

**context:** querystring

Specifies whether append `<!DOCTYPE>` to response body

## html

**value:** *0 or 1*

**default:** *0*

**context:** querystring

Specifies whether append `<html></html>` to response body

## script

**value:** *0 or 1*

**default:** *0*

**context:** querystring

Specifies whether allow `<script></script>`

## style

**value:** *0 or 1*

**default:** *0*

**context:** querystring

Specifies whether allow `<style></style>`

## namespace

**value:** *0、1 or 2*

**default:** *0*

**context:** querystring

Specifies the mode of gumbo-parser with the value as the following:

  - GUMBO\_NAMESPACE\_HTML: 0
  - GUMBO\_NAMESPACE\_SVG: 1
  - GUMBO\_NAMESPACE\_MATHML: 2

## context

**value:** *\[0, 150)*

**default:** *38(GUMBO\_TAG\_DIV)*

**context:** querystring

Specifies the context of gumbo-parser with the value at the this file
[tag\_enum.h](tag_enum.h)

## element

**value:** *0、1、2*

**default:** *0*

**context:** querystring

Specifies the mode of output element with the value as the following:

  - 0: do not output element
  - 1: output all elements
  - 2: output whitelisted elements

## attribute

**value:** *0、1、2*

**default:** *0*

**context:** querystring

Specifies the mode of output attribute with the value as the following:

  - 0: do not output attributes
  - 1: output all attributes
  - 2: output whitelisted attributes

## style\_property

**value:** *0、1、2*

**default:** *0*

**context:** querystring

Specifies the mode of output CSS property with the value as the
following:

  - 0: do not output CSS property
  - 1: output all CSS property
  - 2: output whitelisted CSS property

## style\_property\_value

**value:** *0、1*

**default:** *0*

**context:** querystring

Specifies the mode of output CSS property\_value with the value as the
following:

  - 0: do not check the CSS property's value
  - 1: check the CSS property's value for
    [URL](https://developer.mozilla.org/en-US/docs/Web/CSS/url) function
    and IE's expression function to avoid XSS inject

## url\_protocol

**value:** *0、1*

**default:** *0*

**context:** querystring

Specifies whether check the URL protocol at
[linkable\_attribute](#linkable_attribute). The value is as the
following:

  - 0: do not check the URL protocol
  - 1: output whitelisted URL protocol

## url\_domain

**value:** *0、1*

**default:** *0*

**context:** querystring

Specifies whether check the URL domain at
[linkable\_attribute](#linkable_attribute) when enable
[url\_protocol](#url_protocol) check. The value is as the following:

  - 0: do not check the URL domain
  - 1: output whitelisted URL domain

## iframe\_url\_protocol

**value:** *0、1*

**default:** *0*

**context:** querystring

is the same as [url\_protocol](#url_protocol) but only for `iframe.src`

## iframe\_url\_domain

**value:** *0、1*

**default:** *0*

**context:** querystring

is the same as [url\_domain](#url_domain) but only for
`iframe.src`

# Copyright

[ngx\_http\_html\_sanitize\_module](https://github.com/youzan/ngx_http_html_sanitize_module)
is licensed under the Apache License, Version 2.0. See
[LICENSE](/license) for the complete license text.

Copyright 2017, By detailyang "Yang Bingwu" Youzan Inc. All Rights
Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Notice

Note that
[ngx\_http\_html\_sanitize\_module](https://github.com/youzan/ngx_http_html_sanitize_module)
bundles many projects with different license as the following:

google/gumbo-parser: <https://github.com/google/gumbo-parser>

hackers-painters/katana-parser:
[https://github.com/hackers-painters/katana-parser](https://github.com/hackers-painters/katana-parse)