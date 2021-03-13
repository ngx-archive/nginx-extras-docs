# Description

**testcookie-nginx-module** is a simple robot mitigation module using
cookie based challenge/response.

Challenge cookies can be set using different methods:

  - "Set-Cookie" + 302/307 HTTP Location redirect
  - "Set-Cookie" + HTML meta refresh redirect
  - Custom template, JavaScript can be used here.

To prevent automatic parsing, challenge cookie value can be encrypted
with AES-128 in CBC mode using custom/random key and iv, and then
decrypted at client side with JavaScript.

# Directives

## testcookie

**syntax:** *testcookie (on|off|var);*

**default:** *off*

**context:** *http, server, location, if*

on - Enable module

off - Disable module

var - Don't intercept requests, only set module variables.

## testcookie\_name

**syntax:** *testcookie\_name \<string\>*

**default:** *TCK*

**context:** *http, server, location*

Sets cookie name.

## testcookie\_domain

**syntax:** *testcookie\_domain \<string\>*

**default:** *none, set by browser*

**context:** *http, server, location*

Sets cookie domain.

## testcookie\_expires

**syntax:** *testcookie\_expires \<string\>*

**default:** *31 Dec 2037 23:55:55 GMT*

**context:** *http, server, location*

Sets cookie expiration value.

## testcookie\_path

**syntax:** *testcookie\_path \<string\>*

**default:** */*

**context:** *http, server, location*

Sets cookie path, useful if you plan to use different keys for
locations.

## testcookie\_secret

**syntax:** *testcookie\_secret \<string\>*

**default:** *required configuration directive*

**context:** *http, server, location*

Secret string, used in challenge cookie computation, should be 32 bytes
or more, better to be long but static to prevent cookie reset for
legitimate users every server restart. If set to *"random"* - new secret
will be generated every server restart, not recomended(all cookies with
previous key will be invalid),

## testcookie\_session

**syntax:** *testcookie\_session \<variable\>*

**default:** *required configuration directive*

**context:** *http, server, location*

Sets the challenge generation function input,

  - $remote\_addr - clients IP address will be used as an user unique
    identifier
  - $remote\_addr$http\_user\_agent - clients IP + User-Agent

## testcookie\_arg

**syntax:** *testcookie\_arg \<string\>*

**default:** *none*

**context:** *http, server, location*

Sets GET parameter name, used for cookie setting attempts computation,

If not set - server will try to set cookie infinitely.

## testcookie\_max\_attempts

**syntax:** *testcookie\_max\_attempts \<integer\>*

**default:** *5*

**context:** *http, server, location*

Sets maximum number of redirects before user will be sent to fallback
URL, according to RFC1945 can't be more than 5.

If set to 0 - server will try to set cookie infinitely(actually, browser
will show the error page).

## testcookie\_p3p

**syntax:** *testcookie\_p3p \<string\>*

**default:** *none*

**context:** *http, server, location*

Sets P3P policy.

## testcookie\_fallback

**syntax:** *testcookie\_fallback \<script\>*

**default:** *none*

**context:** *http, server, location*

Sets the fallback URL, user will be redirected to after maximum number
of attempts, specified by directive *testcookie\_max\_attempts* exceded.
Nginx scripting variables can be used here. If not set - client will get
403 after max attempts reached.

## testcookie\_whitelist

**syntax:** *testcookie\_whitelist \<network list\>*

**default:** *none*

**context:** *http, server*

Sets the networks for which the testing will not be used, add search
engine networks here. Currently IPv4 CIDR only.

## testcookie\_pass

**syntax:** *testcookie\_pass $variable;*

**default:** *none*

**context:** *http, server*

Sets the variable name to test if cookie check should be bypassed. If
variable value set to *1* during the request - cookie check will not be
performed. Can be used for more complex whitelisting.

## testcookie\_redirect\_via\_refresh

**syntax:** *testcookie\_redirect\_via\_refresh (on|off);*

**default:** *off*

**context:** *http, server, location*

Set cookie and redirect using HTTP meta refresh, required if
*testcookie\_refresh\_template* used.

## testcookie\_refresh\_template

**syntax:** *testcookie\_refresh\_template \<string\>*

**default:** *none*

**context:** *http, server, location*

Use custom html instead of simple HTTP meta refresh, you need to set
cookie manually from the template Available all the nginx variables
    and

    $testcookie_nexturl - URL the client should be redirected to, if max_attempts exceeded *testcookie_fallback* value will be here
    $testcookie_got - cookie value received from client, empty if no cookie or it does not match format
    $testcookie_set - correct cookie value we're expecting from client
    $testcookie_ok - user passed test (1 - passed, 0 - not passed) Note: changed from "yes"/"no" in v1.10

also, if testcookie\_refresh\_encrypt\_cookie enabled there are three
more variables:

    $testcookie_enc_key - encryption key (32 hex digits)
    $testcookie_enc_iv - encryption iv (32 hex digits)
    $testcookie_enc_sec - encrypted cookie value (32 hex digits)

## testcookie\_refresh\_status

**syntax:** *testcookie\_refresh\_status \<code\>*

**default:** *200*

**context:** *http, server, location*

Use custom HTTP status code when serving html.

## testcookie\_deny\_keepalive

**syntax:** *testcookie\_deny\_keepalive (on|off);*

**default:** *off*

**context:** *http, server, location*

Close connection just after setting the cookie, no reason to keep
connections with bots.

## testcookie\_get\_only

**syntax:** *testcookie\_get\_only (on|off);*

**default:** *off*

**context:** *http, server, location*

Process only GET requests, POST requests will be bypassed.

## testcookie\_https\_location

**syntax:** *testcookie\_https\_location (on|off);*

**default:** *off*

**context:** *http, server, location*

Redirect client to https protocol after setting the cookie, also affects
*$testcookie\_nexturl*, useful with 3dparty SSL offload.

## testcookie\_refresh\_encrypt\_cookie

**syntax:** *testcookie\_refresh\_encrypt\_cookie (on|off);*

**default:** *off*

**context:** *http, server, location*

Encrypt cookie variable, used with *testcookie\_refresh\_template* to
force client-side decryption with AES-128 CBC.

## testcookie\_refresh\_encrypt\_cookie\_key

**syntax:** *testcookie\_refresh\_encrypt\_cookie\_key \<32 hex
digits|random\>*

**default:** *required directive if encryption enabled*

**context:** *http, server, location*

Sets encryption key.

Possible values:

    random - new key generated every nginx restart
    32 hex digits - static key, useful if you plan to obfuscate it deep in client-side javascript.

## testcookie\_refresh\_encrypt\_iv

**syntax:** *testcookie\_refresh\_encrypt\_iv \<32 hex
digits|random|random2\>*

**default:** *random*

**context:** *http, server, location*

Sets encryption iv.

Possible values: random - new iv generated for every client request
random2 - new iv generated for every nginx restart 32 hex digits -
static iv, useful if you plan to obfuscate it deep in client-side
javascript

## testcookie\_internal

**syntax:** *testcookie\_internal (on|off);*

**default:** *off*

**context:** *http, server, location*

Enable testcookie check for internal redirects (disabled by default for
optimization purposes\!), useful for this type of configs:

    rewrite ^/(.*)$ /index.php?$1 last;

## testcookie\_httponly\_flag

**syntax:** *testcookie\_httponly\_flag (on|off);*

**default:** *off*

**context:** *http, server, location*

Enable HttpOnly flag for cookie.

## testcookie\_secure\_flag

**syntax:** *testcookie\_secure\_flag (on|off|$variable);*

**default:** *off*

**context:** *http, server, location*

Enable Secure flag for cookie. Any variable value except "off"
interpreted as True.

## testcookie\_port\_in\_redirect

**syntax:** *testcookie\_port\_in\_redirect (on|off);*

**default:** *off*

**context:** *http, server, location*

Expose port in redirect.

# Compatibility

Module was tested with nginx 1.1+, but should work with 1.0+.

# Example configuration

    http {
        #default config, module disabled
        testcookie off;
    
        #setting cookie name
        testcookie_name BPC;
    
        #setting secret
        testcookie_secret keepmesecret;
    
        #setting session key
        testcookie_session $remote_addr;
    
        #setting argument name
        testcookie_arg ckattempt;
    
        #setting maximum number of cookie setting attempts
        testcookie_max_attempts 3;
    
        #setting p3p policy
        testcookie_p3p 'CP="CUR ADM OUR NOR STA NID", policyref="/w3c/p3p.xml"';
    
        #setting fallback url
        testcookie_fallback http://google.com/cookies.html?backurl=http://$host$request_uri;
    
        #configuring whitelist
        testcookie_whitelist {
            8.8.8.8/32;
        }
    
    
        #setting redirect via html code
        testcookie_redirect_via_refresh on;
    
        #enable encryption
        testcookie_refresh_encrypt_cookie on;
    
        #setting encryption key
        testcookie_refresh_encrypt_cookie_key deadbeefdeadbeefdeadbeefdeadbeef;
    
        #setting encryption iv
        testcookie_refresh_encrypt_cookie_iv deadbeefdeadbeefdeadbeefdeadbeef;
    
        #setting response template
        testcookie_refresh_template '<html><body>setting cookie...<script type=\"text/javascript\" src=\"/aes.min.js\" ></script><script>function toNumbers(d){var e=[];d.replace(/(..)/g,function(d){e.push(parseInt(d,16))});return e}function toHex(){for(var d=[],d=1==arguments.length&&arguments[0].constructor==Array?arguments[0]:arguments,e="",f=0;f<d.length;f++)e+=(16>d[f]?"0":"")+d[f].toString(16);return e.toLowerCase()}var a=toNumbers("$testcookie_enc_key"),b=toNumbers("$testcookie_enc_iv"),c=toNumbers("$testcookie_enc_set");document.cookie="BPC="+toHex(slowAES.decrypt(c,2,a,b))+"; expires=Thu, 31-Dec-37 23:55:55 GMT; path=/";location.href="$testcookie_nexturl";</script></body></html>';
    
        server {
            listen 80;
            server_name test.com;
    
    
            location = /aes.min.js {
                gzip  on;
                gzip_min_length 1000;
                gzip_types      text/plain;
                root /var/www/public_html;
            }
    
            location = /w3c/p3p.xml {
                root /var/www/public_html;
            }
    
            location / {
                #enable module for specific location
                testcookie on;
                proxy_set_header   Host             $host;
                proxy_set_header   X-Real-IP        $remote_addr;
                proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
                proxy_pass http://127.0.0.1:80;
            }
        }
    }

See more cases in "docs" directory of the project.

# Test suite

This module comes with a Perl-driven test suite. Thanks to the
[Test::Nginx](http://search.cpan.org/perldoc?Test::Nginx) module in the
Perl world.

# Sources

Available on github at
[kyprizel/testcookie-nginx-module](http://github.com/kyprizel/testcookie-nginx-module).

# TODO

  - Code review
  - Statistics (?)

# Bugs

Feel free to report bugs and send patches to <kyprizel@gmail.com> or
using [github's issue
tracker](http://github.com/kyprizel/testcookie-nginx-module/issues).

# Support the project

    Send your donations to 1FHmPTP6aDBAzVtM7Pe7Y69zqhjPRx847s

# Copyright & License

Copyright (C) 2011-2017 Eldar Zaitov (<kyprizel@gmail.com>).

All rights reserved.

This module is licenced under the terms of BSD license.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    *   Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    *   Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    *   Neither the name of the authors nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS \`\`AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.