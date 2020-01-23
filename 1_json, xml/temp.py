import os

formats = ['Б', 'КБ', 'МБ', 'ГБ']
dimension = 1024

def human_read_format(size):
    format = formats[0]

    while size // dimension >= 1 and format != formats[-1]:
        format = formats[formats.index(format) + 1]
        size /= dimension
    return f'{round(size)}{format}'


if __name__ == '__main__':
    pass
