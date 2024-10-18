from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Fonction pour générer la table de multiplication
def generate_table(number):
    table = []
    for i in range(1, 13):
        table.append(f"{number} x {i} = {number * i}")
    return table

# Route principale qui retourne la page HTML
@app.route('/')
def index():
    return render_template('front.html')

# Route qui retourne la table de multiplication
@app.route('/get-table', methods=['POST'])
def get_table():
    data = request.get_json()
    number = data.get('number')
    table = generate_table(number)
    return jsonify(table)

if __name__ == '__main__':
    app.run(debug=True)
