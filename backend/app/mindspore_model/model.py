try:
    import mindspore.nn as nn
    from mindspore import Tensor
except ImportError:
    
    class nn:
        Cell = object
        Dense = object
        ReLU = object

class RequirementClassifier(nn.Cell):
    def __init__(self, input_dim, num_classes=4):
        super(RequirementClassifier, self).__init__()
        self.fc1 = nn.Dense(input_dim, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Dense(64, 32)
        self.fc3 = nn.Dense(32, num_classes)

    def construct(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x
