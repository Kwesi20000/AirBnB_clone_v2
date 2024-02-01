#!/usr/bin/python3
"""This compresses web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.237.79.224', '54.90.9.35']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
        """This deploys web files to server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # this upload archive
                put(archive_path, '/tmp/')

                # this create target dir
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # this uncompress archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # this remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # this move contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # this remove extraneous web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                # this delete pre-existing sym link
                run('sudo rm -rf /data/web_static/current')

                # this re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # returns true on success
        return True
