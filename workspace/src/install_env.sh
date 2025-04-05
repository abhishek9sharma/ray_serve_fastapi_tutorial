#!/bin/bash
pip install uv
uv venv ray_env
source ray_env/bin/activate
uv pip install ipykernel nbconvert
uv pip install ray[serve] nest-asyncio litellm