## ABOUT:

ngx\_coolkit is collection of small and useful nginx
add-ons.

## CONFIGURATION DIRECTIVES:

## override\_method off | \[methods\] source (context: http, server, location)

Override HTTP method.

default: none

## CONFIGURATION VARIABLES:

## $remote\_passwd

Decoded password from "Authorization" header (Basic HTTP
Authentication).

## $location

Name of the matched location block.

## EXAMPLE CONFIGURATION \#1:

http { server { location / { override\_method $arg\_method; proxy\_pass
<http://127.0.0.1:8100>; } } }

Pass request with changed HTTP method (based on "?method=XXX") to the
backend.

## EXAMPLE CONFIGURATION \#2:

http { upstream database { postgres\_server 127.0.0.1 dbname=test
user=monty password=some\_pass; }

    server {
        location = /auth {
            internal;
    
            set_quote_sql_str  $user $remote_user;
            set_quote_sql_str  $pass $remote_passwd;
    
            postgres_pass      database;
            postgres_query     "SELECT login FROM users WHERE login=$user AND pass=$pass";
            postgres_rewrite   no_rows 403;
            postgres_output    none;
        }
    
        location / {
            auth_request       /auth;
            root               /files;
        }
    }

}

Restrict access to local files by authenticating against SQL database.

Required modules (other than ngx\_coolkit):

  - ngx\_http\_auth\_request\_module,
  - ngx\_postgres (PostgreSQL) or ngx\_drizzle (MySQL, Drizzle, SQLite),
  - ngx\_set\_misc.