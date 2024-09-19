from rembg import remove
from PIL import Image
import io

input_path = "/Users/juanlozadacalderon/downloads/Remove background/macacos.jpg"
output_path = "output.png"  # Cambiado a PNG para preservar la transparencia

# Abrir la imagen de entrada
with open(input_path, "rb") as input_file:
    input_data = input_file.read()

# Remover el fondo
result_data = remove(input_data)

# Convertir el resultado a una imagen de PIL
output = Image.open(io.BytesIO(result_data))

# Guardar la imagen de salida en formato PNG para preservar la transparencia
output.save(output_path)

