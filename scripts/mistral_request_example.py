
import requests
import base64
def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None



image_path = r"C:\Users\isaac\PycharmProjects\pictures2obsdian\scripts\mistral_math.png"
base64_image = encode_image(image_path)

# Your base64 encoded image string

# API endpoint
url = "http://localhost:8000/ocr/process"


# Send POST request
response = requests.post("http://localhost:8000/ocr/process", params={"base64_image": base64_image})

print(response.json())

#%%