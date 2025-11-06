from locust import HttpUser, task, between, events
import random
import string
import json

# Utility functions
def random_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def random_proxytype():
    return random.choice(["TYPE1", "TYPE2", "TYPE3"])

class TransactionUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def post_transaction(self):
        payload = {
            "txn_id": f"TX{random_string(6)}",
            "cif": f"CIF{random_string(4)}",
            "amount": round(random.uniform(10, 5000), 2),
            "proxytype": random_proxytype()
        }
        headers = {"Content-Type": "application/json"}

        with self.client.post("/transaction", data=json.dumps(payload), headers=headers, catch_response=True) as response:
            try:
                # check if status code is 2xx
                if response.status_code == 200:
                    # optionally check response content
                    data = response.json()
                    if data.get("status") == "success":
                        response.success()
                    else:
                        response.failure(f"Unexpected status in response: {data}")
                else:
                    response.failure(f"HTTP {response.status_code}")
            except Exception as e:
                response.failure(f"Exception: {e}")

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    # Add custom percentile keys to be reported
    environment.stats.global_percentile_list = [50, 95, 97, 98, 99, 100]
    for s in environment.stats.entries.values():
        s.percentile_list = [50, 95, 97, 98, 99, 100]