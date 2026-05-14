import React from 'react';
import { Cpu, AlertTriangle } from 'lucide-react';

interface Props {
  data: {
    category: string;
    confidence: number;
    is_fallback: boolean;
  };
}

export default function MindSporePanel({ data }: Props) {
  const categoryColors: Record<string, string> = {
    clear: 'bg-green-100 text-green-800 border-green-200',
    ambiguous: 'bg-yellow-100 text-yellow-800 border-yellow-200',
    incomplete: 'bg-orange-100 text-orange-800 border-orange-200',
    untestable: 'bg-red-100 text-red-800 border-red-200',
  };

  const categoryNames: Record<string, string> = {
    clear: '清晰 (Clear)',
    ambiguous: '模糊 (Ambiguous)',
    incomplete: '不完整 (Incomplete)',
    untestable: '不可测 (Untestable)',
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-2">
          <Cpu size={18} className="text-purple-600" />
          <h2 className="font-semibold text-slate-800">MindSpore 意图分类</h2>
        </div>
        {data.is_fallback && (
          <span className="text-xs bg-slate-100 text-slate-500 px-2 py-1 rounded flex items-center">
            <AlertTriangle size={12} className="mr-1" />
            降级规则模式
          </span>
        )}
      </div>

      <div className="flex items-center justify-between mt-6">
        <div>
          <p className="text-sm text-slate-500 mb-1">预测类别</p>
          <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium border ${categoryColors[data.category] || 'bg-gray-100'}`}>
            {categoryNames[data.category] || data.category}
          </span>
        </div>
        <div className="text-right">
          <p className="text-sm text-slate-500 mb-1">置信度</p>
          <div className="flex items-center justify-end">
            <span className="text-xl font-bold text-slate-700">
              {(data.confidence * 100).toFixed(1)}%
            </span>
          </div>
        </div>
      </div>
      
      <div className="w-full bg-slate-100 h-2 rounded-full mt-4 overflow-hidden">
        <div 
          className="bg-purple-500 h-full rounded-full transition-all duration-1000" 
          style={{ width: `${data.confidence * 100}%` }}
        />
      </div>
    </div>
  );
}
