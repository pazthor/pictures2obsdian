#%%
import base64
import requests

# Read an image and encode it in base64
with open(r"C:\Users\isaac\PycharmProjects\pictures2obsdian\scripts\mistral_math.png", "rb") as img_file:
    base64_str = base64.b64encode(img_file.read()).decode("utf-8")

# Make the request
response = requests.post(
    "http://0.0.0.0:8000/ocr/process",
    json={"base64_image": base64_str}
)

print(response.json())