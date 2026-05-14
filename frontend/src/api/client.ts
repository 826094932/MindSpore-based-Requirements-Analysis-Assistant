import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const apiClient = axios.create({
  baseURL: API_BASE_URL
});

export interface AnalyzeRequest {
  requirement_text: string;
}

export interface RiskItem {
  word: string;
  reason: string;
  severity: string;
}

export interface RadarData {
  subject: string;
  A: number;
  fullMark: number;
}

export interface AnalyzeResponse {
  audit: {
    score: number;
    risks: RiskItem[];
    radar_data: RadarData[];
  };
  mindspore: {
    category: string;
    confidence: number;
    is_fallback: boolean;
  };
  rag: {
    retrieved_examples: Array<{ original: string; gwt: string; quality_score: number }>;
  };
  gwt: {
    given: string;
    when: string;
    then: string;
    improved_requirement: string;
    source: string;
  };
}

export const analyzeRequirement = async (text: string): Promise<AnalyzeResponse> => {
  const response = await apiClient.post('/analyze', { requirement_text: text });
  return response.data;
};

export const getExamples = async (): Promise<{ examples: string[] }> => {
  const response = await apiClient.get('/examples');
  return response.data;
};
