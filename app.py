import requests, ctypes, urllib.request 
from PIL import Image
from unsplash import Unsplash

# Path for the image
path = "YourPath/unsplash.jpg"

# Instantiate Unsplash Object
u = Unsplash()

# Photo
photo = ""

# Method to change the desktop image
def change_desktop(photo):
	# save image locally 
	urllib.request.urlretrieve(photo, "unsplash.jpg")
	print(photo)

	# Change background image with ctypes library, code = 20
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

# -------------------
# Menu
# -------------------
def menu():
	print("Welcome!\nLet's change your background")
	print("1) Random Photo\n2) Search by term\n3) Search by collection\n4) Exit")

# -------------------
# Main
# -------------------
def main():
	flag = True
	while (flag):
		menu()
		user_input = input()
		if user_input == "1":
			photo = u.get_random_image()
			change_desktop(photo)
		elif user_input == "2":
			search_term = input("Search term: ")
			photo = u.get_photo(search_term)
			change_desktop(photo)
		elif user_input == "3":
			collection = input("Collection name: ")
			photo = u.get_collection(collection)
			change_desktop(photo)
		elif user_input == "4":
			flag = False
			print("Exiting")

if __name__ == '__main__':
	main()
