# Flag
natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

I noticed the URL has a page paramter and the supplied page is used to query the file associated with the value in the parameter.
If we try and check http://natas7.natas.labs.overthewire.org/index.php?page=jkhjk, the page returns:

Warning: include(jkhjk): failed to open stream: No such file or directory in /var/www/natas/natas7/index.php on line 21
....

In the source it says:
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

If we go to http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8,
we can get see the password is displayed: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe