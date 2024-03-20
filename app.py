from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Lista de equipos
teams = ["Millonarios",
         "Nacional",
         "America",
         "Junio"]

@app.route('/')
def index():
    return render_template('index.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
