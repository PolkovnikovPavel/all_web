def human_read_format(size):
    formats = ['Б', 'КБ', 'МБ', 'ГБ']
    dimension = 1024
    format = formats[0]

    while size // dimension >= 1 and format != formats[-1]:
        format = formats[formats.index(format) + 1]
        size /= dimension
    return f'{round(size)}{format}'
