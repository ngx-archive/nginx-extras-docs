# Description

**ngx\_http\_geoip2\_module** - creates variables with values from the
maxmind geoip2 databases based on the client IP (default) or from a
specific variable (supports both IPv4 and IPv6)

The module now supports nginx streams and can be used in the same way
the http module can be used.

## Download Maxmind GeoLite2 Database (optional)

The free GeoLite2 databases are available from [Maxminds
website](http://dev.maxmind.com/geoip/geoip2/geolite2/)

[GeoLite2
City](http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz)
[GeoLite2
Country](http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz)

## Example Usage:

    http {
        ...
        geoip2 /etc/maxmind-country.mmdb {
            auto_reload 5m;
            $geoip2_metadata_country_build metadata build_epoch;
            $geoip2_data_country_code default=US source=$variable_with_ip country iso_code;
            $geoip2_data_country_name country names en;
        }
    
        geoip2 /etc/maxmind-city.mmdb {
            $geoip2_data_city_name default=London city names en;
        }
        ....
    
        fastcgi_param COUNTRY_CODE $geoip2_data_country_code;
        fastcgi_param COUNTRY_NAME $geoip2_data_country_name;
        fastcgi_param CITY_NAME    $geoip2_data_city_name;
        ....
    }
    
    stream {
        ...
        geoip2 /etc/maxmind-country.mmdb {
            $geoip2_data_country_code default=US source=$remote_addr country iso_code;
        }
        ...
    }

##### Metadata:

Retrieve metadata regarding the geoip database.

    $variable_name metadata <field>

Available fields:

  - build\_epoch: the build timestamp of the maxmind database.
  - last\_check: the last time the database was checked for changes
    (when using auto\_reload)
  - last\_change: the last time the database was reloaded (when using
    auto\_reload)

##### Autoreload (default: disabled):

Enabling auto reload will have nginx check the modification time of the
database at the specified interval and reload it if it has changed.

    auto_reload <interval>

##### GeoIP:

    $variable_name [default=<value] [source=$variable_with_ip] path ...

If default is not specified, the variable will be empty if not found.

If source is not specified, $remote\_addr will be used to perform the
lookup.

To find the path of the data you want (eg: country names en), use the
[mmdblookup
tool](https://maxmind.github.io/libmaxminddb/mmdblookup.html):

    $ mmdblookup --file /usr/share/GeoIP/GeoIP2-Country.mmdb --ip 8.8.8.8
    
      {
        "country":
          {
            "geoname_id":
              6252001 <uint32>
            "iso_code":
              "US" <utf8_string>
            "names":
              {
                "de":
                  "USA" <utf8_string>
                "en":
                  "United States" <utf8_string>
              }
          }
      }
    
    $ mmdblookup --file /usr/share/GeoIP/GeoIP2-Country.mmdb --ip 8.8.8.8 country names en
    
      "United States" <utf8_string>

This translates
    to:

    $country_name "default=United States" source=$remote_addr country names en