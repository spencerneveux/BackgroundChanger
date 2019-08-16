import requests, urllib, random

class Unsplash:

	def __init__(self):
		self.path = "YourPath/unsplash.jpg"
		self.KEY = "YourKey"

	def get_random_image(self):
		response = requests.get("https://api.unsplash.com/photos/random/?client_id=" + self.KEY).json()
		return response["urls"]["full"]

	def get_photo(self, term):
		random_image = random.randint(0, 5)
		response = requests.get("https://api.unsplash.com/search/photos/?page=1&query=" + term + "&client_id=" + self.KEY).json()
		return response["results"][random_image]["urls"]["full"]

	def get_photo_urls(self, term):
		random_image = random.randint(0, 5)
		response = requests.get("https://api.unsplash.com/search/photos/?page=1&query=" + term + "&client_id=" + self.KEY).json()
		return response["results"][random_image]["urls"]

	def get_collection(self, collection):
		random_image = random.randint(0, 5)
		response = requests.get("https://api.unsplash.com/search/photos/?page=1&query=" + collection + "&client_id=" + self.KEY).json()
		return response["results"][random_image]["urls"]["full"]

def main():
	u = Unsplash()
	random_image = u.get_random_image()

if __name__ == '__main__':
	main()
