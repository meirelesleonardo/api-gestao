# **Projeto API Flask com DDD**

Este projeto nasceu com o propósito de explorar de forma prática o desenvolvimento de uma API em Flask, seguindo os princípios do Domain-Driven Design (DDD). À medida que novas funcionalidades são estudadas e implementadas, o projeto continua a evoluir, adotando uma estrutura modular semelhante à encontrada no Django, mas com o foco no desacoplamento dos controladores e na implementação de serviços distribuídos em diferentes módulos.

## **Funcionalidades Implementadas:**

- Desenvolvimento de uma API para Webhook totalmente funcional, utilizada inclusive para automatizar o processo de implantação sempre que há um novo push no repositório do GitHub.
- Criação de um projeto básico para o frontend.

## **Futuras Implementações Planejadas:**

- Construção de um portfólio de aplicativos base que possam ser adaptados para diferentes segmentos de negócios, oferecendo operações CRUD simples e flexíveis.
- Integração de um sistema de leitura de placas de veículos com o auxílio de Inteligência Artificial, com potencial para expandir para a detecção de outros padrões.
- Integração com bancos de dados MongoDB e Redis para armazenamento e gerenciamento de dados.

# Estrutura Inicial do Projeto
api-gestao/
│
├── apps/
│   ├── __init__.py
|   ├── api-gestao/
|   │   ├── __init__.py
|   │   ├── controllers/
|   │   │   └── __init__.py
|   |   │   ├── models/
|   │   │   └── __init__.py
|   │   ├── services/
|   │   │   └── __init__.py
|   │   └── utils/
|   │       └── __init__.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── tests/
│   └── __init__.py
└── run.py


# Criar Ambiente venv
Obs.: Os comandos abaixo devem ser executados dentro da pasta do seu aplicativo

## Linux
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv

python3  -m venv venv 
source venv/bin/activate

pip3 install --no-cache-dir -r requirements.txt

Deactive 


## Windows
python -m pip install --user virtualenv
python.exe -m pip install --upgrade pip

python -m virtualenv venv
.\venv\Scripts\activate.bat

pip install --no-cache-dir -r requirements.txt

Deactivate

# Servidor de produção exemplo de configuração base
## Exemplo de Script que incializa um serço
- **/home/meu_usuario/scripts/meu_app_flask**
    
    ```bash
    #! /bin/bash
    cd /home/meu_usuario/projetos/meu_app_flask/ # Ajustar o nome do usuário, nome da pasta do aplicativo
    source ./venv/bin/activate
    gunicorn -b 0.0.0.0:5000 wsgi:app
    
    ```
## Criar um serviço
## Criar serviço para API Gestão em Flask

```bash
sudo vi /etc/systemd/system/api-gestao.service

[Unit]
Description=meu_app_flask Service
After=network.target

[Service]
User=meu_usuario
Group=meu_usuario
WorkingDirectory=/home/meu_usuario/projetos/meu_app_flask
Environment="PATH=/home/meu_usuario/projetos/meu_app_flask/venv/bin"
Environment="FLASK_ENV=production"
ExecStart=/bin/bash /home/meu_usuario/scripts/meu_app_flask.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Recarregue o systemd para aplicar as alterações
sudo systemctl daemon-reload

sudo chmod -R 755 /home/meu_usuario/projetos/meu_app_flask/venv

sudo systemctl enable meu_app_flask.service
sudo systemctl start meu_app_flask.service

```

## Nginx
- **Exemplo básico para app em Flask**
    
    ```bash
    server {
        listen 80;
        server_name seu_dominio.com;
    
        location /static/ {
            alias /caminho/para/seus/arquivos/estaticos/;
        }
    
        location / {
            include proxy_params;
            proxy_pass http://localhost:5000;  # Substitua 5000 pela porta do seu aplicativo Flask
        }
    }
    
    ```


