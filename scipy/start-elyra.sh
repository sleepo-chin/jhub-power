
USER root
export NB_PORT=${NB_PORT:-8888}
export KERNEL_USERNAME=${KERNEL_USERNAME:-${NB_USER}}

echo "Kernel user: " ${KERNEL_USERNAME}
echo "JupyterLab port: " ${NB_PORT}
echo "Gateway URL: " ${JUPYTER_GATEWAY_URL}

echo "${@: -1}"

exec /usr/local/bin/start-singleuser.sh $*
