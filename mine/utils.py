from minecraft_launcher_lib.utils import get_minecraft_directory, get_version_list

def get_minectaft_dir(dir):
    return get_minecraft_directory().replace('minecraft', dir)

def get_minectaft_version_list():
    return get_version_list()