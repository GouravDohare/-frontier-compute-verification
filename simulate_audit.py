from attestation import ComputeRecord, sign, verify

SECRET = b"demo-secret-only"

record = ComputeRecord(
    accelerator_hours=1200.0,
    workload_id="training-run-demo",
    timestamp="2026-09-13T00:00:00Z",
)

signature = sign(record, SECRET)

print("Original record verifies:", verify(record, signature, SECRET))

tampered = ComputeRecord(
    accelerator_hours=12000.0,
    workload_id=record.workload_id,
    timestamp=record.timestamp,
)

print("Tampered record verifies:", verify(tampered, signature, SECRET))
