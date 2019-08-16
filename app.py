import requests, webbrowser, ctypes, urllib.request 
from PIL import Image

# Path for the image
path = "YourPath/unsplash.jpg"

# Access Key for Unsplash API
KEY = "Your key"

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
