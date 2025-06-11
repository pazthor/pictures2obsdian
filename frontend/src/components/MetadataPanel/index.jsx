import React, { useState } from 'react';
import { useApp } from '../../contexts/AppContext';
import { saveToObsidian } from '../../api/obsidianService';
import './styles.css';

const MetadataPanel = () => {
  const { state, actions } = useApp();
  const [newTag, setNewTag] = useState('');

  console.log('MetadataPanel state.metadata:', state.metadata);

  const handleTitleChange = (e) => {
    actions.setMetadata({ title: e.target.value });
  };

  const handleCategoryChange = (e) => {
    actions.setMetadata({ category: e.target.value });
  };

  const handleAddTag = () => {
    if (newTag.trim() && !state.metadata.tags.includes(newTag.trim())) {
      actions.setMetadata({ 
        tags: [...state.metadata.tags, newTag.trim()] 
      });
      setNewTag('');
    }
  };

  const handleRemoveTag = (tagToRemove) => {
    actions.setMetadata({ 
      tags: state.metadata.tags.filter(tag => tag !== tagToRemove) 
    });
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleAddTag();
    }
  };

  const handleSaveToObsidian = async () => {
    try {
      actions.setLoading({ saving: true });
      actions.setError(null);

      const saveData = {
        markdownText: state.markdownContent,
        title: state.metadata.title,
        tags: state.metadata.tags,
        category: state.metadata.category,
        images: state.imageData?.ocrImages || []
      };

      await saveToObsidian(saveData);
      
      // Success - reset the app
      alert('Successfully saved to Obsidian!');
      actions.reset();
      
    } catch (error) {
      actions.setError(error.message);
    } finally {
      actions.setLoading({ saving: false });
    }
  };

  const handleBack = () => {
    actions.setStage('editing');
  };

  const handleStartOver = () => {
    actions.reset();
  };

  const isFormValid = state.metadata.title.trim() && state.markdownContent.trim();

  return (
    <div className="metadata-panel">
      <div className="metadata-header">
        <h2>Configure Metadata</h2>
        <div className="header-actions">
          <button onClick={handleBack} className="btn-secondary">
            Back to Editor
          </button>
          <button onClick={handleStartOver} className="btn-outline">
            Start Over
          </button>
        </div>
      </div>

      <div className="metadata-form">
        <div className="form-group">
          <label htmlFor="title">Title *</label>
          <input
            id="title"
            type="text"
            value={state.metadata.title}
            onChange={handleTitleChange}
            placeholder="Enter document title"
            className="form-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="category">Category</label>
          <input
            id="category"
            type="text"
            value={state.metadata.category}
            onChange={handleCategoryChange}
            placeholder="Enter category"
            className="form-input"
          />
        </div>

        <div className="form-group">
          <label>Tags</label>
          <div className="tags-input-container">
            <input
              type="text"
              value={newTag}
              onChange={(e) => setNewTag(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Enter a tag and press Enter"
              className="form-input"
            />
            <button 
              onClick={handleAddTag} 
              className="btn-add-tag"
              disabled={!newTag.trim()}
            >
              Add Tag
            </button>
          </div>
          
          {state.metadata.tags.length > 0 && (
            <div className="tags-container">
              {state.metadata.tags.map((tag, index) => (
                <div key={index} className="tag-chip">
                  <span>{tag}</span>
                  <button
                    onClick={() => handleRemoveTag(tag)}
                    className="tag-remove"
                    aria-label={`Remove ${tag} tag`}
                  >
                    ×
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="form-group">
          <label>Preview</label>
          <div className="preview-container">
            <div className="preview-section">
              <strong>Title:</strong> {state.metadata.title || 'Untitled'}
            </div>
            <div className="preview-section">
              <strong>Category:</strong> {state.metadata.category || 'None'}
            </div>
            <div className="preview-section">
              <strong>Tags:</strong> {state.metadata.tags.length > 0 ? state.metadata.tags.join(', ') : 'None'}
            </div>
            <div className="preview-section">
              <strong>Content Length:</strong> {state.markdownContent.length} characters
            </div>
          </div>
        </div>

        {state.error && (
          <div className="error-message">
            <p>Error: {state.error}</p>
            <button onClick={() => actions.setError(null)}>Dismiss</button>
          </div>
        )}

        <div className="save-section">
          <button
            onClick={handleSaveToObsidian}
            disabled={!isFormValid || state.loading.saving}
            className="btn-save"
          >
            {state.loading.saving ? 'Saving...' : 'Save to Obsidian'}
          </button>
          <p className="save-info">
            * Title is required. This will save your markdown content with the specified metadata to Obsidian.
          </p>
        </div>
      </div>
    </div>
  );
};

export default MetadataPanel;