#!/usr/bin/python3
# A fabric script that creates and distributes an archive to the web servers

from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ['54.146.74.212', '18.207.139.48']


def do_pack():
    """
    Generates a .tgz archive of the web_static folder.
    """

    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        name_format = "web_static_{}.tgz".format(now)
        local("tar -cvzf versions/{} web_static".format(name_format))
        return "versions/{}".format(name_format)
    except Exception:
        return None


def do_deploy(archive_path):
    """
    A function that distributes an archive
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        a_name = os.path.basename(archive_path)
        a_box = '/data/web_static/releases/' + a_name.split('.')[0]
        run('mkdir -p {}'.format(a_box))

        run('tar -xzf /tmp/{} -C {}'.format(a_name, a_box))

        run('rm /tmp/{}'.format(a_name))

        run('mv {}/web_static/* {}'.format(a_box, a_box))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(a_box))

        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """
    Creates and distributes
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return False
