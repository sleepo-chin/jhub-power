FROM jupyterhub/jupyterhub:master

RUN useradd admin

COPY jupyterhub_config.py .

RUN pip install \
    dockerspawner==0.10.0 \
    jhub_cas_authenticator==1.0.0