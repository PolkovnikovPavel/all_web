class pas_Exception(Exception):
    pass


combination = ['йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх',
               'зхъ',
               'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ'
                                                                       'ячс',
               'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю',
               'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
               'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
               'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
               'qwd', 'wdf', 'dfk', 'fkj', 'kju', 'jur', 'url',
               'ase', 'set', 'etg', 'tgy', 'gyn', 'yni', 'nio', 'ioh',
               'zxc', 'xcv', 'cvb', 'vbp', 'bpm']


def check_password(pas):
    if len(pas) <= 8:
        return False
    if pas.isupper() or pas.islower():
        return False
    if pas.isdigit() or pas.isalpha():
        return False
    if any(map(lambda x: x in pas.lower() or x in pas[::-1].lower(),
               combination)):
        return False

    return True


if check_password(input()):
    print('ok')
else:
    print('error')
