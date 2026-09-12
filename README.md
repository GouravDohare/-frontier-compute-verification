# Frontier AI Compute Verification

An independent research prototype exploring whether hardware-backed attestation and cryptographic evidence could help an auditor verify claims about the computational scale of frontier AI development.

## Research question

Can a verifier obtain useful evidence about compute usage without requiring a lab to reveal every sensitive infrastructure detail?

## Prototype

This version models:
- a compute record containing accelerator-hours, workload ID, and timestamp;
- an integrity/authentication mechanism;
- verification of an unchanged record;
- detection of a tampered record.

The cryptographic mechanism is deliberately a toy HMAC construction so the project runs with Python's standard library. It is **not** a production remote-attestation system.

## Run

```bash
python src/attestation.py
python src/simulate_audit.py
python -m unittest discover -s tests -v
```

## Research limitations

A real system would need hardware roots of trust, secure measurement, key management, remote attestation, independent auditing procedures, privacy analysis, and a stronger adversary model. The central research challenge is not merely signing a number; it is establishing whether the signed measurement faithfully represents the underlying computation.

## Status

Initial prototype / research-in-progress. No empirical claims are made beyond the reproducible tests in this repository.
