from definitions import OBSIDIAN_DIRECTORY
import os
import base64

class ObsidianHandler:
    def __init__(self):
        self.directory = OBSIDIAN_DIRECTORY

    def remove_base64_header(self,base64_string):
        if base64_string.startswith("data:image"):
            base64_string = base64_string.split(",")[1]
        return base64_string

    def write_file_2obsidian(self,
                             markdown_text: str,
                             tittle: str,
                             tags: list[str],
                             category: str,
                             images: list[dict[str, str]]
                             ):

        snake_case_category = category.lower().replace(" ", "_")

        category_dict = os.path.join(self.directory, snake_case_category)

        if not os.path.exists(category_dict):
            os.makedirs(category_dict)

        snake_case_tittle = tittle.lower().replace(" ", "_")

        reformated_images = [{"original_name": image["img_name"],
                              "new_name": snake_case_tittle + image["img_name"],
                              "base_64": self.remove_base64_header(image["img_base_64"]),
                              } for image in images]
        for image in reformated_images:
            with open(os.path.join(category_dict, image["new_name"]), "wb") as f:
                f.write(base64.b64decode(image["base_64"]))
            markdown_text = markdown_text.replace(image["original_name"], image["new_name"])

        # We add the tags at the beggininf of the document
        formated_tags = " ".join(["#" + x.strip() for x in tags])
        markdown_doc = f"{formated_tags}\n\n{markdown_text}"
        # save the doc to the tittle
        with open(os.path.join(category_dict, (tittle+".md")), "w") as f:
            f.write(markdown_doc)
