from io import BytesIO
import os
import typer
import requests
from datetime import datetime
from config import BASE_URL, API_KEY, IMAGE_DIR
from PIL import Image

app = typer.Typer()


@app.callback()
def main():
    """
    CLI tool to fetch NASA's Astronomy Picture of the Day (APOD) for a given date.
    """
    pass


# Set the default date (today)
DEFAULT_DATE = datetime.now().strftime("%Y-%m-%d")


@app.command()
def fetch_image(
    date: datetime = typer.Argument(DEFAULT_DATE, formats=["%Y-%m-%d"]),
    save: bool = typer.Option(
        False, "--save", help="Save the photo to the images folder"
    ),
):
    print(f"Sending request to NASA API for date: {date.date()}...")
    dt = str(date.date())

    # 1. Build request parameters as a dictionary
    params = {"api_key": API_KEY, "date": date.strftime("%Y-%m-%d")}

    try:
        # requests will automatically build the correct URL from BASE_URL and params
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Check: if the result for this date is a video instead of an image
        if data.get("media_type") != "image":
            print(
                f"For this date ({data.get('date')}) a video is available instead of a photo."
            )
            print(f"Video link: {data.get('url')}")
            return

        url = data["url"]
        title = data["title"]

        print(f"Found: '{title}'")
        print("Downloading image...")

        img_res = requests.get(url)
        img_res.raise_for_status()

        # Open the image using PIL
        image = Image.open(BytesIO(img_res.content))
        image.show()

        # 2. Saving logic
        if save:
            # Create the directory if it doesn't exist (Pathlib will handle this)
            IMAGE_DIR.mkdir(parents=True, exist_ok=True)

            # Clean the title by removing forbidden Windows characters
            clean_title = "".join(
                c for c in title if c.isalnum() or c in (" ", "-", "_")
            ).strip()
            extension = image.format.lower() if image.format else "jpg"
            file_path = IMAGE_DIR / f"{clean_title}.{extension}"

            image.save(file_path)
            print(f"Saved: {file_path}")

        image.close()

    except requests.exceptions.HTTPError as err:
        print(f"API Error: {err}")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    app()
