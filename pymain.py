import docker
from flask import Flask, render_template, request, redirect, session

client_docker = docker.from_env()
app = Flask(__name__, template_folder="templates", static_folder="templates/static")
app.secret_key = "PythonDevKey"

@app.route('/')
@app.route('/index')
def index():
    try:
        session['counter'] += 1
        dict_conteiners = {}
        conteiners = client_docker.api.containers()
        # for conteiner in conteiners:
        #     dict_conteiners[conteiner['Names'][0].strip('/')] = conteiner['Names'][0].strip('/')
        #     dict_conteiners[conteiner['State']] = conteiner['State']
        print(dict_conteiners)
    except:
        session['counter'] = 0
    return render_template('index.html', conteiners=conteiners)


@app.route('/contact')
def contact():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 0
    return render_template('contact.html')


@app.route('/add', methods = ['POST'])
def add():
    try:
        session['counter'] += 2
    except:
        session['counter'] = 0
    return render_template('add.html')


@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
    