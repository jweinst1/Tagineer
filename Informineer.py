from flask import Flask, render_template, request
from POS_tagger import *
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(result=None):
    if request.args.get('mail', None):
        retrieved_text = request.args['mail']
        result = process_text(retrieved_text)
    return render_template('index.html', result=result)


def process_text(text):
    elem = Sentence(text)
    tag = tag_avna(elem)
    tag = tag_pronouns(tag)
    tag = tag_preposition(tag)
    tag = tag_coord_conj(tag)
    tag = tag_subord_conj(tag)
    tag = tag_be_verbs(tag)
    tag = post_processing(tag)
    tag = tag_noun_plurals(tag)
    tagged = package_sentence(tag)
    new = str(tagged)
    return new


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
