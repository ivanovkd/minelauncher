from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.command import get_minecraft_command

from random_username.generate import generate_username

# make a UUID based on the host ID and current time
from uuid import uuid1

from subprocess import call

def minecraft_run(minecraft_directory, version_id, callback, username):
    # launcher always needs to check minecraft files before launching
    install_minecraft_version(versionid=version_id, minecraft_directory=minecraft_directory, callback=callback)

    # prevent empty username by generating random
    if username == '':
        username = generate_username()[0]
    
    options = {
        'username': username,
        'uuid': str(uuid1()),
        'token': ''
    }

    call(get_minecraft_command(version=version_id, minecraft_directory=minecraft_directory, options=options))