import shutil
import os
import argparse
import requests
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def download_content(session, folder, filename, url):
    os.makedirs(folder, exist_ok=True)
    content_path = os.path.join(folder, filename)

    with session.get(url, stream=True) as response:
        response.raise_for_status()
        with open(f"{content_path}", "wb") as f:
            shutil.copyfileobj(response.raw, f)

        logging.info(f"Downloaded picture to {content_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Saves n-number of pictures of random dogs"
    )
    parser.add_argument(
        "-f",
        "--folder",
        help="Folder where dog pictures will be saved",
        type=str,
        default="dogs",
    )

    parser.add_argument(
        "-c",
        "--count",
        help="Specify the number of dog images to download",
        type=int,
        default=50,
    )

    args = parser.parse_args()
    folder = args.folder
    pictures_count = args.count

    if os.path.isdir(folder):
        shutil.rmtree(folder)

    with requests.Session() as session:
        for response_number in range(pictures_count):
            params = {"filter": "mp4,webm"}
            url = "https://random.dog/woof.json"
            try:
                response = session.get(url, params=params)
                response.raise_for_status()
                picture_link = response.json().get("url")
                link, picture_extension = os.path.splitext(picture_link)
                filename = f"dog_{response_number + 1}{picture_extension}"
                download_content(session, folder, filename, picture_link)
            except requests.RequestException as e:
                logging.error(f"Failed to download {url}: {e}")
