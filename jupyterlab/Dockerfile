FROM jupyter/scipy-notebook:13b866ff67b9

LABEL maintainer="Luca De Feo <https://defeo.lu/>"

USER root

# APT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    scilab \
    libpari-dev \
    sagemath \
    sagemath-jupyter \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Conda packages
# Sage conflicts with the latest jupyterhub, thus we must relax the pinning
RUN conda install --yes \
    'jupyterhub' &&\
#    'sage=8.*' \
    fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include

RUN pip install \
    pari_jupyter \
#    PySingular jupyter_kernel_singular \
    scilab-kernel && \
    fix-permissions $CONDA_DIR

# Fix SageMath kernel
USER root
RUN sed -i 's/"\/usr\/bin\/sage"/"env", "PATH=\/usr\/local\/sbin:\/usr\/local\/bin:\/usr\/sbin:\/usr\/bin:\/sbin:\/bin", "\/usr\/bin\/sage"/' /usr/share/jupyter/kernels/sagemath/kernel.json
USER $NB_UID

# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
