import React from 'react';
import { AppProvider, useApp } from './contexts/AppContext';
import ImageDropZone from './components/ImageDropZone';
import MarkdownPane from './components/MarkdownPane';
import MetadataPanel from './components/MetadataPanel';
import LoaderOverlay from './components/LoaderOverlay';
import './App.css';

const AppContent = () => {
  const { state } = useApp();

  const renderCurrentStage = () => {
    switch (state.currentStage) {
      case 'upload':
        return <ImageDropZone />;
      case 'editing':
        return <MarkdownPane />;
      case 'metadata':
        return <MetadataPanel />;
      default:
        return <ImageDropZone />;
    }
  };

  const getLoadingMessage = () => {
    if (state.loading.ocr) return 'Processing image with OCR...';
    if (state.loading.analysis) return 'Analyzing markdown content...';
    if (state.loading.saving) return 'Saving to Obsidian...';
    return 'Loading...';
  };

  const isLoading = state.loading.ocr || state.loading.analysis || state.loading.saving;

  return (
    <div className="App">
      <header className="app-header">
        <h1>Pictures to Obsidian</h1>
        <div className="stage-indicator">
          <div className={`stage ${state.currentStage === 'upload' ? 'active' : state.currentStage !== 'upload' ? 'completed' : ''}`}>
            1. Upload Image
          </div>
          <div className={`stage ${state.currentStage === 'editing' ? 'active' : state.currentStage === 'metadata' ? 'completed' : ''}`}>
            2. Edit Markdown
          </div>
          <div className={`stage ${state.currentStage === 'metadata' ? 'active' : ''}`}>
            3. Configure & Save
          </div>
        </div>
      </header>

      <main className="app-main">
        {renderCurrentStage()}
      </main>

      <LoaderOverlay 
        isVisible={isLoading} 
        message={getLoadingMessage()} 
      />
    </div>
  );
};

function App() {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
}

export default App;
