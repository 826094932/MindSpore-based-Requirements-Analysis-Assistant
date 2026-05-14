import React from 'react';
import { CheckCircle2, Circle, Loader2 } from 'lucide-react';

const steps = [
  { id: 1, name: '规则审计 (模糊词检测)' },
  { id: 2, name: 'MindSpore 轻量分类' },
  { id: 3, name: 'RAG 知识库检索' },
  { id: 4, name: '大模型 GWT 生成' }
];

export default function WorkflowView({ currentStep }: { currentStep: number }) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
      <h2 className="font-semibold text-slate-800 mb-4">分析流水线</h2>
      <div className="space-y-4">
        {steps.map((step, index) => {
          const isCompleted = currentStep > index;
          const isCurrent = currentStep === index;
          
          return (
            <div key={step.id} className="flex items-center space-x-3">
              {isCompleted ? (
                <CheckCircle2 className="text-green-500" size={20} />
              ) : isCurrent ? (
                <Loader2 className="text-blue-500 animate-spin" size={20} />
              ) : (
                <Circle className="text-slate-300" size={20} />
              )}
              <span className={`text-sm ${isCurrent ? 'text-blue-700 font-medium' : isCompleted ? 'text-slate-700' : 'text-slate-400'}`}>
                {step.name}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
