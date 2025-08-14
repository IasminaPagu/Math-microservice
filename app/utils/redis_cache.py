import redis
import json
from typing import Any

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_cached_result(key: str):
    value = r.get(key)
    if value:
        return json.loads(value)
    return None
def set_cached_result(key: str, value: Any, ttl_seconds: int = 3600):
    r.set(key, json.dumps(value), ex=ttl_seconds)
    r.set(key, json.dumps(value), ex=ttl_seconds)
