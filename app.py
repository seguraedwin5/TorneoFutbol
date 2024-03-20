from flask import Flask, jsonify, request, render_template_string
from itertools import combinations

app = Flask(__name__)

# Lista de equipos
teams = ["Millonarios FC",
         "Nacional FC",
         "America FC",
         "Junior FC"]

# Diccionario de Victorias por Equipos
victories = {team: 0 for team in teams}

def get_match_teams_combinations(teams):
    return list(combinations(teams, 2))

# Index
@app.route('/')
def index():
    
    rounds = get_match_teams_combinations(teams)
    
    return render_template_string(
        open('templates/index.html').read(),
        teams=teams,
        matches=rounds
    )

# Ruta: Obtener Ganador
@app.route('/get_winner', methods=['POST'])
def get_winner():
    
    results = request.json['resultados']
    
    for result in results:
        victories[result] += 1
    
    winner = max(victories, key=victories.get)
    
    return jsonify({'winner': winner})

if __name__ == '__main__':
    app.run(debug=True)
