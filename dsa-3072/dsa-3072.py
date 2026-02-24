# coding: utf-8
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256  # Compatible hash
from timeit import default_timer

start = default_timer()
key = DSA.generate(3072)
end = default_timer()
print('3072 bit DSA key generation time in microseconds: ' + str((end - start) * 1e6))

# Small file
sha256_hash = SHA256.new()

start = default_timer()

with open("smallFile_1KB.txt", "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)

signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(sha256_hash)  # Pass hash object

pub_key = key.publickey()
verifier = DSS.new(pub_key, 'fips-186-3')
try:
    verifier.verify(sha256_hash, signature)  # Pass hash object
    print("OK")
except ValueError:
    print("Incorrect signature")

end = default_timer()
print('Using 3072 bit DSA key signing and verification time in microseconds: ' + str((end - start) * 1e6))

# Large file
sha256_hash = SHA256.new()

start = default_timer()

with open("largeFile_1MB.txt", "rb") as f:  # Fixed name
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)

signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(sha256_hash)

pub_key = key.publickey()
verifier = DSS.new(pub_key, 'fips-186-3')
try:
    verifier.verify(sha256_hash, signature)
    print("OK")
except ValueError:
    print("Incorrect signature")

end = default_timer()
print('Using 3072 bit DSA key signing and verification time in microseconds: ' + str((end - start) * 1e6))