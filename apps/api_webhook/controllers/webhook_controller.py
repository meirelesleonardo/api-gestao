from flask import Blueprint, request, abort
import hmac
import hashlib
import subprocess
from flask import Blueprint, jsonify
import sys
import os

BASE_DIR = os.path.abspath('./')
sys.path.append(BASE_DIR)

from config import variabbles


webhook_bp = Blueprint('webhook', __name__, url_prefix='/webhook')
WEBHOOK_SECRET = variabbles.WEBHOOK_SECRET_DEPLOY

@webhook_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'up'})

@webhook_bp.route('/deploy-connect-city', methods=['POST'])
def deploy_connect_city():
    signature = request.headers.get('X-Hub-Signature')
    if not signature:
        abort(400, "Signature header is missing")

    sha_name, signature = signature.split('=')
    if sha_name != 'sha1':
        abort(501, "Unsupported signature type")

    mac = hmac.new(bytes(WEBHOOK_SECRET, 'utf-8'), msg=request.data, digestmod=hashlib.sha1)
    assinatura = str(mac.hexdigest())
    if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
        abort(403, "Invalid signature")

    # Chama o script de deploy
    subprocess.run([variabbles.DEPLOY_CONNECT_CITY])

    return "Deployment started", 200

@webhook_bp.route('/deploy-api-gestao', methods=['POST'])
def deploy_api_gestao():
    signature = request.headers.get('X-Hub-Signature')
    if not signature:
        abort(400, "Signature header is missing")

    sha_name, signature = signature.split('=')
    if sha_name != 'sha1':
        abort(501, "Unsupported signature type")

    mac = hmac.new(bytes(WEBHOOK_SECRET, 'utf-8'), msg=request.data, digestmod=hashlib.sha1)
    assinatura = str(mac.hexdigest())
    if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
        abort(403, "Invalid signature")

    # Chama o script de deploy
    retorno = subprocess.run([variabbles.DEPLOY_API_GESTAO])
    print(retorno)

    return "Deployment started", 200


