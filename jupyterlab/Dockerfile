FROM jupyter-base-notebook:0.1

USER root

# APT packages
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

USER $NB_UID

# Conda packages
# Sage conflicts with the latest jupyterhub, thus we must relax the pinning
#RUN conda install --yes \
#    'jupyterhub' &&\
#    'sage=8.*' \
