#!/usr/bin/env bash
# this removes all pyc file under this location - recursively

export POK_HOME=/opt/dev/pok # For dalloway, arturo

find ${POK_HOME} -name "*.pyc" -exec rm '{}' ';'
