import React, { createContext, useContext, useReducer } from 'react';

const AppContext = createContext();

const initialState = {
  currentStage: 'upload', // 'upload' | 'editing' | 'metadata'
  imageData: null,
  markdownContent: '',
  metadata: {
    title: '',
    tags: [],
    category: ''
  },
  loading: {
    ocr: false,
    analysis: false,
    saving: false
  },
  error: null
};

const appReducer = (state, action) => {
  switch (action.type) {
    case 'SET_STAGE':
      console.log('Reducer SET_STAGE:', action.payload);
      return { ...state, currentStage: action.payload };
    case 'SET_IMAGE_DATA':
      return { ...state, imageData: action.payload };
    case 'SET_MARKDOWN_CONTENT':
      return { ...state, markdownContent: action.payload };
    case 'SET_METADATA':
      const newMetadata = { ...state.metadata, ...action.payload };
      console.log('Reducer SET_METADATA:', 'current:', state.metadata, 'payload:', action.payload, 'new:', newMetadata);
      return { ...state, metadata: newMetadata };
    case 'SET_LOADING':
      return { ...state, loading: { ...state.loading, ...action.payload } };
    case 'SET_ERROR':
      return { ...state, error: action.payload };
    case 'RESET':
      return initialState;
    default:
      return state;
  }
};

export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  const actions = {
    setStage: (stage) => {
      console.log('Setting stage to:', stage);
      dispatch({ type: 'SET_STAGE', payload: stage });
    },
    setImageData: (imageData) => dispatch({ type: 'SET_IMAGE_DATA', payload: imageData }),
    setMarkdownContent: (content) => dispatch({ type: 'SET_MARKDOWN_CONTENT', payload: content }),
    setMetadata: (metadata) => {
      console.log('Context setMetadata called with:', metadata);
      dispatch({ type: 'SET_METADATA', payload: metadata });
    },
    setLoading: (loading) => dispatch({ type: 'SET_LOADING', payload: loading }),
    setError: (error) => dispatch({ type: 'SET_ERROR', payload: error }),
    reset: () => dispatch({ type: 'RESET' })
  };

  return (
    <AppContext.Provider value={{ state, actions }}>
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};