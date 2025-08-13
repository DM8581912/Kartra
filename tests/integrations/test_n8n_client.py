"""Tests for the n8n client integration."""
import pathlib
import sys
import types

import pytest

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2] / "src"))
from integrations import n8n_client


def test_trigger_workflow_missing_env(monkeypatch):
    monkeypatch.delenv("N8N_BASE_URL", raising=False)
    monkeypatch.delenv("N8N_API_KEY", raising=False)
    with pytest.raises(ValueError):
        n8n_client.trigger_workflow("123", {})


def test_trigger_workflow_success(monkeypatch):
    monkeypatch.setenv("N8N_BASE_URL", "http://example.com")
    monkeypatch.setenv("N8N_API_KEY", "secret")

    called = {}

    def fake_post(url, json, headers, timeout):  # type: ignore[override]
        called["url"] = url
        called["json"] = json
        called["headers"] = headers
        response = types.SimpleNamespace()
        response.raise_for_status = lambda: None
        return response

    monkeypatch.setattr(n8n_client.requests, "post", fake_post)

    response = n8n_client.trigger_workflow("1", {"foo": "bar"})
    assert hasattr(response, "raise_for_status")
    assert called["url"] == "http://example.com/api/v1/workflows/1/run"
    assert called["json"] == {"foo": "bar"}
    assert called["headers"]["Authorization"] == "Bearer secret"


def test_trigger_default_workflow(monkeypatch):
    monkeypatch.setenv("N8N_BASE_URL", "http://example.com")
    monkeypatch.setenv("N8N_API_KEY", "secret")
    monkeypatch.setenv("N8N_EXAMPLE_WORKFLOW_ID", "2")

    called = {}

    def fake_post(url, json, headers, timeout):  # type: ignore[override]
        called["url"] = url
        called["json"] = json
        called["headers"] = headers
        response = types.SimpleNamespace()
        response.raise_for_status = lambda: None
        return response

    monkeypatch.setattr(n8n_client.requests, "post", fake_post)

    response = n8n_client.trigger_default_workflow({"bar": "baz"})
    assert hasattr(response, "raise_for_status")
    assert called["url"] == "http://example.com/api/v1/workflows/2/run"
    assert called["json"] == {"bar": "baz"}
