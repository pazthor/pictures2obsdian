import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { useApp } from '../../contexts/AppContext';
import { processOCR } from '../../api/ocrService';
import './styles.css';

const ImageDropZone = () => {
  const { state, actions } = useApp();

  const convertToBase64 = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = error => reject(error);
    });
  };

  const onDrop = useCallback(async (acceptedFiles) => {
    if (acceptedFiles.length === 0) return;

    const file = acceptedFiles[0];
    
    try {
      actions.setLoading({ ocr: true });
      actions.setError(null);

      const base64 = await convertToBase64(file);
      actions.setImageData({
        file,
        base64,
        preview: URL.createObjectURL(file)
      });

      const ocrResult = await processOCR(base64);
      actions.setMarkdownContent(ocrResult.markdown || ocrResult.text || '');
      
      // Store the images from OCR response for later use in Obsidian save
      if (ocrResult.images && ocrResult.images.length > 0) {
        actions.setImageData({
          file,
          base64,
          preview: URL.createObjectURL(file),
          ocrImages: ocrResult.images // Store the properly formatted images
        });
      }
      
      actions.setStage('editing');

    } catch (error) {
      actions.setError(error.message);
    } finally {
      actions.setLoading({ ocr: false });
    }
  }, [actions]);

  const {
    getRootProps,
    getInputProps,
    isDragActive,
    isDragReject
  } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.webp']
    },
    maxFiles: 1,
    multiple: false
  });

  return (
    <div className="dropzone-container">
      <div
        {...getRootProps()}
        className={`dropzone ${isDragActive ? 'drag-active' : ''} ${isDragReject ? 'drag-reject' : ''}`}
      >
        <input {...getInputProps()} />
        <div className="dropzone-content">
          {isDragActive ? (
            <p>Drop the image here...</p>
          ) : (
            <>
              <div className="upload-icon">📁</div>
              <p>Drag and drop an image here, or click to select</p>
              <small>Supported formats: JPEG, PNG, GIF, BMP, WebP</small>
            </>
          )}
        </div>
      </div>
      
      {state.imageData && (
        <div className="image-preview">
          <img 
            src={state.imageData.preview} 
            alt="Uploaded" 
            className="preview-image"
          />
          <p className="image-name">{state.imageData.file?.name}</p>
        </div>
      )}
      
      {state.error && (
        <div className="error-message">
          <p>Error: {state.error}</p>
          <button onClick={() => actions.setError(null)}>Dismiss</button>
        </div>
      )}
    </div>
  );
};

export default ImageDropZone;