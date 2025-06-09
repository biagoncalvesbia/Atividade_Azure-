from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Mundooo! esta funcionando professor mauricio:)"

if __name__ == '__main__':
    app.run()
