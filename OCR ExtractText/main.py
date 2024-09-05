from PIL import Image
import pytesseract


def extract_text(image_path):
    # Open the image using PIL
    img = Image.open(image_path)
    
    # Extract text from image using pytesseract
    extracted_text = pytesseract.image_to_string(img)
    
    return extracted_text

# Path to your image
image_path = 'OCR ExtractText/image.png'

# Call the function and print the extracted text
text = extract_text(image_path)
print("Extracted Text: \n", text)
