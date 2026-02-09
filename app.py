from flask import Flask, render_template, request
import re

app = Flask(__name__)

def show_match(text, expr):
    matches = re.findall(expr, text)
    return matches

@app.route('/', methods=['GET', 'POST'])
def home():
    matches = []
    text = ""
    expr = r"\b(?=\w*ra)(?=\w*pp)\w*\b"  # regex for words containing 'ra' and 'pp'

    if request.method == 'POST':
        text = request.form['input_text']
        matches = show_match(text, expr)

    return render_template('index.html', text=text, expr=expr, matches=matches)

if __name__ == '__main__':
    app.run(debug=True)