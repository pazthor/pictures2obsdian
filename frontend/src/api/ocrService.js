import api from './index';

export const processOCR = async (base64Image) => {
  try {
    console.log('Sending OCR request with base64 length:', base64Image.length);
    console.log('Base64 starts with:', base64Image.substring(0, 50));
    
    const response = await api.post('/ocr/process', {
      base64_image: base64Image
    });
    
    console.log('OCR response status:', response.status);
    console.log('OCR response data:', response.data);
    
    return response.data;
  } catch (error) {
    console.error('OCR processing failed:', error);
    console.error('Error response:', error.response?.data);
    throw new Error(error.response?.data?.message || 'OCR processing failed');
  }
};