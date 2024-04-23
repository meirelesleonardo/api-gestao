import os
from flask import render_template
from apps.gestao import create_app

# Criar o aplicativo Flask
app = create_app()


@app.route("/")
def index():
    return render_template("index.html")
 
 
# Se o arquivo for importado por um servidor WSGI, este será o ponto de entrada
if __name__ == "__main__":
    app.run(port=5004)
