import hashlib
import hmac
import json
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class ComputeRecord:
    accelerator_hours: float
    workload_id: str
    timestamp: str

    def canonical_bytes(self):
        payload = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))
        return payload.encode("utf-8")

def sign(record, secret):
    return hmac.new(secret, record.canonical_bytes(), hashlib.sha256).hexdigest()

def verify(record, signature, secret):
    expected = sign(record, secret)
    return hmac.compare_digest(expected, signature)
