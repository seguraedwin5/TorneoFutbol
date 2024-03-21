from flask import Flask, jsonify, request, render_template_string
from match import match


app = Flask(__name__)

# Index
@app.route('/')
def index():
    
    rounds = match_object.get_match_teams_combinations()
    
    return render_template_string(
        open('templates/index.html').read(),
        teams=match_object.get_teams(),
        matches=rounds
    )

# Ruta: Obtener Ganador
@app.route('/get_winner', methods=['POST'])
def get_winner():
    
    results = request.json['resultados']
    
    for result in results:
        match_object.set_victory(result,1)
    
    winner = max(match_object.get_victories(), key=match_object.get_victories().get)
    match_object.reload_victories()
    
    return jsonify({'winner': winner})

@app.post('/add_equipo/<string:equipo>')
def agregar_equipo(equipo):
    match_object.add_team(equipo=equipo)
    return jsonify({'mensaje' : f'equipo {equipo} agregado correctamente'})

if __name__ == '__main__':
    match_object = match(["Millonarios FC", "Nacional FC", "America FC", "Junior FC"])
    app.run(debug=True)
