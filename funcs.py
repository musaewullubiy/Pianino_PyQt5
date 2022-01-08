import os


def get_names_from_dir(dir, key=None):
    dirs = os.scandir(dir)
    names = list()
    for i in dirs:
        name = i.name
        if key:
            if key(name):
                names.append(name)
        else:
            names.append(name)
    return names