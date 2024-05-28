import shutil
import os
import argparse
import requests

def get_response(url, params):
	response = requests.get(url, params)
	response.raise_for_status()
	print(response.url)
	return response.json()


def download_content(folder, filename, url):
	os.makedirs(folder, exist_ok=True)
	content_path = os.path.join(folder, filename)
	picture_bytes = requests.get(picture_link).content
	with open(f"{content_path}", "wb") as f:
		f.write(picture_bytes)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Saves n-number of pictures of random dogs")
	parser.add_argument(
		'-f', 
		'--folder',
		help="Folder where dog pictures will be saved",
		type=str,
		default="dogs"
	)

	parser.add_argument(
		'-c', 
		'--count',
		help="Specify the number of dog images to download",
		type=int,
		default=50
	)

	args = parser.parse_args()
	folder = args.folder
	pictures_count = args.count

	if os.path.isdir(folder):
		shutil.rmtree(folder)

	for response in range(pictures_count):
		params = {"filter": "mp4,webm"}
		picture_link = get_response("https://random.dog/woof.json", params).get('url')
		link, picture_extension = os.path.splitext(picture_link)
		filename = f"dog_{response + 1}{picture_extension}"
		download_content(folder, filename, picture_link)
