>>> from Crypto.Cipher import DES
>>> obj=DES.new('abcdefgh', DES.MODE_ECB)
>>> plain="Guido van Rossum is a space alien."
>>> len(plain)
34
>>> obj.encrypt(plain)
Traceback (innermost last):
  File "<stdin>", line 1, in ?
ValueError: Strings for DES must be a multiple of 8 in length
>>> ciph=obj.encrypt(plain+'XXXXXX')
>>> ciph
'\021,\343Nq\214DY\337T\342pA\372\255\311s\210\363,\300j\330\250\312\347\342I\3215w\03561\303dgb/\006'
>>> obj.decrypt(ciph)
'Guido van Rossum is a space alien.XXXXXX'
