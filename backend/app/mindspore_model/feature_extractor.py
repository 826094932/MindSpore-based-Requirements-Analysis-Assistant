class SimpleFeatureExtractor:
    def __init__(self, vocab_size=1000):
        self.vocab_size = vocab_size
        self.vocab = {}
        
    def fit(self, texts):
        # 极简的分词和词表构建
        words = set()
        for text in texts:
            for char in text:
                words.add(char)
                
        for i, word in enumerate(list(words)[:self.vocab_size]):
            self.vocab[word] = i + 1
            
    def transform(self, texts):
        import numpy as np
        features = np.zeros((len(texts), self.vocab_size), dtype=np.float32)
        for i, text in enumerate(texts):
            for char in text:
                if char in self.vocab:
                    features[i, self.vocab[char]-1] = 1.0
        return features
        
    def get_vocab_size(self):
        return len(self.vocab) if self.vocab else self.vocab_size
