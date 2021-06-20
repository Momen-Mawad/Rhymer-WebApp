from flask import render_template, request, url_for, redirect
import pronouncing, pandas as pd
from model import lyricModel, db, app


dictionary = [u.__dict__ for u in db.session.query(lyricModel).all()]
for i in dictionary:
    del i['_sa_instance_state']

x = 'hello (yes) - what do you need .... no.txt'

with open(x, 'r', encoding='UTF-8'):
    y = x.readlines()
    print(y)

df = pd.DataFrame(dictionary)
df = df.sort_values(by=['lyrics'])
word = 'feel'
#dfFiltered = df.loc[df['text'].str.split().str[-1].isin(pronouncing.rhymes(word))]
dfFiltered = df.loc[df['lyrics'].str.split().str[-1].isin(pronouncing.rhymes(word))]
dfFiltered = dfFiltered.sort_values(by=['lyrics'])

index = list(range(0,29444))
global checklist2
checklist2 = []
i


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        checklist = request.form.getlist('checklisthtml')
        checklist = [int(x) for x in checklist]
        checklist3 = request.form.get('checklisthtml2')
        if checklist != checklist3:
            usage = lyricModel.query.filter_by(usage=1).all()
            for i in usage:
                i.usage = 0
            for i in checklist:
                x = lyricModel.query.filter_by(index=i).first()
                x.usage = 1
        try:
            db.session.commit()

        except:
            pass
        checklist2.extend(checklist)
        checklist22 = set(checklist2)
        checklist22 = list(checklist22)
        dictionary = [u.__dict__ for u in db.session.query(lyricModel).all()]
        for i in dictionary:
            del i['_sa_instance_state']
        df = pd.DataFrame(dictionary)
        word = request.form.get('Rhyme-Word')
        dfFiltered = df.loc[df['lyrics'].str.split().str[-1].isin(pronouncing.rhymes(word))]
        dfJSON = dfFiltered.to_json(orient='index')

        numberSyllable = int(request.form.to_dict().get('syllables-num'))
        return render_template('result.html', number=str(numberSyllable), checklist2=checklist22, checklist3=checklist3, dfJSON=dfJSON, word=word)

    return render_template('main.html')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    usage = lyricModel.query.filter_by(usage=1).all()
    for i in usage:
        i.usage = 0
    try:
        db.session.commit()
    except:
        pass
    return redirect(url_for('main'))


if __name__ == "__main__":
    app.secret_key = '123456'
    app.run(debug='Enable', use_reloader=True)