import React from 'react';
import { Layers } from 'lucide-react';

export default function TechArchitecture() {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mt-6">
      <div className="flex items-center space-x-2 mb-4">
        <Layers size={18} className="text-slate-600" />
        <h2 className="font-semibold text-slate-800">技术架构简述</h2>
      </div>
      
      <ul className="text-xs text-slate-600 space-y-2">
        <li className="flex items-center"><span className="w-2 h-2 rounded-full bg-blue-400 mr-2"></span> <strong>前端:</strong> React 18 + TailwindCSS + Recharts</li>
        <li className="flex items-center"><span className="w-2 h-2 rounded-full bg-green-400 mr-2"></span> <strong>后端:</strong> FastAPI (Python 3.10)</li>
        <li className="flex items-center"><span className="w-2 h-2 rounded-full bg-purple-400 mr-2"></span> <strong>模型:</strong> MindSpore 分类 + DeepSeek RAG/GWT</li>
        <li className="flex items-center"><span className="w-2 h-2 rounded-full bg-yellow-400 mr-2"></span> <strong>容灾:</strong> 支持 Mock 降级模式</li>
      </ul>
    </div>
  );
}
