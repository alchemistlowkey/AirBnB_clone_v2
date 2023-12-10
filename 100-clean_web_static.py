#!/usr/bin/python3
"""
A Fabric script that deletes out-of-date archives
"""

from fabric.api import *


env.hosts = ['54.146.74.212', '18.207.139.48']


def do_clean(number=0):
    """
    Using the do_clean function to delete out-of-date archives
    """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
