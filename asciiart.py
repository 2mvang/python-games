# asciiart.py
import requests
import random
def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)

# data = requests.get('http://artii.herokuapp.com/fonts_list')
# print(data)
# fontsArray = data.text.split('\n')

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

### Be weary of control flow order and Boolean Logic

if font == "random":
  data = requests.get('http://artii.herokuapp.com/fonts_list')
  fontsArray = data.text.split('\n')

  for i in range(3):
      font = random.choice(fontsArray)
      getAsciiArt(text, font)

elif font:
  font = font
  getAsciiArt(text, font)

elif font == "":
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
  print("Font: default")
  print(r.text)



# r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
# print(r.text)