import requests, webbrowser, ctypes, urllib.request 
from PIL import Image

# Path for the image
path = "C:/Users/spenc/OneDrive/Desktop/Coding/Python/BackgroundChanger/unsplash.jpg"

# Access Key for Unsplash API
KEY = "e4ac487b825cd5353dc1425b133157b1d56793e436124f4cca58e704ac96629e"

# Call API/jsonify data
response = requests.get("https://api.unsplash.com/photos/random/?client_id=" + KEY).json()
print(response)
# Get the raw image from the call
raw = response['urls']['full']

# Save the image locally
urllib.request.urlretrieve(raw, "unsplash.jpg")
print(raw)

# Change background image with ctypes library, code = 20
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)