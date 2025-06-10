from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import io
from pydantic import BaseModel,Field
from typing import List, Optional

from back_end.models.mistral_api import MistralApiHandler
class ImageData(BaseModel):
    img_name: str
    img_base_64: str


class OCRResponse(BaseModel):
    status: int
    message: str
    markdown: str
    images: List[ImageData]
class OCRResponseDetailed(BaseModel):
    """Response model for OCR processing endpoint"""
    status: int = Field(..., description="HTTP status code", example=200)
    message: str = Field(..., description="Error message if any", example="")
    markdown: str = Field(..., description="Extracted markdown text from the image", example="# Sample Text\nThis is extracted content...")
    images: List[ImageData] = Field(..., description="List of extracted images with base64 data")

    class Config:
        json_schema_extra = {
            "example": {
                "status": 200,
                "message": "",
                "markdown": "# Document Title\n\nSome extracted text content...",
                "images": [
                    {
                        "img_name": "image_001",
                        "img_base_64": "dsaasddafwafa"
                    }
                ]
            }
        }



app = FastAPI()



class ImageRequest(BaseModel):
    image_data: str  # Base64 encoded image string
class OCRRequest(BaseModel):
    base64_image: str

@app.post("/ocr/process", response_model=OCRResponse)
async def process_ocr(request: OCRRequest):
    try:
        result = MistralApiHandler().base64_to_markdown(request.base64_image)
        return result
    except Exception as e:
        print("Error during OCR processing:", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Hi"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)