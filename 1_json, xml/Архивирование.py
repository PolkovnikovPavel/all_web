import os
import time
from zipfile import ZipFile


def make_reserve_arc(source, dest):
    zip_name = time.strftime(f'{source} %d.%m.%Y  %H-%M-%S')

    my_zip = ZipFile(f'{dest}/{zip_name}.zip', 'w')

    count = 1
    for currentdir, dirs, files in os.walk(source):
        if count != 1:
            way = '\\'.join(currentdir.split('\\')[1:])
            my_zip.write(currentdir, way)
        for filename in files:
            way = os.path.join(currentdir, filename)
            way = '\\'.join(way.split('\\')[1:])
            my_zip.write(os.path.join(currentdir, filename), way)
        count += 1
