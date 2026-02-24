# coding: utf-8
import hashlib  # Not needed if using Crypto.Hash, but keeping for reference
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256  # For compatible hash object
from timeit import default_timer

start = default_timer()
key = DSA.generate(2048)
end = default_timer()
print('2048 bit DSA key generation time in microseconds: ' + str((end - start) * 1e6))

# Small file
sha256_hash = SHA256.new()

start = default_timer()

with open("smallFile_1KB.txt", "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)

signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(sha256_hash)  # Pass the hash object directly

pub_key = key.publickey()
verifier = DSS.new(pub_key, 'fips-186-3')
try:
    verifier.verify(sha256_hash, signature)  # Pass the hash object directly
    print("OK")
except ValueError:
    print("Incorrect signature")

end = default_timer()
print('Using 2048 bit DSA key signing and verification time in microseconds: ' + str((end - start) * 1e6))

# Large file
sha256_hash = SHA256.new()

start = default_timer()

with open("largeFile_1MB.txt", "rb") as f:  # Fixed name assuming typo
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
print('Using 2048 bit DSA key signing and verification time in microseconds: ' + str((end - start) * 1e6))