#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents
# of the web_static folder of the AirBnB Clone repo

from fabric.api import local
from datetime import datetime
import os


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
