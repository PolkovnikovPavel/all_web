import os

formats = ['Б', 'КБ', 'МБ', 'ГБ']
dimension = 1024


def human_read_format(size):
    format = formats[0]

    while size // dimension >= 1 and format != formats[-1]:
        format = formats[formats.index(format) + 1]
        size /= dimension
    return f'{round(size)}{format}'


def get_ﬁles_sizes():
    all_files = os.listdir()
    result = []
    for file in all_files:
        size = os.path.getsize(file)
        size = human_read_format(size)
        result.append(f'{file} {size}')
    return '\n'.join(result)


if __name__ == '__main__':
    print(get_ﬁles_sizes())
