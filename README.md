#GoogleFontAPI2CompressedCSS
Creates a compressed CSS file with embedded fonts (base64 encoded) from a Google Font API call.

Useful for intranets.  

##Checkout:
git clone git@github.com:yousry/GoogleFontAPI2CompressedCSS.git

##Call Example:

CSSFontCompressor.py -o fonts.css.gz "https://fonts.googleapis.com/css?family=Baloo+Bhaina|Yatra+One

Creates a file *fonts.css.gz* with two fonts.

##Limitations

###Server Side comression
If server-side compression is enabled. the css file can be extracted with gunzip. 

Server-side compression for Apache can be enabled with: 

```javascript
<ifModule mod_gzip.c>
mod_gzip_on Yes
mod_gzip_dechunk Yes
mod_gzip_item_include file .(html?|txt|css|js|php|pl)$
mod_gzip_item_include handler ^cgi-script$
mod_gzip_item_include mime ^text/.*
mod_gzip_item_include mime ^application/x-javascript.*
mod_gzip_item_exclude mime ^image/.*
mod_gzip_item_exclude rspheader ^Content-Encoding:.*gzip.*
</ifModule>
```

Source: [https://varvy.com/pagespeed/enable-compression.html](https://varvy.com/pagespeed/enable-compression.html)[https://varvy.com/pagespeed/enable-compression.html)[https://varvy.com/pagespeed/enable-compression.html)

###Font compression

For pythons urllib queries the Google font api returns ttf (instead o woff2) files.
