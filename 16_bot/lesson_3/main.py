import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()

text = sys.stdin.read()
ru_letters = set('ёйцукенгшщзхъфывапролджэячсмитьбю \n')
words = ''.join(i for i in text.lower() if i in ru_letters).split()

for word in words:
    tag = str(morph.parse(word.strip())[0].tag).split(',')[2].split()
    if 'NOUN' in morph.parse(word.strip())[0].tag:
        if 'anim' in morph.parse(word.strip())[0].tag:
            if len(tag) == 1:
                print(morph.parse('Живое')[0].inflect(
                    {tag[0], 'sing'}).word.capitalize())

            elif len(tag) != 1 and tag[1] != 'plur':
                print(morph.parse('Живое')[0].inflect(
                    {tag[0], 'sing'}).word.capitalize())

            else:
                print(morph.parse('Живое')[0].inflect(
                    {'plur'}).word.capitalize())

        else:
            if len(tag) == 1:
                print('Не ' + morph.parse('Живое')[0].inflect(
                    {tag[0], 'sing'}).word)

            elif tag[1] != 'plur':
                print('Не ' + morph.parse('Живое')[0].inflect(
                    {tag[0], 'sing'}).word)

            else:
                print('Не ' + morph.parse('Живое')[0].inflect({'plur'}).word)
    else:
        print('Не существительное')
