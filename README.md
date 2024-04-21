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
├── presentation/
│   ├──frontend_gestao/
|   │   ├── static/
|   │   │   ├── css/
|   │   │   ├── js/
|   │   │   └── images/
|   │   ├── templates/
|   │   │   ├── base.html
|   │   │   ├── home.html
|   │   │   └── partials/
|   │   │       ├── header.html
|   │   │       └── footer.html
|   │   └── __init__.py
├── tests/
│   └── __init__.py
└── run.py


# Servidor de produção
gunicorn -b 0.0.0.0:8025 wsgi:app


# Criar Ambiente venv
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
