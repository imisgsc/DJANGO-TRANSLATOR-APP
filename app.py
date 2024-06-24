from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        translated_text = translator.translate(input_text, src=source_lang, dest=target_lang).text
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
