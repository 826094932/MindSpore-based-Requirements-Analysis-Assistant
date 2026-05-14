import React from 'react';
import { AlertOctagon, ShieldAlert } from 'lucide-react';
import { RiskItem } from '../api/client';

export default function RiskList({ risks }: { risks: RiskItem[] }) {
  if (risks.length === 0) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 flex flex-col items-center justify-center h-32">
        <ShieldAlert className="text-green-500 mb-2" size={24} />
        <p className="text-slate-500 text-sm">未检测到高风险模糊词</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 max-h-48 overflow-y-auto">
      <div className="flex items-center space-x-2 mb-4 sticky top-0 bg-white z-10 pb-2">
        <AlertOctagon size={18} className="text-red-500" />
        <h2 className="font-semibold text-slate-800">模糊风险词检测 ({risks.length})</h2>
      </div>
      
      <div className="space-y-3">
        {risks.map((risk, idx) => (
          <div key={idx} className="flex items-start space-x-3 p-3 bg-red-50 text-red-900 rounded-lg text-sm border border-red-100">
            <div className="mt-0.5 w-2 h-2 rounded-full bg-red-500 shrink-0" />
            <div>
              <span className="font-bold underline decoration-red-300 underline-offset-2 mr-2">"{risk.word}"</span>
              <span className="opacity-90">{risk.reason}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
