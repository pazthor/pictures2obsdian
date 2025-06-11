# Pictures to Obsidian - Frontend

A React-based web application that provides an intuitive interface for processing images with OCR, editing markdown content, and saving documents to Obsidian vaults.

## Features

- **Drag & Drop Image Upload**: Easy image upload with visual feedback
- **OCR Processing**: Convert images to editable markdown text
- **Markdown Editor**: Rich markdown editor with live preview
- **Metadata Management**: AI-powered content analysis with editable metadata
- **Obsidian Integration**: Direct saving to your Obsidian vault
- **Responsive Design**: Works on desktop and mobile devices

## Prerequisites

- Node.js 16+ and npm
- Running backend API server (see backend README)

## Installation

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

## Environment Variables

Create a `.env` file in the `frontend` directory:

```env
# Backend API URL
REACT_APP_API_BASE_URL=http://localhost:8000
```

### Environment Variables Reference

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `REACT_APP_API_BASE_URL` | Backend API server URL | `http://localhost:8000` | No |

**Note**: Environment variables in React must be prefixed with `REACT_APP_` to be accessible in the browser.

## Available Scripts

### `npm start`
Runs the app in development mode.
- Open [http://localhost:3000](http://localhost:3000) to view it in the browser
- The page will reload when you make changes
- You may also see any lint errors in the console

### `npm test`
Launches the test runner in interactive watch mode.

### `npm run build`
Builds the app for production to the `build` folder.
- It correctly bundles React in production mode and optimizes the build for best performance
- The build is minified and the filenames include the hashes
- Your app is ready to be deployed!

### `npm run eject`
**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time.

## Usage

### 1. Start the Application

Make sure your backend server is running, then:

```bash
npm start
```

The application will open at `http://localhost:3000`.

### 2. Upload and Process Images

1. **Upload**: Drag and drop an image onto the upload zone or click to select a file
2. **OCR Processing**: The image will be automatically processed and converted to markdown
3. **Edit**: Review and edit the extracted markdown content in the editor
4. **Metadata**: Configure title, category, and tags (AI suggestions will be provided)
5. **Save**: Save the processed document to your Obsidian vault

### 3. Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)

## Project Structure

```
frontend/
├── public/                 # Static files
├── src/
│   ├── api/               # API service functions
│   │   ├── index.js       # Axios configuration
│   │   ├── ocrService.js  # OCR API calls
│   │   ├── markdownService.js # Markdown analysis
│   │   └── obsidianService.js # Obsidian save
│   ├── components/        # React components
│   │   ├── ImageDropZone/ # Image upload component
│   │   ├── MarkdownPane/  # Markdown editor
│   │   ├── MetadataPanel/ # Metadata configuration
│   │   └── LoaderOverlay/ # Loading indicators
│   ├── contexts/          # React Context for state management
│   │   └── AppContext.jsx # Global application state
│   ├── App.js            # Main application component
│   ├── App.css           # Main styles
│   └── index.js          # Application entry point
├── package.json          # Dependencies and scripts
└── README.md            # This file
```

## Application Flow

1. **Upload Stage**: User uploads an image via drag-and-drop
2. **Processing Stage**: Image is sent to backend for OCR processing
3. **Editing Stage**: User reviews and edits the extracted markdown
4. **Analysis Stage**: Content is analyzed for metadata extraction
5. **Metadata Stage**: User configures title, category, and tags
6. **Save Stage**: Document is saved to Obsidian vault

## Dependencies

### Core Dependencies
- **React 19**: UI framework
- **React DOM**: React rendering
- **Axios**: HTTP client for API requests

### UI Components
- **@uiw/react-md-editor**: Markdown editor with preview
- **react-dropzone**: Drag-and-drop file upload
- **react-markdown**: Markdown rendering

### Development Dependencies
- **react-scripts**: Build tools and development server
- **@testing-library**: Testing utilities

## Configuration

### API Integration

The frontend communicates with three main backend endpoints:

1. **POST /ocr/process**: Image to markdown conversion
2. **POST /markdown/analyze**: Content metadata extraction
3. **POST /obsidian/save**: Save to Obsidian vault

### Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- Invalid file formats
- API server errors
- Processing timeouts

## Troubleshooting

### Common Issues

1. **Backend Connection Errors**:
   - Ensure the backend server is running on the correct port
   - Verify `REACT_APP_API_BASE_URL` in your `.env` file
   - Check for CORS issues in browser console

2. **Image Upload Issues**:
   - Verify the image format is supported
   - Check file size (very large images may timeout)
   - Ensure stable internet connection

3. **Build Errors**:
   - Delete `node_modules` and run `npm install` again
   - Clear npm cache: `npm cache clean --force`
   - Check Node.js version compatibility

4. **Environment Variables Not Loading**:
   - Ensure `.env` file is in the `frontend` directory
   - Restart the development server after adding variables
   - Variables must be prefixed with `REACT_APP_`

### Development Tips

- Use browser developer tools to monitor network requests
- Check console for error messages and debugging information
- Use React Developer Tools browser extension for component debugging

## Production Deployment

1. **Build the application**:
   ```bash
   npm run build
   ```

2. **Deploy the `build` folder** to your web server or hosting platform

3. **Update environment variables** for production:
   ```env
   REACT_APP_API_BASE_URL=https://your-api-domain.com
   ```

