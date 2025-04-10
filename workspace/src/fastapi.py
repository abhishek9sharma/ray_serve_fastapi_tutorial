from fastapi import FastAPI, HTTPException

app = FastAPI()


import math
import random


def compute_intensive_task(n: int = None) -> int:
    """A CPU-intensive task (calculating primes up to n). If n is not provided, it is randomly chosen."""
    if n is None:
        n = random.randint(1000, 10000)  # Randomly choose n between 1000 and 1,000,000

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
    return {"message": "Hello, World!", "primes_count": str(result)}
