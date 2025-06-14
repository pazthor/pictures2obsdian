from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import io
from pydantic import BaseModel,Field
from typing import List, Optional

from back_end.models.mistral_api import MistralApiHandler
from back_end.models.openai_api import OpenAIHandler
from back_end.models.obsidian import ObsidianHandler

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

class DocumentMetadata(BaseModel):
    Document_tittle: str
    document_type: str
    Tags: List[str]

class MarkdownRequest(BaseModel):
    markdown_text: str = Field(..., description="Markdown text to be analyzed")

class MarkdownResponse(BaseModel):
    status: int = Field(..., description="HTTP status code", example=200)
    message: str = Field(..., description="Error message if any", example="")
    title: str = Field(..., description="Extracted document title", example="Sample Title")
    category: str = Field(..., description="Document category/type", example="Tutorial")
    tags: List[str] = Field(..., description="Extracted tags", example=["tag1", "tag2"])

    class Config:
        json_schema_extra = {
            "example": {
                "status": 200,
                "message": "",
                "title": "Getting Started with PyTorch",
                "category": "Tutorial", 
                "tags": ["PyTorch", "Deep Learning", "Machine Learning"]
            }
        }


class ObsidianRequest(BaseModel):
    markdown_text: str = Field(..., description="Markdown text to be saved to Obsidian")
    title: str = Field(..., description="Title of the document")
    tags: List[str] = Field(..., description="List of tags for the document")
    category: str = Field(..., description="Category for document organization")
    images: List[dict[str,str]] = Field(default=[], description="List of images with base64 data")


class ObsidianResponse(BaseModel):
    status: int = Field(..., description="HTTP status code", example=200)
    message: str = Field(..., description="Success or error message", example="Document saved successfully")

    class Config:
        json_schema_extra = {
            "example": {
                "status": 200,
                "message": "Document saved successfully to Obsidian vault"
            }
        }


app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React and Vite dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class ImageRequest(BaseModel):
    image_data: str  # Base64 encoded image string
class OCRRequest(BaseModel):
    base64_image: str

@app.post("/ocr/process", response_model=OCRResponseDetailed)
async def process_ocr(request: OCRRequest):
    try:
        result = MistralApiHandler().base64_to_markdown(request.base64_image)
        return result
    except Exception as e:
        print("Error during OCR processing:", e)
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/markdown/analyze", response_model=MarkdownResponse)
async def analyze_markdown(request: MarkdownRequest):
    try:
        result = OpenAIHandler().process_markdown(request.markdown_text)
        
        # Extract the content object from the response
        content = result.get("content", {})
        print(content)
        # Map the response to match the new MarkdownResponse structure
        return {
            "status": result.get("status", 200),
            "message": result.get("message", ""),
            "title": content.get("document_tittle", ""),
            "category": content.get("document_type", ""),
            "tags": content.get("tags", [])
        }
    except Exception as e:
        print("Error during markdown processing:", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Hi"}


@app.post("/obsidian/save", response_model=ObsidianResponse)
async def save_to_obsidian(request: ObsidianRequest):
    try:
        ObsidianHandler().write_file_2obsidian(
            markdown_text=request.markdown_text,
            tittle=request.title,  # Note: using 'tittle' as that's what the class expects
            tags=request.tags,
            category=request.category,
            images=request.images
        )

        return {
            "status": 200,
            "message": f"Document '{request.title}' saved successfully to Obsidian vault"
        }
    except Exception as e:
        print(f"Error saving to Obsidian: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
