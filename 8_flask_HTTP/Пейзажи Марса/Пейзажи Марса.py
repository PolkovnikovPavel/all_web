from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def advertising():
    lines = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнем с Марса!',
             'Присоединяйся!']
    return '</br>'.join(lines)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.jpg')
    }" alt="здесь должна была быть картинка марса">
                    <h3>Вот она какая, красная планета<h3>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for(
        'static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.jpg')
    }" alt="здесь должна была быть картинка марса">
                        <div class="alert alert-dark" role="alert">
                         Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                         Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-dark" role="alert">
                         Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                         И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                         Присоединяйся!
                        </div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    ''' style.css
form.login_form {
    margin-left: auto;
    margin-right: auto;
    max-width: 450px;
    background-color: #ffca86;
    border: 1px solid gray;
    border-radius: 5px;
    padding: 10px;
}
h1 {
    text-align: center
}
h3 {
    text-align: center
}
    '''

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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
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
                                          <option>професиональное</option>
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
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    types_of_styles = ['alert-success', 'alert-dark', 'alert-danger']
    planets_description = {'марс': [('Эта планета близка к Земле', 1),
                                ('На ней много ресурсов', 1),
                                ('На ней есть вода и атмосфера', 1),
                                ('На есть небольшое магнитное поле', 2),
                                ('Наконец, она просто красива!', 1)],
                          'земля': [('Эта наш дом!', 1),
                                ('На ней очень много ресурсов', 1),
                                ('На ней есть много воды и атмосферы', 1),
                                ('На есть магнитное поле', 1),
                                ('Земля не повтарима!', 1)],
                          'луна': [('Эта планета близка к Земле', 1),
                                ('На ней мало ресурсов', 3),
                                ('На ней почти нет атмосферы и нет воды', 3),
                                ('На есть небольшое магнитное поле', 2),
                                ('Она усыпана кратерами', 2)],
                          'юпитер': [('Эта планета близка к Марсу', 2),
                                ('Он просто газовый гигант', 3),
                                ('На нём нет ничего', 3),
                                ('На есть магнитное поле', 2),
                                ('Наконец, он самый большой в солнечной системме!', 1)],
                          'меркурий': [('Эта планета близка к Венере', 2),
                                ('На нём не сильно много ресурсов', 2),
                                ('На нём совсем маленькая атмосфера', 3),
                                ('На есть небольшое магнитное поле', 2),
                                ('Наконец, он самый близкий к солнцу!', 1)],
                          'нептун': [('Эта планета близка к Урану', 2),
                                ('На нём очень холодно', 3),
                                ('На нём нет атмосферы', 3),
                                ('На есть небольшое магнитное поле', 2),
                                ('Наконец, он самый далёкий от солнца!', 2)]}

    if planet_name.lower() not in planets_description:
        return f'<h2>По вашему выбору ({planet_name}) ничего не нашлось</h2>'

    description = planets_description[planet_name.lower()]
    styles = list(map(lambda x: types_of_styles[x[1] - 1], description))
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}</h1>
                        <div class="alert {styles[0]}" role="alert">
                         <h5>{description[0][0]}</h5>
                        </div>
                        <div class="alert {styles[1]}" role="alert">
                         <h5>{description[1][0]}</h5>
                        </div>
                        <div class="alert {styles[2]}" role="alert">
                         <h5>{description[2][0]}</h5>
                        </div>
                        <div class="alert {styles[3]}" role="alert">
                         <h5>{description[3][0]}</h5>
                        </div>
                        <div class="alert {styles[4]}" role="alert">
                         <h5>{description[4][0]}</h5>
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}:</h2>
                        <div class="alert alert-success" role="alert">
                         <h2>Поздравляем! Ваш рейтинг после {level} этапа отбора</h2>
                        </div>
                        <h3>состовляет {rating}!</h3>
                         <div class="alert alert-warning" role="alert">
                         <h1>Желаем удачи!</h1>
                        </div>
                      </body>
                    </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':

        file = request.files['file'].read()
        form = request.files['file'].filename.split('.')[-1]

        with open(f'static/img/img.{form}', 'wb') as f:
            f.write(file)
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="/static/img/img.{form}" alt="здесь должна была быть ваша картинка">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="ru">
<head>
    <!-- Required meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

    <title>Пейзажи Марса</title>
</head>
<body>
<h1>Пейзажи Марса</h1>
<div class="container">
        <div id="carousel-basic" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                <li data-target="carousel-basic" data-slide-to="1"></li>
                <li data-target="carousel-basic" data-slide-to="2"></li>
                <li data-target="carousel-basic" data-slide-to="3"></li>
            </ol>

            <div class="carousel-inner" role="listbox">
                <div class="carousel-item active">
                    <img src="{url_for('static', filename='img/mars_1.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/mars_2.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/mars_3.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/mars_4.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
            </div>

            <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Назад</span>
            </a>
            <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Вперед</span>
            </a>
        </div>

    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
