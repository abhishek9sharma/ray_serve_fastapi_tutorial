from ray import serve

from .fastapi import app


@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 2})
@serve.ingress(app)
class RayAppAdvanced:
    pass


rayappadvanced = RayAppAdvanced.bind()
