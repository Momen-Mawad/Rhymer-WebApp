from flask import Flask, render_template, request, url_for, redirect
#from connect import df
import pronouncing, pandas as pd

df = pd.read_csv("static/data.csv").sort_values(by='syllables').reset_index(drop=True)
df['usage'] = False
x = df[:100]
list(df.index)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        global df
        df2=df
        word = request.form.get('Rhyme-Word')
        numberSyllable = int(request.form.to_dict().get('syllables-num'))
        checklist = request.form.getlist('checklisthtml')
        checklist = [int(x) for x in checklist]
        for i in list(df2.index):
            if i in checklist:
                df.at[i, 'usage'] = True
            
        dfFiltered = df2.loc[df2['text'].str.split().str[-1].isin(pronouncing.rhymes(word))]
        dfJSON = dfFiltered.to_json(orient='index')
        return render_template('result.html', file=dfFiltered.iterrows(), df=df2,
                               number=str(numberSyllable), x=checklist, dfJSON=dfJSON, word=word)

    return render_template('main.html')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        df['usage'] = False
    return redirect(url_for('main'))


if __name__ == "__main__":
    app.secret_key = '123456'
    app.run(debug='Enable', use_reloader=True)