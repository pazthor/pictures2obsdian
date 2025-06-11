from typing import Union

from back_end.definitions import MISTRAL_API_KEY
from mistralai import Mistral


class MistralApiHandler:
    def __init__(self):
        self.client=Mistral(api_key=MISTRAL_API_KEY)

    def remove_base64_header(self,base64_string):
        if base64_string.startswith("data:image"):
            base64_string = base64_string.split(",")[1]
        return base64_string

    def base64_to_markdown(self,base64_img)->dict[str:Union[int,str,list]]:

        try:
            ocr_response = self.client.ocr.process(
                model="mistral-ocr-latest",
                document={
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{self.remove_base64_header(base64_img)}"
                },
                include_image_base64=True
            )
        except Exception as e:
            return {"status":e.status_code,
                    "message":e.message,
                    "markdown":"",
                    "images":[]}

        markdowm_text = ocr_response.pages[0].markdown
        images= [
            {"img_name":image.id,
             "img_base_64":image.image_base64}
            for image in ocr_response.pages[0].images]


        if markdowm_text==".":
            return {"status":200,
                    "message":"",
                    "markdown":"",
                    "images":[]}
        return { "status":200,
                 "message":"",
                    "markdown":markdowm_text,
                    "images":images
        }


