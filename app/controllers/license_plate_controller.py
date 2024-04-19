from flask import Blueprint, request, jsonify
from app.services.license_plate_service import detect_license_plate
import cv2

license_plate_bp = Blueprint('license_plate', __name__)

@license_plate_bp.route('/detect', methods=['POST'])
def detect_license_plate_route():
    # Recebe a imagem do request
    image = cv2.imdecode(np.fromstring(request.files['image'].read(), np.uint8), cv2.IMREAD_COLOR)

    # Chama o serviço para detectar a placa de carro na imagem
    text, plates = detect_license_plate(image)

    # Retorna as informações da detecção de placa de carro
    return jsonify({'text': text, 'plates': plates})
