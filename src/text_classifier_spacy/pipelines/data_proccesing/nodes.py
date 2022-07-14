import spacy
import json

from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split

path = "C:/Proyectos/TextClassificator-Spacy-Kedro/text-classifier-spacy/"


def convert():

    infile = path + "data/01_raw/train.json"
    with open(infile) as f:
        lines = f.readlines()

    train, test = train_test_split(lines, test_size=0.2, random_state=42)
    iterate("train", train)
    iterate("test", test)


def iterate(outfile, lines):
    outfile = path + "data//05_model_input//{0}.spacy".format(outfile)
    categories = ["POLITICS", "WELLNESS", "ENTERTAINMENT", "TRAVEL"]
    nlp = spacy.blank("en")
    db = DocBin()

    for line in lines:
        l = json.loads(line)
        doc = nlp.make_doc(l["headline"])
        doc.cats = {category: 0 for category in categories}
        doc.cats[l["category"]] = 1
        db.add(doc)
    db.to_disk(outfile)


convert()
