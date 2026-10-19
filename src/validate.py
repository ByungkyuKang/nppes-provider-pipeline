"""Step 3: Validate — check the data against quality rules.

Example rules:
1. No duplicate NPIs (identifiers)
2. No missing required fields (name, state)
3. Flag expired licenses
4. Validate ZIP code format
5. Report anomalous records
(To be implemented on Day 5 — the Python version of production data-quality monitoring)
"""


def run_checks(df) -> dict:
    """Run each rule and return {rule_name: failure_count}."""
    raise NotImplementedError("To be implemented on Day 5")
