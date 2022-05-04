from machinetranslation import translator
from machinetranslation.translator import french_to_english, english_to_french
#from translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    englishtext = english_to_french(textToTranslate)
    return englishtext


@app.route("/frenchToEnglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext = french_to_english(textToTranslate)
    return frenchtext


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
