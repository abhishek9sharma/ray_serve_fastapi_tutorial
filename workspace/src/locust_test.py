from locust import HttpUser, between, task


class HelloWorldUser(HttpUser):
    # wait_time = 1.2

    @task
    def get_hello(self):
        headers = {"accept": "application/json"}
        x = self.client.get("/hello", headers=headers)
        print(x)
