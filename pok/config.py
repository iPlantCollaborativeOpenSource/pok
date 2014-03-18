"""
Configuration should be easy.
"""
from abc import ABCMeta, abstractmethod
import operator

from impl import file as f
from impl import zk


def merge_configs(impls):
    """
    Merge all configurations in impls.
    Use the first configuration found in impls.
    """
    return reduce(operator.or_, [impl.config() for impl in impls])

config = merge_configs([f, zk])
