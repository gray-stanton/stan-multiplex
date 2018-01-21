import paramiko as pm
import yaml
import os
import sys
import socket as sk

# Components of local
# Data file pool
# Remote hosts + connection info
# Remote host configurations to be transmitted
# Transmitting interface


def get_model(compiled_model_path)

def parse_yaml(remote_hosts_yaml)

def process(compiled_model_path, remote_hosts_config)

def create_job_pool(datafiles):
    """Creates job pool """

def setup_sockets(remote_conf, socket_num=19090):

def connect_to_host(hostname):
    """Opens ssh connection to given hostname, returns ssh object"""

def setup_hosts(remote_conf):
    for h in remote_conf['hosts']:
        con = connect_to_host(h)



def finished():
    pass
def listen():
    pass
def get_new_job(job_pool):
    pass
def postprocess():
    pass

if __name__ == "__main__":
    model_path = sys.argv[1]
    yaml_path = sys.argv[2]
    data_files = sys.argv[3:]
    remote_conf = parse_yaml(yaml_path)
    setup_sockets(remote_conf)
    setup_hosts(model_path, remote_conf)
    complete = False
    while not finished():
        listen()
    postprocess()








