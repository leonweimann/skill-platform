from __future__ import annotations

from functools import lru_cache

from skillcore.settings import BaseAppSettings


@lru_cache(maxsize=1)
def _db_url() -> str:
    return BaseAppSettings().database_url
