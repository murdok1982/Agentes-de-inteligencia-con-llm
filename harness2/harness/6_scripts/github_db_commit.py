import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from pydantic import BaseModel
from typing import List, Dict

class IntelligenceContract(BaseModel):
    spec_reference: str
    execution_cycle_timestamp: str
    intelligence_summary: Dict[str, object]
    intelligence_graph: Dict[str, List[object]]
    next_autonomous_threads: List[Dict[str, object]]

class GithubIntelligenceSync:
    def __init__(self):
        self.repo_path = Path(os.getenv("LOCAL_REPO_CLONE", "./data_repo_clone"))
        self.remote_repo = os.getenv("TARGET_REPO", "murdok1982/DataBaseInt-Osint-socmint-Sigint")
        self.pat = os.getenv("GITHUB_PAT", "")

    def validate_and_push(self, payload_json_str: str, operation_code: str = "OP-001") -> str:
        raw_data = json.loads(payload_json_str)
        validated = IntelligenceContract(**raw_data)

        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        out_dir = self.repo_path / "operations" / operation_code
        out_dir.mkdir(parents=True, exist_ok=True)

        file_path = out_dir / f"intel_graph_{ts}.json"
        file_path.write_text(validated.model_dump_json(indent=2), encoding="utf-8")
        return str(file_path)
