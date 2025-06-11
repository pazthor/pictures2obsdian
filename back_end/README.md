# Pictures to Obsidian - Backend API

A FastAPI backend service that processes images using OCR, analyzes markdown content with AI, and saves documents to Obsidian vaults.

## Features

- **OCR Processing**: Convert images to markdown text using Mistral AI's vision capabilities
- **Content Analysis**: Extract metadata (title, category, tags) from markdown using OpenAI
- **Obsidian Integration**: Save processed documents directly to your Obsidian vault

## Prerequisites

- Python 3.8+
- Mistral AI API key
- OpenAI API key
- Obsidian vault directory

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd pictures2obsdian
   ```

2. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn python-dotenv mistralai openai pydantic
   ```
   
   Or create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install fastapi uvicorn python-dotenv mistralai openai pydantic
   ```

## Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# Mistral AI API Key (required for OCR processing)
MISTRAL_API_KEY=your_mistral_api_key_here

# OpenAI API Key (required for content analysis)
OPENAI_API_KEY=your_openai_api_key_here
```

## Configuration

### Obsidian Directory

Update the `OBSIDIAN_DIRECTORY` path in `back_end/definitions.py`:

```python
OBSIDIAN_DIRECTORY = r"path/to/your/obsidian/vault"
```

Example:
- Windows: `r"C:\Users\username\Documents\MyVault"`
- macOS/Linux: `"/Users/username/Documents/MyVault"` or `"/home/username/Documents/MyVault"`

## Running the Server

1. **Start the FastAPI server**:
   ```bash
   python back_end/main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn back_end.main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Server will be available at**:
   - API: `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

## API Endpoints

### 1. OCR Processing
- **POST** `/ocr/process`
- **Description**: Convert base64 image to markdown text
- **Request Body**:
  ```json
  {
    "base64_image": "data:image/jpeg;base64,..."
  }
  ```
- **Response**:
  ```json
  {
    "status": 200,
    "message": "",
    "markdown": "# Extracted Text\n\nContent from image...",
    "images": [
      {
        "img_name": "image_001",
        "img_base_64": "..."
      }
    ]
  }
  ```

### 2. Markdown Analysis
- **POST** `/markdown/analyze`
- **Description**: Extract metadata from markdown content
- **Request Body**:
  ```json
  {
    "markdown_text": "# Sample Document\n\nContent here..."
  }
  ```
- **Response**:
  ```json
  {
    "status": 200,
    "message": "",
    "title": "Sample Document",
    "category": "Tutorial",
    "tags": ["tag1", "tag2", "tag3"]
  }
  ```

### 3. Save to Obsidian
- **POST** `/obsidian/save`
- **Description**: Save processed document to Obsidian vault
- **Request Body**:
  ```json
  {
    "markdown_text": "# Document Title\n\nContent...",
    "title": "Document Title",
    "tags": ["tag1", "tag2"],
    "category": "Tutorial",
    "images": [
      {
        "img_name": "image_001",
        "img_base_64": "..."
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "status": 200,
    "message": "Document saved successfully to Obsidian vault"
  }
  ```

## CORS Configuration

The server is configured to accept requests from:
- `http://localhost:3000` (React development server)
- `http://localhost:5173` (Vite development server)

To modify allowed origins, update the `allow_origins` list in `main.py`.

## Getting API Keys

### Mistral AI
1. Visit [Mistral AI Console](https://console.mistral.ai/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key

### OpenAI
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Go to API Keys section
4. Create a new secret key

## Troubleshooting

### Common Issues

1. **Module not found errors**:
   - Ensure all dependencies are installed
   - Check that you're running from the correct directory

2. **API key errors**:
   - Verify your `.env` file exists and contains valid API keys
   - Ensure environment variables are properly loaded

3. **Obsidian save errors**:
   - Check that the `OBSIDIAN_DIRECTORY` path exists and is writable
   - Ensure the path uses the correct format for your operating system

4. **CORS errors**:
   - Verify the frontend is running on an allowed port
   - Update `allow_origins` in `main.py` if needed

### Development Mode

For development with auto-reload:
```bash
uvicorn back_end.main:app --reload --host 0.0.0.0 --port 8000
```
