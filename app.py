from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Rota principal para o site
@app.route('/')
def index():
    return render_template('index.html')  # Carrega a página HTML

# Função que gerencia as mensagens enviadas
@socketio.on('message')
def handle_message(msg):
    print(f'Mensagem recebida: {msg}')
    send(msg, broadcast=True)  # Envia a mensagem para todos os usuários conectados

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
