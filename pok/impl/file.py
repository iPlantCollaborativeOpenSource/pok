"""
Implementation of a file configuration.
"""
import os
from ConfigParser import SafeConfigParser


def config():
    """
    Return configuration settings from /etc/default/iplant.
    """
    f = SafeConfigParser()
    if os.path.exists("/etc/default/iplant"):
        f.read("/etc/default/iplant")
    # TODO: Return in a similar python data structure.
    return f
