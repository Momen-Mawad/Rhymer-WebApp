from flask import Flask, render_template, request, url_for, redirect
#from connect import df
import pronouncing, pandas as pd

df = pd.read_csv("static/data.csv").sort_values(by='syllables')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        word = request.form.get('Rhyme-Word')
        x = int(request.form.to_dict().get('syllables-num'))
        dfFiltered = df.loc[df['text'].str.split().str[-1].isin(pronouncing.rhymes(word))]
        dfFiltered = dfFiltered.loc[df['syllables'] == x]
        return render_template('result.html', file=dfFiltered.iterrows(), number=str(x), word=word)

    return render_template('main.html')

if __name__ == "__main__":
    app.secret_key = '123456'
    app.run(debug='Enable', use_reloader=True)