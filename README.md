# Pictures to Obsidian

A full-stack application that allows users to extract text from images using OCR, edit the extracted content in Markdown format, and save it to an Obsidian vault with metadata.

## Project Overview

This application combines OCR (Optical Character Recognition) technology with Markdown editing capabilities to streamline the process of digitizing physical documents and storing them in an organized manner in Obsidian. The workflow is as follows:

1. Upload an image containing text
2. The backend processes the image using OCR (via Mistral AI)
3. The extracted text is returned as Markdown
4. The Markdown content is analyzed to suggest metadata (via OpenAI)
5. The user can edit the content and metadata
6. The final document is saved to an Obsidian vault

## Architecture

### Backend (FastAPI)

The backend is built with FastAPI and provides the following endpoints:

- `/api/ocr/process`: Processes an image using OCR and returns the extracted text as Markdown
- `/api/markdown/analyze`: Analyzes Markdown content to suggest metadata (title, category, tags)
- `/api/obsidian/save`: Saves the Markdown content and metadata to an Obsidian vault

The backend uses:
- Mistral AI for OCR processing
- OpenAI for Markdown analysis
- Custom Obsidian handler for saving to Obsidian vault

### Frontend (React)

The frontend is built with React and Vite and provides a user-friendly interface for:

- Uploading images via drag-and-drop
- Editing the extracted Markdown content
- Editing document metadata (title, category, tags)
- Saving the document to Obsidian

## Setup Instructions

There are two ways to run this application: using Docker (recommended for production) or local development setup.

### Option 1: Docker Setup (Recommended)

#### Prerequisites
- Docker installed on your system
- An Obsidian vault
- API keys for Mistral AI and OpenAI

#### Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd pictures2obsdian
   ```

2. **Create environment file:**
   - Create a `.env` file in the root directory (next to Dockerfile)
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     MISTRAL_API_KEY=your_mistral_api_key
     ```

3. **Create Docker volume for Obsidian vault:**
   ```bash
   # Replace the path with your actual Obsidian vault path
   docker volume create --driver local \
     --opt type=none \
     --opt device="C:\Users\isaac\Documents\Obsidian Vault\OCR" \
     --opt o=bind obsidian-ocr-volume
   ```

4. **Build and run the Docker container:**
   ```bash
   # Build the image
   docker build -t pictures2obsidian .
   
   # Run the container
   docker run -p 8000:8000 -v obsidian-ocr-volume:/app/api_vault pictures2obsidian
   ```

5. **Access the application:**
   - Open `http://localhost:8000` in your browser
   - The application serves both frontend and API from the same port

### Option 2: Local Development Setup

#### Prerequisites
- Python 3.8+ for the backend
- Node.js 14+ for the frontend
- An Obsidian vault
- API keys for Mistral AI and OpenAI

#### Backend Setup

1. **Clone and setup environment:**
   ```bash
   git clone <repository-url>
   cd pictures2obsdian
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

2. **Install dependencies:**
   ```bash
   pip install -r back_end/requirements.txt
   ```

3. **Environment variables:**
   - Create a `.env` file in the `back_end` directory
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     MISTRAL_API_KEY=your_mistral_api_key
     ```

4. **Start the backend:**
   ```bash
   cd back_end
   python main.py
   ```
   Server runs on `http://localhost:8000`

#### Frontend Setup

1. **Setup frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Frontend runs on `http://localhost:5173`

## Usage Instructions

### Accessing the Application

- **Docker**: Navigate to `http://localhost:8000`
- **Local Development**: Navigate to `http://localhost:5173` (frontend) with backend on `http://localhost:8000`

### Using the Application

1. **Upload an Image**:
   - Drag and drop an image onto the upload area, or click to select a file
   - Supported formats: JPEG, PNG, GIF, BMP, WebP
   - Maximum file size: 5MB

2. **Edit Extracted Content**:
   - The extracted text will be displayed in the Markdown editor
   - You can switch between "Write" and "Preview" modes to see how the Markdown will render
   - Make any necessary edits to the content

3. **Edit Document Metadata**:
   - The system will suggest a title, category, and tags based on the content
   - You can edit these suggestions or add your own
   - To add a tag, type it in the input field and press Enter or click "Add"
   - To remove a tag, click the "×" button next to it

4. **Save to Obsidian**:
   - Click the "Save to Obsidian" button to save the document to your Obsidian vault
   - The document will be saved with the specified title, category, and tags
   - Any images in the document will also be saved to the vault

5. **Start Over**:
   - Click the "Clear & Start Over" button to reset the form and start with a new image

## Technologies Used

### Backend
- FastAPI: Web framework for building APIs
- Pydantic: Data validation and settings management
- Mistral AI: OCR processing
- OpenAI: Markdown analysis
- CORS middleware: For handling cross-origin requests

### Frontend
- React: UI library
- Vite: Build tool and development server
- Axios: HTTP client for API requests
- React Dropzone: Drag-and-drop file upload
- React MDE: Markdown editor component
- React Spinners: Loading indicators
- Showdown: Markdown to HTML conversion

## Features

- Drag-and-drop image upload
- OCR processing of images
- Markdown editing with live preview
- Automatic metadata suggestion
- Tag management (add/remove)
- Saving to Obsidian vault
- Error handling and validation
- Responsive design
- **Single-container deployment** (frontend + backend)
- **Embedded environment variables** (no need to pass API keys at runtime)

## Docker Commands Reference

### Create Obsidian Volume
```bash
# Windows path example - replace with your actual Obsidian vault path
docker volume create --driver local \
  --opt type=none \
  --opt device="C:\Users\isaac\Documents\Obsidian Vault\OCR" \
  --opt o=bind obsidian-ocr-volume

# Linux/macOS path example
docker volume create --driver local \
  --opt type=none \
  --opt device="/path/to/your/obsidian/vault" \
  --opt o=bind obsidian-ocr-volume
```

### Build and Run Container
```bash
# Build the image
docker build -t pictures2obsidian .

# Run the container
docker run -p 8000:8000 -v obsidian-ocr-volume:/app/api_vault pictures2obsidian

```

## Troubleshooting

### Docker Issues
- **Build Errors**: Ensure `.env` file exists in root directory with API keys
- **Volume Mount Issues**: Verify your Obsidian vault path is correct when creating the volume
- **Port Conflicts**: Change `-p 8001:8000` if port 8000 is already in use

### API Issues
- **API Key Errors**: Verify API keys in `.env` file are correct and valid
- **File Size Errors**: Images larger than 5MB will be rejected
- **Network Errors**: Ensure API endpoints use `/api/` prefix

### Development Issues
- **CORS Errors**: In development mode, frontend (port 5173) and backend (port 8000) run separately
- **Static Files**: Frontend is only served by backend in production/Docker mode

## Future Improvements

- Support for multiple image uploads
- Rich text for the markdown content
- Support for MistralAI in /api/ocr/process