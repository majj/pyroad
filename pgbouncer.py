
## generate password for pgBounder
## PostgreSQL\pgBouncer\etc\userlist.txt

import hashlib

## he md5 password is just the md5sum of password + username with the string md5 prepended. 

print('md5'+ hashlib.md5(b'mabouser' + b'mabotech').hexdigest())
