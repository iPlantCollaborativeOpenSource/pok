"""
Implementation of a zookeeper configuration.
"""
from kazoo import KazooClient


zk = KazooClient(hosts)

def config():
    """
    Return configuration settings from zookeeper.
    """
    # TODO: Get all the children and thier values. Return in a similar
    #       python data structure.
    return zk.get_children("/iplant/pok/")
