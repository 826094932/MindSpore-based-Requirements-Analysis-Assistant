import React from 'react';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, ResponsiveContainer, PolarRadiusAxis } from 'recharts';
import { RadarData } from '../api/client';
import { Activity } from 'lucide-react';

interface Props {
  score: number;
  radarData: RadarData[];
}

export default function QualityDashboard({ score, radarData }: Props) {
  let scoreColor = 'text-green-600';
  if (score < 60) scoreColor = 'text-red-600';
  else if (score < 80) scoreColor = 'text-yellow-600';

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 flex flex-col h-full">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-2">
          <Activity size={18} className="text-blue-600" />
          <h2 className="font-semibold text-slate-800">质量综合评分</h2>
        </div>
        <div className={`text-3xl font-bold ${scoreColor}`}>
          {score}
        </div>
      </div>
      
      <div className="flex-1 min-h-[200px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <RadarChart cx="50%" cy="50%" outerRadius="70%" data={radarData}>
            <PolarGrid gridType="polygon" />
            <PolarAngleAxis dataKey="subject" tick={{ fill: '#64748b', fontSize: 12 }} />
            <PolarRadiusAxis angle={30} domain={[0, 100]} tick={false} />
            <Radar
              name="Quality"
              dataKey="A"
              stroke="#3b82f6"
              fill="#3b82f6"
              fillOpacity={0.4}
            />
          </RadarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
