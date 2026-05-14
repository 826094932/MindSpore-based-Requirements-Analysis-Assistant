import React, { useState } from 'react';
import RequirementInput from './components/RequirementInput';
import WorkflowView from './components/WorkflowView';
import QualityDashboard from './components/QualityDashboard';
import RiskList from './components/RiskList';
import MindSporePanel from './components/MindSporePanel';
import RetrievedExamples from './components/RetrievedExamples';
import GWTResult from './components/GWTResult';
import ImprovementPanel from './components/ImprovementPanel';
import TechArchitecture from './components/TechArchitecture';
import { analyzeRequirement, AnalyzeResponse } from './api/client';
import { Activity } from 'lucide-react';

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [currentStep, setCurrentStep] = useState(0);

  const handleAnalyze = async (text: string) => {
    setLoading(true);
    setResult(null);
    setCurrentStep(0);
    
    // Simulate steps for UI
    const stepsInterval = setInterval(() => {
      setCurrentStep(prev => (prev < 4 ? prev + 1 : prev));
    }, 600);

    try {
      const data = await analyzeRequirement(text);
      clearInterval(stepsInterval);
      setCurrentStep(4);
      setResult(data);
    } catch (error) {
      console.error(error);
      clearInterval(stepsInterval);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 p-6">
      <header className="max-w-6xl mx-auto mb-8 flex items-center space-x-3">
        <div className="p-2 bg-blue-600 rounded-lg text-white">
          <Activity size={24} />
        </div>
        <div>
          <h1 className="text-2xl font-bold text-slate-900">基于MindSpore的需求分析助手</h1>
          <p className="text-slate-500 text-sm">需求分析智能化</p>
        </div>
      </header>

      <main className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column - Input & Status */}
        <div className="lg:col-span-4 space-y-6">
          <RequirementInput onAnalyze={handleAnalyze} loading={loading} />
          {loading || result ? (
            <WorkflowView currentStep={currentStep} />
          ) : null}
          <TechArchitecture />
        </div>

        {/* Right Column - Results */}
        <div className="lg:col-span-8 space-y-6">
          {result ? (
            <div className="animate-fade-in space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <QualityDashboard score={result.audit.score} radarData={result.audit.radar_data} />
                <div className="space-y-6">
                   <MindSporePanel data={result.mindspore} />
                   <RiskList risks={result.audit.risks} />
                </div>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <RetrievedExamples examples={result.rag.retrieved_examples} />
                <GWTResult data={result.gwt} />
              </div>
              
              <ImprovementPanel improvedText={result.gwt.improved_requirement} />
            </div>
          ) : (
            <div className="h-full min-h-[400px] flex items-center justify-center border-2 border-dashed border-slate-200 rounded-xl p-12 text-slate-400 bg-white">
              <div className="text-center">
                <Activity size={48} className="mx-auto mb-4 opacity-50" />
                <p>输入需求文本开始智能分析</p>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
