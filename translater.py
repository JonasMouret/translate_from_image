from PIL import Image
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')

translate_again = 'y'

while translate_again == 'y':
  language = input ('Please select your translation language: ')
  image_dir = input ('Enter the dir of the image : ')
  saved_file = input ('Enter the name to save the file: ')

  img = Image.open(image_dir)
  result = pytesseract.image_to_string(img)

  p = Translator()
  # translates the text into your selected language
  k = p.translate(result, dest=language)
  #converts the result into string format
  translated = str(k.text)

  with open(saved_file, mode ='w') as file:
    file.write(translated)
    print("\nTranslation DONE !!!")
  translate_again = input ('Would you like to translate another image ? (y= yes , n = no):')
