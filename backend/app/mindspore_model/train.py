import os
import sys

try:
    import mindspore as ms
    import mindspore.nn as nn
    from mindspore import Model
    from mindspore.train.callback import LossMonitor
    import pickle
except ImportError:
    print("MindSpore is not installed. Please install it to train the model.")
    sys.exit(0)

from dataset import load_data, create_dataset
from model import RequirementClassifier
from feature_extractor import SimpleFeatureExtractor

def train():
    # 1. 准备数据
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'training_samples.json')
    texts, labels = load_data(data_path)
    
    # 2. 提取特征
    extractor = SimpleFeatureExtractor(vocab_size=200)
    extractor.fit(texts)
    features = extractor.transform(texts)
    
    # 保存特征提取器
    checkpoint_dir = os.path.join(os.path.dirname(__file__), 'model_checkpoint')
    os.makedirs(checkpoint_dir, exist_ok=True)
    with open(os.path.join(checkpoint_dir, 'extractor.pkl'), 'wb') as f:
        pickle.dump(extractor, f)
        
    dataset = create_dataset(features, labels, batch_size=4)
    
    # 3. 定义模型
    input_dim = extractor.get_vocab_size()
    network = RequirementClassifier(input_dim=input_dim, num_classes=4)
    
    # 4. 定义损失函数和优化器
    loss_fn = nn.CrossEntropyLoss()
    optimizer = nn.Adam(network.trainable_params(), learning_rate=0.01)
    
    # 5. 编译模型
    model = Model(network, loss_fn, optimizer, metrics={"Accuracy": nn.Accuracy()})
    
    # 6. 训练
    print("Starting training...")
    model.train(10, dataset, callbacks=[LossMonitor(1)], dataset_sink_mode=False)
    print("Training finished.")
    
    # 7. 保存模型
    ms.save_checkpoint(network, os.path.join(checkpoint_dir, "requirement_model.ckpt"))
    print("Model saved.")

if __name__ == "__main__":
    ms.set_context(mode=ms.GRAPH_MODE, device_target="CPU")
    train()
