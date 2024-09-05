import requests
from PIL import Image
import pytesseract
from io import BytesIO

def extract_text(image_path=None, image_url=None):
    if image_url:
        # Fetch the image from the URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
    elif image_path:
        # Open the image from the local file system
        img = Image.open(image_path)
    else:
        raise ValueError("Either image_path or image_url must be provided.")
    
    # Extract text from the image using pytesseract
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text

# Example usage
image_path = 'OCR ExtractText/Handwriting-test-dataset-for-OCR-operation.png'  # or leave as None if using URL
image_url = None  # or leave as None if using local image

# Extract and print text from either a URL or local image
text = extract_text(image_path=image_path, image_url=image_url)
print("Extracted Text: \n", text)
