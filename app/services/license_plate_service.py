import cv2
import pytesseract
from openalpr import Alpr

import cv2
import pytesseract
from openalpr import Alpr

def detect_license_plate(image_path):
    # Carrega a imagem
    image = cv2.imread(image_path)

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplica um filtro de suavização para reduzir o ruído
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detecta as bordas na imagem usando o operador de Sobel
    edges = cv2.Canny(blurred, 50, 150)

    # Localiza contornos na imagem
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Itera sobre os contornos encontrados
    for contour in contours:
        # Aproxima o contorno para um polígono
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # Se o polígono tiver 4 vértices, é possível que seja uma placa de carro
        if len(approx) == 4:
            # Calcula a área do polígono
            area = cv2.contourArea(contour)

            # Se a área for razoável, desenha um retângulo em torno da placa
            if 1000 < area < 5000:
                x, y, w, h = cv2.boundingRect(approx)
                
                # Recorta a região da placa da imagem original
                plate_image = gray[y:y+h, x:x+w]
                
                # Realiza OCR na região da placa usando Tesseract
                text = pytesseract.image_to_string(plate_image, config=r'--oem 3 --psm 6')
                
                # Retorna o texto da placa encontrado
                return text

    # Se nenhuma placa for encontrada, retorna None
    return None




if __name__ == "__main__":
    # Chama a função para detectar placas de carro em uma imagem
    plate_text = detect_license_plate('image.jpg')

    # Exibe o texto da placa detectada
    if plate_text:
        print("Placa detectada:", plate_text)
    else:
        print("Nenhuma placa detectada.")