import React from 'react';
import { Lightbulb } from 'lucide-react';

export default function ImprovementPanel({ improvedText }: { improvedText: string }) {
  if (!improvedText || improvedText === "N/A" || improvedText === "Failed to generate") return null;

  return (
    <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl shadow-sm border border-blue-100 p-6">
      <div className="flex items-center space-x-2 mb-3">
        <Lightbulb size={20} className="text-blue-600" />
        <h2 className="font-semibold text-blue-900 text-lg">Deepseek改写建议</h2>
      </div>
      
      <p className="text-blue-800 leading-relaxed font-medium">
        {improvedText}
      </p>
    </div>
  );
}
