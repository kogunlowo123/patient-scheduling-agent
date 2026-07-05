"""Patient Scheduling Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_find_available_slots():
    """Test Find available appointment slots for a provider or specialty."""
    tools = AgentTools()
    result = await tools.find_available_slots(provider_id="test", specialty="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_book_appointment():
    """Test Book a patient appointment with a provider."""
    tools = AgentTools()
    result = await tools.book_appointment(patient_id="test", provider_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_waitlist():
    """Test Add patient to waitlist and notify on availability."""
    tools = AgentTools()
    result = await tools.manage_waitlist(patient_id="test", preferred_criteria="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_send_reminder():
    """Test Send appointment reminder via SMS, email, or phone."""
    tools = AgentTools()
    result = await tools.send_reminder(appointment_id="test", channel="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.patient_scheduling_agent_agent import PatientSchedulingAgentAgent
    agent = PatientSchedulingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
