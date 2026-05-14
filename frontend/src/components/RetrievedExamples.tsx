import React from 'react';
import { Database, ThumbsUp } from 'lucide-react';

interface Example {
  original: string;
  gwt: string;
  quality_score: number;
}

export default function RetrievedExamples({ examples }: { examples: Example[] }) {
  if (!examples || examples.length === 0) return null;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
      <div className="flex items-center space-x-2 mb-4">
        <Database size={18} className="text-blue-600" />
        <h2 className="font-semibold text-slate-800">RAG 历史相似优质需求 (Top {examples.length})</h2>
      </div>
      
      <div className="space-y-4">
        {examples.map((example, idx) => (
          <div key={idx} className="p-4 border border-slate-100 bg-slate-50 rounded-lg">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-medium bg-blue-100 text-blue-800 px-2 py-1 rounded">
                示例 #{idx + 1}
              </span>
              <div className="flex items-center text-xs text-green-600 font-medium">
                <ThumbsUp size={12} className="mr-1" />
                综合得分: {example.quality_score}
              </div>
            </div>
            <p className="text-sm text-slate-700 mb-2 font-medium">{example.original}</p>
            <div className="text-xs text-slate-500 bg-white p-2 rounded border border-slate-200 whitespace-pre-wrap">
              {example.gwt}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
