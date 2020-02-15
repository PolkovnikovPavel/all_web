import os
import time
from zipfile import ZipFile


def make_reserve_arc(source, dest):
    dest = time.strftime(f'{dest} %d.%m.%Y  %H-%M-%S')
    os.mkdir(dest)
    with ZipFile(source) as myzip:
        for name in myzip.namelist():
            if '.' in name:
                file = myzip.open(name)
                text = file.read()
                with open(f'{dest}/{name}', 'wb') as file:
                    file.write(text)
            else:
                os.mkdir(f'{dest}/{name[:-1]}')