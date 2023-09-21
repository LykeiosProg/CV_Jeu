import requests
from PIL import Image
from io import BytesIO

url = "https://i.imgur.com/K4A9jQv.png"

response = requests.get(url)

image = BytesIO(response.content)
