from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

# key = RSA.generate(2048)
# private_key = key.export_key()
# file_out = open("private.pem", "wb")
# file_out.write(private_key)

# message = 'cactus'.encode()
# key = RSA.import_key(open('./private.pem').read())
# h = SHA256.new(message)
# signature = pkcs1_15.new(key).sign(h)
# print(base64.b64encode(signature))

key = RSA.import_key(open('./public').read())
h = SHA256.new('00'.encode('utf-8'))
signature = 'TmrneZj2xWZxh6mM0rKhhf2GF/nP2w7tU6YBgfSYbRJT3WQ5yATg/RDPyOGYn/HgyDyfrXPhugMli0dHxUMLoZRGirvQCHKvs6EFP/Ktl+WKVO8N++PaOuISB5cO3CKQKv/zYzzeG0wWt3BfwJGaF5Ba31Xy4r6p8pVCgGnTsfvDIfz/IXjNF5U/oNTgxy/LAD3EcIg5SSrS1nSgeVG+IlvoYf9m+7xIuhrlIIZUROt6GtTbq1o0fU9rpINRsjlPlswr7kNH/wuvzqnM2sECJcDjz/ASYjcLyfJYV+MxCw85VVIXoDmuIUJRwd5z2+NO9/CZLqkbh5ME0ho6LvwSBg=='
try:
    pkcs1_15.new(key).verify(h, base64.b64decode(signature))
    print("The signature is valid.")
except Exception as e:
    print("The signature is not valid.", e)
