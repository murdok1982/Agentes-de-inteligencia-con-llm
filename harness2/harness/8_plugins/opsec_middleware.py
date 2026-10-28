import os

def sanitize_output(payload: str) -> str:
    sensitive_vars = ["OPENROUTER_API_KEY", "HARNESS2_CODEX_API_KEY", "TG_API_HASH", "GITHUB_PAT"]
    clean = payload
    for var in sensitive_vars:
        secret = os.getenv(var)
        if secret and len(secret) > 4:
            clean = clean.replace(secret, "[REDACTED_BY_OPSEC_MIDDLEWARE]")
    return clean
