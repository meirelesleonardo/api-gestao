# Estrutura Inicial do Projeto
api-gestao/
│
├── app/
│ ├── init.py
│ ├── controllers/
│ │ └── init.py
│ ├── models/
│ │ └── init.py
│ ├── services/
│ │ └── init.py
│ └── utils/
│ └── init.py
├── config/
│ ├── init.py
│ └── settings.py
├── tests/
│ └── init.py
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
