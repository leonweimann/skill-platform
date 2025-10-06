from functools import lru_cache

from fastapi import FastAPI

from skillcore.settings import ApiSettings


@lru_cache(maxsize=1)
def get_settings() -> ApiSettings:
    return ApiSettings()


app = FastAPI(
    title="SkillForge API",
    version="0.1.0",
)


@app.get("/healthz")
def health():
    s = get_settings()
    return {"status": "ok", "env": s.env, "log_level": s.log_level}
