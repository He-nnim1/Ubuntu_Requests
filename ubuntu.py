import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Ask user for image URL
    url = input("Please enter the image URL: ")
    
    try:
        # Make folder if it does not exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Download image
        response = requests.get(url, timeout=10)
        response.raise_for_status()   # check if the request was ok

        # Get filename from url
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, give it a default one
        if filename == "":
            filename = "downloaded_image.jpg"

        # Full path to save
        filepath = os.path.join("Fetched_Images", filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
