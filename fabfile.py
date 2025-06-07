#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers."""

import os
from datetime import datetime
from invoke import Context  # For local commands
from fabric import task, Connection  # For remote connections
from os.path import exists

# Web server IPs
hosts = ["18.212.50.164", "44.206.233.118"]

@task
def do_pack(_):
    """Create a .tgz archive from the web_static folder."""
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{time_stamp}.tgz"
    local = Context()

    try:
        local.run("mkdir -p versions")
        local.run(f"tar -cvzf {archive_path} web_static")
        if os.path.exists(archive_path):
            print(f"✅ Archive created: {archive_path}")
            return archive_path
        else:
            print("❌ Failed to create archive")
            return None
    except Exception as e:
        print(f"❌ Error creating archive: {e}")
        return None


@task
def do_deploy(c, archive_path):
    """Distribute the archive to web servers and deploy it."""
    if not exists(archive_path):
        print("❌ Archive path does not exist")
        return False

    file_name = os.path.basename(archive_path)
    name = file_name.split(".")[0]
    release_path = f"/data/web_static/releases/{name}"

    try:
        for host in hosts:
            print(f"📡 Connecting to {host}...")
            conn = Connection(
                host=host,
                user="ubuntu",
                connect_kwargs={"key_filename": "~/.ssh/school"}
            )

            print("📤 Uploading archive...")
            conn.put(archive_path, "/tmp/")
            conn.run(f"mkdir -p {release_path}")
            conn.run(f"tar -xzf /tmp/{file_name} -C {release_path}")
            conn.run(f"rm /tmp/{file_name}")
            conn.run(f"mv {release_path}/web_static/* {release_path}/")
            conn.run(f"rm -rf {release_path}/web_static")
            conn.run("rm -rf /data/web_static/current")
            conn.run(f"ln -s {release_path} /data/web_static/current")
            print(f"✅ Deployment to {host} successful.")
            conn.close()

        return True
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        return False


@task
def deploy(c):
    """Create and distribute an archive to web servers."""
    archive_path = do_pack(c)
    if not archive_path:
        return False
    return do_deploy(c, archive_path)
