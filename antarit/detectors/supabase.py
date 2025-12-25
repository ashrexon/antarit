from __future__ import annotations

import re
from typing import List, Pattern

from .base import BaseDetector


class SupabaseDetector(BaseDetector):
    name = "Supabase Key"
    provider = "supabase"
    keywords = ("supabase", "anon key", "service role")

    def compile_patterns(self) -> List[Pattern[str]]:
        return [
            re.compile(r"(?i)supabase_anon_key[\"'=:\\s]{0,5}([A-Za-z0-9._-]{40,})"),
            re.compile(r"(?i)supabase_service_role_key[\"'=:\\s]{0,5}([A-Za-z0-9._-]{40,})"),
        ]

    def provider_name(self) -> str:
        return self.provider
