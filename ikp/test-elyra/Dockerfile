FROM k8s-notebook

USER root

ADD start-elyra.sh /usr/local/bin/start-elyra.sh

RUN chmod ugo+x /usr/local/bin/start-elyra.sh && \
    apt-get update && apt-get install -y gcc g++ make gcc python3-dev python3-setuptools build-essential curl dirmngr apt-transport-https lsb-release ca-certificates &&\
    curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - &&\
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN python -m pip install --upgrade pip && \
    python -m pip install --ignore-installed --upgrade setuptools pandas && \
    echo "scripts-prepend-node-path=true" >> /home/jovyan/.npmrc && \
    echo "prefix=/home/jovyan/.npm-global" >> /home/jovyan/.npmrc && \
    mkdir -p /home/jovyan/.npm-global && \
    npm install -g yarn && \
    npm install -g npm
    
RUN conda install nodejs
RUN conda install -c conda-forge elyra && jupyter lab build
RUN jupyter serverextension list
RUN jupyter labextension list

WORKDIR /home/jovyan/work

CMD ["/usr/local/bin/start-elyra.sh"]

