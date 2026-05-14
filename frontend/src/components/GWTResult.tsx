import React from 'react';
import { Sparkles, ArrowRight } from 'lucide-react';

interface Props {
  data: {
    given: string;
    when: string;
    then: string;
    source: string;
  };
}

export default function GWTResult({ data }: Props) {
  if (!data) return null;
  
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-2">
          <Sparkles size={18} className="text-indigo-600" />
          <h2 className="font-semibold text-slate-800">智能 GWT </h2>
        </div>
        <span className="text-xs px-2 py-1 bg-indigo-50 text-indigo-700 rounded-full border border-indigo-100">
          Source: {data.source}
        </span>
      </div>

      <div className="space-y-3">
        <div className="flex items-start">
          <div className="w-16 shrink-0 text-sm font-bold text-slate-400 mt-1">Given</div>
          <div className="bg-indigo-50 border border-indigo-100 rounded-lg p-3 text-sm text-indigo-900 w-full">
            {data.given}
          </div>
        </div>
        
        <div className="flex items-start">
          <div className="w-16 shrink-0 text-sm font-bold text-slate-400 mt-1">When</div>
          <div className="bg-indigo-50 border border-indigo-100 rounded-lg p-3 text-sm text-indigo-900 w-full">
            {data.when}
          </div>
        </div>

        <div className="flex items-start">
          <div className="w-16 shrink-0 text-sm font-bold text-slate-400 mt-1">Then</div>
          <div className="bg-indigo-50 border border-indigo-100 rounded-lg p-3 text-sm text-indigo-900 w-full">
            {data.then}
          </div>
        </div>
      </div>
    </div>
  );
}
