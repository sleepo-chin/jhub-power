FROM k8s-notebook

USER root

ADD start-elyra.sh /usr/local/bin/start-elyra.sh

RUN chmod ugo+x /usr/local/bin/start-elyra.sh && \
    apt-get update && apt-get install -y gcc g++ make libssl-dev libffi-dev python-dev gcc python3-dev python3-setuptools build-essential curl dirmngr apt-transport-https lsb-release ca-certificates &&\
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn && \
    rm -rf /var/lib/apt/lists/*

ENV PKG_CONFIG_PATH="/usr/lib/powerpc64le-linux-gnu/pkgconfig"
ENV LDFLAGS="-L/usr/lib/powerpc64le-linux-gnu"

USER $NB_USER

RUN python -m pip install --upgrade pip && \
    python -m pip install --ignore-installed --upgrade setuptools pandas && \
    echo "scripts-prepend-node-path=true" >> /home/jovyan/.npmrc && \
    echo "prefix=/home/jovyan/.npm-global" >> /home/jovyan/.npmrc && \
    mkdir -p /home/jovyan/.npm-global && \
    npm install -g yarn && \
    npm install -g npm
    
RUN conda install nodejs

RUN pip install --ignore-installed terminado
#COPY ./elyra-1.1.0 /tmp/elyra
RUN cd /tmp && git clone https://github.com/elyra-ai/elyra.git && \
    cd /tmp/elyra && git checkout tags/v1.2.1 -b v1.2.1 && \
    make UPGRADE_STRATEGY=eager install && \
    rm -rf /tmp/elyra

USER $NB_USER

WORKDIR /home/jovyan/work

CMD ["/usr/local/bin/start-elyra.sh"]

