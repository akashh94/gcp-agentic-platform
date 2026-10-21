"""Guardrails for the agent, implemented as ADK plugins.

A plugin is registered once on the ``App`` (see ``agent.py``) and its callbacks
run for every model call in the workflow. Returning a value from a callback
short-circuits the default behaviour; returning ``None`` lets it continue.
"""

import re
from typing import Optional

from google.adk.models import LlmResponse
from google.adk.plugins.base_plugin import BasePlugin

_PII_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "phone": re.compile(r"\+?\d[\d\s().-]{7,}\d"),
}


def _redact(text: str) -> str:
    for label, pattern in _PII_PATTERNS.items():
        text = pattern.sub(f"[REDACTED:{label}]", text)
    return text


class PiiRedactionPlugin(BasePlugin):
    """Redacts PII from model responses before they reach the user."""

    def __init__(self) -> None:
        super().__init__(name="pii_redaction")

    async def after_model_callback(
        self,
        *,
        callback_context,
        llm_response: LlmResponse,
    ) -> Optional[LlmResponse]:
        if not llm_response.content or not llm_response.content.parts:
            return None

        redacted = llm_response.model_copy(deep=True)
        changed = False
        for part in redacted.content.parts:
            if part.text:
                cleaned = _redact(part.text)
                if cleaned != part.text:
                    part.text = cleaned
                    changed = True
        return redacted if changed else None
