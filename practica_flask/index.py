from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Inicio():
    return render_template('inicio.html')

@app.route('/cursos')
def Cursos():
    return render_template('cursos.html')

@app.route('/about')
def About():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
