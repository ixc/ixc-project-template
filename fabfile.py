from deployo.contrib.deployment.gunicorn import *
from deployo.tasks import environment
from fabric.api import env, task
env.use_ssh_config = True
