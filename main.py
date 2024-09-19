from rembg import remove
from PIL import Image
import io

input_path = "./Remove background/macacos.jpg"
output_path = "output.png"  # Changed to PNG to preserve transparency

# Open imagen input
with open(input_path, "rb") as input_file:
    input_data = input_file.read()

# Remove background
result_data = remove(input_data)

# Convert the result to a PIL image
output = Image.open(io.BytesIO(result_data))

# Save the output image in PNG format to preserve transparency
output.save(output_path)

