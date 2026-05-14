import json
import os
try:
    import mindspore.dataset as ds
    import numpy as np
except ImportError:
    pass # 允许在没有MindSpore的环境下导入用于查看结构

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    texts = [item['text'] for item in data]
    labels_map = {"clear": 0, "ambiguous": 1, "incomplete": 2, "untestable": 3}
    labels = [labels_map[item['label']] for item in data]
    
    return texts, labels

class RequirementDataset:
    def __init__(self, features, labels):
        self.features = features
        self.labels = np.array(labels, dtype=np.int32)
        
    def __getitem__(self, index):
        return self.features[index], self.labels[index]
        
    def __len__(self):
        return len(self.features)

def create_dataset(features, labels, batch_size=4):
    dataset_generator = RequirementDataset(features, labels)
    dataset = ds.GeneratorDataset(dataset_generator, ["data", "label"])
    dataset = dataset.batch(batch_size)
    return dataset
