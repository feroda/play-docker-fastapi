from fastapi import FastAPI
import redis
import time

app = FastAPI()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

@app.get("/api/")
def root():
    r.incr("hits")
    return {"message": "Hello from FastAPI", "hits": r.get("hits")}

@app.get("/api/cpubound")
def cpubound(number: int):
    start_time = time.time()
    result = fib(number)
    end_time = time.time()
    return {"number": number, "result": result, "time": end_time - start_time}

@app.get("/api/cached")
def cached(number: int):
    start_time = time.time()
    cached_result = r.get(f"fib:{number}")
    if cached_result:
        end_time = time.time()
        return {"number": number, "result": int(cached_result), "time": end_time - start_time, "from_cache": True}
    
    result = fib(number)
    r.set(f"fib:{number}", result)
    end_time = time.time()
    return {"number": number, "result": result, "time": end_time - start_time, "from_cache": False}
