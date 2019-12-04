import torch


class JetNet(torch.nn.Module):

    def __init__(self, alpha=0.01):

        super(JetNet, self).__init__()

        self.initialize_network()
        self.optimizer = torch.optim.Adam(params=self.parameters(), lr=alpha)


    def initialize_network(self):
        pass


    def forward(self):
        pass


    def optmize(self):
        pass
