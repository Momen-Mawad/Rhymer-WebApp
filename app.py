from flask import Flask, render_template, request
from flask_caching import Cache
import pronouncing

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        word = request.form.get('Rhyme-Word')
        file = request.files['file']
        text = file.read().splitlines()
        text = [i.decode("utf-8") for i in text if i]
        text = [i for i in text if i.split().pop().lower() in pronouncing.rhymes(word)]
        return render_template('main.html', file=text)

    return render_template('main.html')

if __name__== "__main__":
    app.secret_key = '123456'
    app.run(debug='Enable', use_reloader=True)

