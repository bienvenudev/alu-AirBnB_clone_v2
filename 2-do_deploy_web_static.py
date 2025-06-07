#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric import task, Connection
from os.path import exists


@task
def do_deploy(c, archive_path):
    """Function to distribute an archive to your web servers"""
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

# Run the script like this:
# $ fab do-deploy --archive-path=versions/file_name.tgz