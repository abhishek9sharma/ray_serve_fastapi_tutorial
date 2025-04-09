#!/bin/bash
pip install uv
uv venv ray_env
source ray_env/bin/activate
uv pip install ray[serve] 
uv pip install nest-asyncio litellm
uv pip install locust