import pronouncing
from itertools import compress

pronouncing.rhymes("no")

with open('Bob Dylan Master/Bob Dylan 2 Lyrics.txt', 'r', encoding="UTF-8") as file:
    text = file.read().splitlines()
    text = [i.replace('"', '') for i in text if not i == '']
    Rhyme = [i for i in text if i.split().pop().lower() in pronouncing.rhymes("free")]
    Rhyme = '\n'.join(Rhyme)

text[2].split().pop().lower() in pronouncing.rhymes("free")

text[2].split().pop().lower()