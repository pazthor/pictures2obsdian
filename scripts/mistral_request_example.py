#%%
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
    except Exception as e:
        print(f"Error: {e}")
        return None


image_path = r"C:\Users\isaac\PycharmProjects\pictures2obsdian\scripts\mistral_math.png"
base64_image = encode_image(image_path)

# API endpoint
url = "http://localhost:8000/api/ocr/process"

# Send POST request with JSON body instead of query parameters
response = requests.post(
    url,
    json={"base64_image": base64_image}  # Send as JSON body instead of query parameters
)
print(response.json())
#%%
# import os
result=response.json()
#
# OBSIDIAN_DIRECTORY=r"C:\Users\isaac\Documents\api_vault\examples"
#
#
# class ObsidianHandler:
#     def __init__(self):
#         self.directory = OBSIDIAN_DIRECTORY
#
#     def remove_base64_header(self,base64_string):
#         if base64_string.startswith("data:image"):
#             base64_string = base64_string.split(",")[1]
#         return base64_string
#
#     def write_file_2obsidian(self,
#                              markdown_text: str,
#                              tittle: str,
#                              tags: list[str],
#                              category: str,
#                              images: list[dict[str, str]]
#                              ):
#
#         snake_case_category = category.lower().replace(" ", "_")
#
#         category_dict = os.path.join(self.directory, snake_case_category)
#
#         if not os.path.exists(category_dict):
#             os.makedirs(category_dict)
#
#         snake_case_tittle = tittle.lower().replace(" ", "_")
#
#         reformated_images = [{"original_name": image["img_name"],
#                               "new_name": snake_case_tittle + image["img_name"],
#                               "base_64": self.remove_base64_header(image["img_base_64"]),
#                               } for image in images]
#         for image in reformated_images:
#             with open(os.path.join(category_dict, image["new_name"]), "wb") as f:
#                 f.write(base64.b64decode(image["base_64"]))
#             markdown_text = markdown_text.replace(image["original_name"], image["new_name"])
#
#         # We add the tags at the beggininf of the document
#         formated_tags = " ".join(["#" + x.strip() for x in tags])
#         markdown_doc = f"{formated_tags}\n\n{markdown_text}"
#         # save the doc to the tittle
#         with open(os.path.join(category_dict, (tittle+".md")), "w") as f:
#             f.write(markdown_doc)
#
#
# Obsidian().write_file_2obsidian(result["markdown"],"test",["tag1","tag2","tag3"],"Tutorial",result["images"])

obsidian_url = "http://localhost:8000/obsidian/save"

# Create request payload
obsidian_payload = {
    "markdown_text": result["markdown"],
    "title": "test",
    "tags": ["tag1","tag2","tag3"],
    "category": "Tutorial",
    "images": result["images"]
}

# Send POST request to save to Obsidian
obsidian_response = requests.post(
    obsidian_url,
    json=obsidian_payload
)
#%%