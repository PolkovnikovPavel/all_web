from flask import Flask, render_template, url_for


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
