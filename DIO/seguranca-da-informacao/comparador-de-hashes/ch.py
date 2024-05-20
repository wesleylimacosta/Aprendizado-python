import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('sha1')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('sha1')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print('Os arquivos são diferentes')
else:
    print('Os arquivos são iguais')
