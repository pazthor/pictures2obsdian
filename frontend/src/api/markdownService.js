import api from './index';

export const analyzeMarkdown = async (markdownContent) => {
  try {
    const response = await api.post('/markdown/analyze', {
      markdown_text: markdownContent
    });
    return response.data;
  } catch (error) {
    console.error('Markdown analysis failed:', error);
    throw new Error(error.response?.data?.message || 'Markdown analysis failed');
  }
};