from flask import Flask, jsonify

app = Flask(__name__)

teams = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4"]

@app.route('/')
def index():
    return '¡Bienvenido!'

if __name__ == '__main__':
    app.run(debug=True)