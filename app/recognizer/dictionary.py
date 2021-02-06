from os.path import join, dirname


FILE_DIR = dirname(__file__)
DATA_DIR = join(FILE_DIR, '../../data')


def load_dict(name):
    path = join(DATA_DIR, name)
    with open(path, encoding='utf8') as file:
        for line in file:
            index = line.find('#')
            if index > 0:
                line = line[:index]
            yield line.rstrip()
