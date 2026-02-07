from pathlib import Path
import subprocess
import sys


def test_pipeline_generates_report():
    # run pipeline
    result = subprocess.run(
        [sys.executable, "-m", "dss.main"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert Path("reports/sample_daily_brief.md").exists()
    assert Path("reports/sample_daily_brief.md").stat().st_size > 0
