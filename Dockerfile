FROM python:3.12-slim-bookworm
EXPOSE 9001
EXPOSE 8000
EXPOSE 8100
EXPOSE 8265
EXPOSE 8080
EXPOSE 6006
EXPOSE 6379
EXPOSE 9000



#https://docs.astral.sh/uv/guides/integration/docker/#available-images
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates git tree
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

RUN uv pip install jupyterlab --system
COPY startup.sh /ray_serve_tutorial/startup.sh
COPY README.md /ray_serve_tutorial/README.md
RUN chmod +x /ray_serve_tutorial/startup.sh
ENTRYPOINT ["/ray_serve_tutorial/startup.sh"]