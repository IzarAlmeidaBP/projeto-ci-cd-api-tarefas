from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Configurar pipeline CI/CD', 'description': 'Usar GitHub Actions para automatizar o build e teste', 'done': True},
    {'id': 2, 'title': 'Elaborar documento do projeto', 'description': 'Descrever o passo a passo da configuração', 'done': False}
]

@app.route('/', methods=['GET'])
def home():
    return "Bem-vindo à API de Tarefas!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)