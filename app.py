from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Lista de equipos
teams = ["Millonarios",
         "Nacional",
         "America",
         "Junio"]

# Diccionario de Victorias por Equipos
victories = {team: 0 for team in teams}

# Index
@app.route('/')
def index():
    rounds = [
        (teams[0], teams[1]),
        (teams[2], teams[3]),
        (teams[0], teams[2]),
        (teams[1], teams[3])
    ]
    
    return render_template_string(
        open('templates/index.html').read(),
        equipos=teams,
        partidos=rounds
    )

# Ruta: Obtener Ganador
@app.route('/get_winner', methods=['POST'])
def get_winner():
    
    results = request.json['resultados']
    
    for result in results:
        victories[result] += 1
    
    winner = max(victories, key=victories.get)
    
    print(winner)
    
    return jsonify({'winner': winner})


if __name__ == '__main__':
    app.run(debug=True)
