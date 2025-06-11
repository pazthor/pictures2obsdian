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

- `/ocr/process`: Processes an image using OCR and returns the extracted text as Markdown
- `/markdown/analyze`: Analyzes Markdown content to suggest metadata (title, category, tags)
- `/obsidian/save`: Saves the Markdown content and metadata to an Obsidian vault

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

### Prerequisites

- Python 3.8+ for the backend
- Node.js 14+ for the frontend
- An Obsidian vault
- API keys for Mistral AI and OpenAI

### Backend Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pictures2obsdian
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the `back_end` directory
   - Add your API keys and Obsidian vault path:
     ```
     OPENAI_API_KEY=your_openai_api_key
     MISTRAL_API_KEY=your_mistral_api_key
     OBSIDIAN_VAULT_PATH=path_to_your_obsidian_vault
     ```

5. Start the backend server:
   ```
   cd back_end
   python main.py
   ```
   The server will run on `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

## Usage Instructions

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

## Troubleshooting

- **API Key Errors**: Verify that your API keys for Mistral AI and OpenAI are correctly set in the `.env` file.
- **File Size Errors**: Images larger than 5MB will be rejected. Resize your image and try again.
- **Obsidian Path Errors**: Ensure the path to your Obsidian vault is correctly set in the `.env` file.

## Future Improvements

- Support for multiple image uploads
- Progress bar for OCR processing
- Autosave drafts to localStorage
- Diff view between OCR result and edited content
- Support for additional OCR providers