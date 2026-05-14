import React, { useState, useEffect } from 'react';
import { getExamples } from '../api/client';
import { Play, FileText, Loader2 } from 'lucide-react';

interface Props {
  onAnalyze: (text: string) => void;
  loading: boolean;
}

export default function RequirementInput({ onAnalyze, loading }: Props) {
  const [text, setText] = useState('');
  const [examples, setExamples] = useState<string[]>([]);

  useEffect(() => {
    getExamples().then(res => setExamples(res.examples)).catch(console.error);
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
      <div className="flex items-center space-x-2 mb-4">
        <FileText size={18} className="text-blue-600" />
        <h2 className="font-semibold text-slate-800">需求输入</h2>
      </div>
      
      <textarea
        className="w-full h-32 p-3 border border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none resize-none transition-all"
        placeholder="请输入原始产品需求..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        disabled={loading}
      />
      
      <div className="mt-4 flex flex-col sm:flex-row gap-3">
        <button
          onClick={() => {
            if (examples.length > 0) {
              setText(examples[Math.floor(Math.random() * examples.length)]);
            }
          }}
          disabled={loading || examples.length === 0}
          className="text-sm px-4 py-2 text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-lg transition-colors flex-1"
        >
          随机示例
        </button>
        <button
          onClick={() => text.trim() && onAnalyze(text)}
          disabled={loading || !text.trim()}
          className="text-sm px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center flex-[2]"
        >
          {loading ? (
            <>
              <Loader2 size={16} className="animate-spin mr-2" />
              分析中...
            </>
          ) : (
            <>
              <Play size={16} className="mr-2" />
              开始智能分析
            </>
          )}
        </button>
      </div>
    </div>
  );
}
