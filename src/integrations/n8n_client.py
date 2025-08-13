"""Client utilities for interacting with n8n workflows."""
from __future__ import annotations

import os
from typing import Any, Dict, Tuple

import requests


def _get_config() -> Tuple[str, str]:
    """Return the n8n base URL and API key from environment variables."""
    base_url = os.getenv("N8N_BASE_URL")
    api_key = os.getenv("N8N_API_KEY")
    if not base_url or not api_key:
        raise ValueError("N8N_BASE_URL and N8N_API_KEY must be set")
    return base_url, api_key


def trigger_workflow(workflow_id: str, payload: Dict[str, Any]) -> requests.Response:
    """Trigger an n8n workflow with the given payload.

    Parameters
    ----------
    workflow_id:
        The ID of the workflow to execute.
    payload:
        Data to send to the workflow.

    Returns
    -------
    requests.Response
        The response returned by the n8n server.

    Raises
    ------
    ValueError
        If required configuration variables are missing.
    requests.HTTPError
        If the HTTP request fails.
    """
    base_url, api_key = _get_config()

    url = f"{base_url}/api/v1/workflows/{workflow_id}/run"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response


def trigger_default_workflow(payload: Dict[str, Any]) -> requests.Response:
    """Trigger the workflow referenced by ``N8N_EXAMPLE_WORKFLOW_ID``."""
    workflow_id = os.getenv("N8N_EXAMPLE_WORKFLOW_ID")
    if not workflow_id:
        raise ValueError("N8N_EXAMPLE_WORKFLOW_ID must be set")
    return trigger_workflow(workflow_id, payload)
