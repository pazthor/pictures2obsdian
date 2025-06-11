import React, { useEffect, useRef } from 'react';
import MDEditor from '@uiw/react-md-editor';
import { useApp } from '../../contexts/AppContext';
import { analyzeMarkdown } from '../../api/markdownService';
import './styles.css';

const MarkdownPane = () => {
  const { state, actions } = useApp();
  const hasAnalyzed = useRef(false);

  useEffect(() => {
    if (state.markdownContent && !state.loading.analysis && !hasAnalyzed.current) {
      const analyzeContent = async () => {
        try {
          hasAnalyzed.current = true;
          actions.setLoading({ analysis: true });
          const result = await analyzeMarkdown(state.markdownContent);
          
          console.log('Analyze result:', result);
          const metadata = {
            title: result.title || '',
            tags: result.tags || [],
            category: result.category || ''
          };
          console.log('Setting metadata:', metadata);
          actions.setMetadata(metadata);
        } catch (error) {
          console.error('Failed to analyze markdown:', error);
          actions.setError('Failed to analyze markdown content');
          hasAnalyzed.current = false; // Reset on error so user can retry
        } finally {
          actions.setLoading({ analysis: false });
        }
      };

      analyzeContent();
    }
  }, [state.markdownContent]);

  const handleMarkdownChange = (value) => {
    actions.setMarkdownContent(value || '');
    // Reset analysis flag when user manually changes content
    hasAnalyzed.current = false;
  };

  const handleNext = () => {
    actions.setStage('metadata');
  };

  const handleBack = () => {
    actions.setStage('upload');
    actions.setMarkdownContent('');
    actions.setImageData(null);
    actions.setMetadata({ title: '', tags: [], category: '' });
  };

  return (
    <div className="markdown-pane">
      <div className="markdown-header">
        <h2>Edit Markdown Content</h2>
        <div className="header-actions">
          <button onClick={handleBack} className="btn-secondary">
            Back to Upload
          </button>
          <button 
            onClick={handleNext} 
            className="btn-primary"
            disabled={!state.markdownContent.trim()}
          >
            Continue to Metadata
          </button>
        </div>
      </div>

      {state.loading.analysis && (
        <div className="analysis-loading">
          <div className="loading-spinner"></div>
          <span>Analyzing content...</span>
        </div>
      )}

      <div className="editor-container">
        <MDEditor
          value={state.markdownContent}
          onChange={handleMarkdownChange}
          height={500}
          preview="edit"
          hideToolbar={false}
          data-color-mode="light"
        />
      </div>

      {state.imageData && (
        <div className="source-image">
          <h3>Source Image:</h3>
          <img 
            src={state.imageData.preview} 
            alt="Source" 
            className="source-preview"
          />
        </div>
      )}
    </div>
  );
};

export default MarkdownPane;