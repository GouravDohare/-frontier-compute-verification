import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from attestation import ComputeRecord, sign, verify

class AttestationTests(unittest.TestCase):
    def setUp(self):
        self.secret = b"test-secret"
        self.record = ComputeRecord(100.0, "job-1", "2026-01-01T00:00:00Z")

    def test_valid_record(self):
        self.assertTrue(verify(self.record, sign(self.record, self.secret), self.secret))

    def test_modified_record_fails(self):
        sig = sign(self.record, self.secret)
        modified = ComputeRecord(101.0, "job-1", self.record.timestamp)
        self.assertFalse(verify(modified, sig, self.secret))

if __name__ == "__main__":
    unittest.main()
