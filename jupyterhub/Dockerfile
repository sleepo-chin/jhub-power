FROM openjupyter/jupyterhub-ppc64le:1.1.0

RUN useradd admin

COPY jupyterhub_config.py .

RUN pip install \
    dockerspawner==0.10.0 \
    kubernetes==10.0.* \
    jupyterhub-kubespawner
