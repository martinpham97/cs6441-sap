# Flag
natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

Another input checking vulnerability with the encode function for the secret in the source.


$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

We can reverse this by first convert it from hex to binary using hex2bin, then reverse it, then decode it with base64.

hex2bin: ==QcCtmMml1ViV3b 
reversed: b3ViV1lmMmtCcQ==
base64: oubWYf2kBq

Enter the secret to get the password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl.
