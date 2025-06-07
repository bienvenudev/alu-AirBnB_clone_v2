#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your
AirBnB Clone repo, using
the function do_pack."""

from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """Function to generate a .tgz archive from the contents of the web_static
    folder."""

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    c.run("mkdir -p versions")
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)
    c.run("tar -cvzf {} web_static".format(archive_path))
    if os.path.exists(archive_path):
        return archive_path
    else:
        return None

# Run the script like this:
# $ fab do-pack