#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

import os
from fabric import task, Connection  # For remote connections
from datetime import datetime
from os.path import exists
from invoke import Context  # For local commands

@task
def do_pack(_):
    """Create a .tgz archive from the web_static folder."""
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local = Context()
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)
    
    try:
        local.run("mkdir -p versions")
        local.run(f"tar -cvzf {archive_path} web_static")
        if os.path.exists(archive_path):
            print(f"Archive created: {archive_path}")
            return archive_path
        else:
            print("Failed to create archive")
            return None
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None


@task
def do_deploy(c, archive_path):
    """Distribute the archive to web servers and deploy it."""
    if not exists(archive_path):
        return False
    
    hosts = ["18.212.50.164", "44.206.233.118"]
    
    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        
        for host in hosts:
            conn = Connection(
                host=host,
                user="ubuntu",
                connect_kwargs={"key_filename": "~/.ssh/school"}
            )
            
            conn.put(archive_path, "/tmp/")
            conn.run("mkdir -p {}/".format(path_name))
            conn.run('tar -xzf /tmp/{} -C {}/'.format(file_name, path_name))
            conn.run("rm /tmp/{}".format(file_name))
            conn.run("mv {}/web_static/* {}".format(path_name, path_name))
            conn.run("rm -rf {}/web_static".format(path_name))
            conn.run('rm -rf /data/web_static/current')
            conn.run('ln -s {}/ /data/web_static/current'.format(path_name))
            conn.close()
            
        return True
    except Exception:
        return False


@task
def deploy(c):
    """Create and distribute an archive to web servers."""
    archive_path = do_pack(c)
    if not archive_path:
        return False

    return do_deploy(c, archive_path)

# Run the script like this:
# $ fab do-pack
# $ fab do-deploy --archive-path=versions/file_name.tgz
# $ fab deploy