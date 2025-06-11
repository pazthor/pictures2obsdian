import api from './index';

export const processOCR = async (base64Image) => {
  try {
    const response = await api.post('/ocr/process', {
      base64_image: base64Image
    });
    return response.data;
  } catch (error) {
    console.error('OCR processing failed:', error);
    throw new Error(error.response?.data?.message || 'OCR processing failed');
  }
};