from apps.api_gestao import create_app

# Criar o aplicativo Flask
app = create_app()

# Se o arquivo for importado por um servidor WSGI, este será o ponto de entrada
if __name__ == "__main__":
    app.run(port=8025)
