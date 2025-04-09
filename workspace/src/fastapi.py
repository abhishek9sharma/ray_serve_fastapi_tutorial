import math
import os

from fastapi import FastAPI, HTTPException

app = FastAPI()


def compute_intensive_task(n: int = 1000000) -> int:
    """A CPU-intensive task (calculating primes up to n)."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return len(primes)


@app.get("/hello")
def hello():
    result = compute_intensive_task()  # This will use CPU
    print(result)
    return {"message": "Hello, World!", "primes_count": result}
