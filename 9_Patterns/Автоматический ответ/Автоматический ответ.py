from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def home(title):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    science_professions = ['врач', 'инженер', 'специалист']
    if any(map(lambda x: x in prof, science_professions)):
        text = 'Научные симуляторы'
        path = url_for('static', filename='img/MARS-2-2.png')
    else:
        text = 'Инженерные тренажеры'
        path = url_for('static', filename='img/MARS-2-1.png')
    return render_template('index.html', text=text, path=path)


@app.route('/list_prof/<list>')
def list_prof(list):
    if list == 'ol':
        type = 1
    elif list == 'ul':
        type = 0
    else:
        return f'Ошибка, "{list}" - неправельный тип отображения, допустимы: "ol", "ul"'
    prof_list = ['Пилот', 'Строитель', 'Врач', 'Штурман', 'Инженер',
                 'Пилот дронов', 'Климатолог', 'Экзобиолог', 'Инженер-исследователь']

    return render_template('index_prof_list.html', type=type, prof_list=prof_list)


@app.route('/answer', methods=['POST', 'GET'])
@app.route('/auto_answer', methods=['POST', 'GET'])
def auto_answer():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/profile.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="classSelect"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас оброзавание?</label>
                                        <select class="form-control" id="education" name="education">
                                          <option>нет оброзавания</option>
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                          <option>профессиональное</option>
                                        </select>
                                     </div>
                                    <label for="classSelect"></label>
                                    <label for="classSelect">Какие у вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules1" name="in_is">
                                        <label class="form-check-label" for="acceptRules1">инженер-исследователь</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules2" name="pil">
                                        <label class="form-check-label" for="acceptRules2">пилот</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules3" name="sto">
                                        <label class="form-check-label" for="acceptRules3">строитель</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules4" name="exb">
                                        <label class="form-check-label" for="acceptRules4">экзобиолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="in_tr">
                                        <label class="form-check-label" for="acceptRules5">инженер по терраформированию</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules6" name="vr">
                                        <label class="form-check-label" for="acceptRules6">врач</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules7" name="klim">
                                        <label class="form-check-label" for="acceptRules7">климатолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules8" name="prog">
                                        <label class="form-check-label" for="acceptRules8">программист</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules9" name="prf_rad_arm">
                                        <label class="form-check-label" for="acceptRules9">специалист по радиационной защите</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules10" name="astrg">
                                        <label class="form-check-label" for="acceptRules10">астрогеолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules11" name="shtur">
                                        <label class="form-check-label" for="acceptRules11">штурман</label>
                                    </div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="answer" rows="3" name="answer"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        professions = []
        if 'accept' in request.form:
            readiness = 'True'
        else:
            readiness = 'False'

        if 'in_is' in request.form:
            professions.append('инженер-исследователь')
        if 'pil' in request.form:
            professions.append('пилот')
        if 'sto' in request.form:
            professions.append('строитель')
        if 'exb' in request.form:
            professions.append('экзобиолог')
        if 'in_tr' in request.form:
            professions.append('инженер по терраформированию')
        if 'vr' in request.form:
            professions.append('врач')
        if 'prog' in request.form:
            professions.append('программист')
        if 'klim' in request.form:
            professions.append('климатолог')
        if 'prf_rad_arm' in request.form:
            professions.append('специалист по радиационной защите')
        if 'astrg' in request.form:
            professions.append('астрогеолог')
        if 'shtur' in request.form:
            professions.append('штурман')

        data = {'surname': request.form['surname'],
                'name': request.form['name'],
                'education': request.form['education'],
                'profession': ', '.join(professions),
                'sex': request.form['sex'],
                'motivation': request.form['answer'],
                'readiness': readiness}

        return render_template('auto_answer.html', title='Анкета',
                          path_to_css='/static/css/profile_ansver.css', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
