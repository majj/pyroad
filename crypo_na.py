
### libsodium

### https://github.com/stef/pysodium/blob/master/test/test_pysodium.py

import pysodium

import binascii


def test0():
    if not pysodium.sodium_version_check(1, 0, 9): return
    
    pk, sk = pysodium.crypto_box_keypair()        
    #print(pk)
    #print(sk)
    p =binascii.hexlify(pk)
    s =binascii.hexlify(sk)
    print(p)
    print(s)        

    c = pysodium.crypto_box_seal(b"passwd", pk)        
    print (binascii.hexlify(c)) 
    print(pysodium.crypto_box_seal_open(c, pk, sk))      

def test_box_seal():    
    #p1 = b'~\x8b8\xf0%\xef\xba\x86\xe6\xcd\xd8\x16\x8b,\xf7\xa9\xc7a@F\x08\x84sx6\x1c\x18\xf5\x03\xbd"\x05'
    #s1 = b'\xe1\xa2\xfd\xc0\xbb\xe9\x1f,\x8a\xe8)D\x1dII\xe0\x9e{\xf1\xbe0\x04\x04\x8c\xde9V\x97\x9f\xe5&\x1a'
    
    pk_s = '7e8b38f025efba86e6cdd8168b2cf7a9c761404608847378361c18f503bd2205'
    sk_s = 'e1a2fdc0bbe91f2c8ae829441d4949e09e7bf1be3004048cde3956979fe5261a'        

    # string to bytes (hexadecimal )
    pk_h = bytes (pk_s, 'utf8')
    sk_h = bytes (sk_s, 'utf8')
    
    # hexadecimal to binary data 
    pk_b = binascii.unhexlify(pk_h)        
    sk_b = binascii.unhexlify(sk_h)
    
      
    
    x_s = '1f4fa3ccb8d877a7c8a26d4c86c6866eba50c8ad03567ac7e6f84cff3069e97e7576bc506c55de41501419fd49dadd13755b426b018d'
    x_b = bytes (x_s, 'utf8')
    
    s = binascii.unhexlify(x_b)
    
    print(pysodium.crypto_box_seal_open(s, pk_b, sk_b))       
        

def test_box():
    
    m = b"passwd"
    
    pk, sk = pysodium.crypto_box_keypair()
    
    n = pysodium.randombytes(pysodium.crypto_box_NONCEBYTES)
    
    print(n)
    
    c = pysodium.crypto_box(m, n, pk, sk)        
    plaintext = pysodium.crypto_box_open(c, n, pk, sk)        
    print(plaintext)

def test_sk_to_pk():
    #pk, sk = pysodium.crypto_box_keypair()
    
    pk, sk = pysodium.crypto_sign_keypair()        
    
    pk2 = pysodium.crypto_sign_sk_to_pk(sk)
    
    print(pk==pk2)        
        
def main():
    test0()
    print("==============================")
    test_box_seal()
    print("==============================")
    test_box()
    print("==============================")
    test_sk_to_pk()
        
if __name__ == "__main__":
    main()