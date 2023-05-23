from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/machinetranslation/translator/english_to_french")
def english_to_french():

     textToTranslate = request.args.get('textToTranslate')

     text = translator.english_to_french(textToTranslate)

     return "Translated text to French: " + text

@app.route("/machinetranslation/translator/french_to_english")
def french_to_english():

     textToTranslate = request.args.get('textToTranslate')

     text = translator.french_to_english(textToTranslate)

     return "Translated text to english: " + text

@app.route("/")
def renderIndexPage():
  return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)