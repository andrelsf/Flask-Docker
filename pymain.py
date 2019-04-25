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
        conteiners = client_docker.api.containers()
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


@app.route('/docker_images', methods = ['GET'])
def add():
    try:
        session['counter'] += 1
        images = client_docker.api.images()
    except:
        session['counter'] = 0
    return render_template('docker_images.html', images=images)


@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
    