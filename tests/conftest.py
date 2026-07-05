"""Test configuration for Patient Scheduling Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "patient-scheduling-agent", "category": "Healthcare"}
