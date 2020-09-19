import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import OrderedDict

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.model = nn.Sequential(OrderedDict([
                                  ('fc1', nn.Linear(state_size,64)),
                                  ('relu1', nn.ReLU()),
                                  ('fc2', nn.Linear(64, 64)),
                                  ('relu2', nn.ReLU()),
                                  ('output', nn.Linear(64,64))
                                ]))
        self.valueModel = nn.Sequential(OrderedDict([
            ('fcV1', nn.Linear(64, 64)),
            ('reluV1', nn.ReLU()),
            ('fcV2', nn.Linear(64, 1))
        ]))

        self.advantageModel = nn.Sequential(OrderedDict([
            ('fcA1', nn.Linear(64, 64)),
            ('reluA1', nn.ReLU()),
            ('fcA2', nn.Linear(64, action_size))
        ]))

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.model(state)
        advantages = self.advantageModel(x)
        value = self.valueModel(x)
        return value + (advantages - advantages.mean())
    def trainNet(self, output, target):
        loss = nn.MSELoss()
        loss(output, target).backward()
