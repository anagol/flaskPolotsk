from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/banks')
def banks():
    return render_template('banks.html', title='Банки')


@app.route('/culture')
def culture():
    return render_template('culture.html', title='Культура')


@app.route('/education')
def education():
    return render_template('education.html', title='Образование')


@app.route('/food')
def food():
    return render_template('food.html', title='Питание')


@app.route('/transport')
def transport():
    return render_template('food.html', title='Транспорт')


@app.route('/sport')
def sport():
    return render_template('sport.html', title='Спорт')


@app.route('/history')
def history():
    return render_template('history.html', title='История Полоцка')


@app.route('/shopping')
def shopping():
    return render_template('shopping.html', title='Торговля')


@app.route('/organization')
def organization():
    return render_template('organization.html', title='Организации')


@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html', title='Досуг')


@app.route('/postcard')
def postcard():
    return render_template('postcard.html', title='Полоцк на старых открытках')


if __name__ == '__main__':
    app.run(debug=True)
