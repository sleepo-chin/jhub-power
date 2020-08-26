# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os

## Generic
c.JupyterHub.admin_access = True
#c.KubeSpawner.default_url = '/lab'

## Docker spawner
c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'
c.KubeSpawner.image = "jupyter-notebook-1" 
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = '0.0.0.0'

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.KubeSpawner.notebook_dir = notebook_dir
c.KubeSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

#Authentication
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = "P@ssw0rd"

# Other stuff
c.KubeSpawner.cpu_limit = 1
c.KubeSpawner.mem_limit = '2G'

c.JupyterHub.shutdown_on_logout = True

c.LocalAuthenticator.create_system_users = True
