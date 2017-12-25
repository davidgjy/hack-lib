import pytesseract
from PIL import Image
image = Image.open('/Users/kg/develop/MyGit/hack-lib/Python/Captcha/captcha.jpg')
vcode = pytesseract.image_to_string(image)
print (vcode)