import os
import sys
import pickle

try:
    import mindspore as ms
    from mindspore import Tensor
    import numpy as np
    
    # 尝试导入同级目录下的模块
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.append(current_dir)
        
    from model import RequirementClassifier
    MINDSPORE_AVAILABLE = True
except ImportError:
    MINDSPORE_AVAILABLE = False

class RequirementPredictor:
    def __init__(self):
        if not MINDSPORE_AVAILABLE:
            raise ImportError("MindSpore is not installed.")
            
        self.model_dir = os.path.join(os.path.dirname(__file__), 'model_checkpoint')
        self.extractor_path = os.path.join(self.model_dir, 'extractor.pkl')
        self.model_path = os.path.join(self.model_dir, 'requirement_model.ckpt')
        
        self.labels_map = {0: "clear", 1: "ambiguous", 2: "incomplete", 3: "untestable"}
        
        self._load_model()
        
    def _load_model(self):
        if not os.path.exists(self.extractor_path) or not os.path.exists(self.model_path):
            raise FileNotFoundError("Model files not found. Please run train.py first.")
            
        with open(self.extractor_path, 'rb') as f:
            self.extractor = pickle.load(f)
            
        input_dim = self.extractor.get_vocab_size()
        self.network = RequirementClassifier(input_dim=input_dim, num_classes=4)
        ms.load_checkpoint(self.model_path, net=self.network)
        self.network.set_train(False)
        
    def predict(self, text):
        features = self.extractor.transform([text])
        tensor_data = Tensor(features, ms.float32)
        logits = self.network(tensor_data)
        
        probs = ms.ops.Softmax()(logits).asnumpy()[0]
        predicted_class = int(np.argmax(probs))
        confidence = float(probs[predicted_class])
        
        return self.labels_map[predicted_class], confidence
