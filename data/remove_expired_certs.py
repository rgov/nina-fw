from datetime import datetime
from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding
import sys

with open("roots.pem","rb") as pem:
    pem_data = pem.read()

certs = x509.load_pem_x509_certificates(pem_data)

for c in certs:
    c_expired = c.not_valid_after < datetime.now()
    if not c_expired:
        sys.stdout.buffer.write(c.public_bytes(encoding=Encoding.PEM))
    