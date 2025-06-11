import api from './index';

export const saveToObsidian = async (data) => {
  try {
    const response = await api.post('/obsidian/save', {
      markdown_text: data.markdownText,
      title: data.title,
      tags: data.tags,
      category: data.category,
      images: data.images
    });
    return response.data;
  } catch (error) {
    console.error('Obsidian save failed:', error);
    throw new Error(error.response?.data?.message || 'Failed to save to Obsidian');
  }
};