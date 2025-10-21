import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn
from torchtyping import TensorType

x = torch.tensor([10, 100, 1000])
y = torch.tensor([1.94, 7.44, 12.92])

class MichaelisMenten():
    def __init__(self):
        self.v = torch.randn(1, requires_grad=True)
        self.k = torch.randn(1, requires_grad=True)
    @property
    def params(self):
        return [self.v, self.k]

    def forward(self,x):
        return (self.v*x)/(self.k+x)
    
m = MichaelisMenten()

def square_loss(y_pred:TensorType, y:TensorType):
    return ((y_pred-y)**2)*0.5

def sgd(params, lr, batch_size = 1):
    with torch.no_grad():
        for param in params:
            param -= lr*param.grad/batch_size
            param.grad.zero_()

lr = 0.5
num_epochs = 8001

all_loss = []
for epoch in range(num_epochs):
    pred = m.forward(x)
    ls = square_loss(pred, y)
    ls.sum().backward()
    sgd([m.v, m.k], lr, 1)
    all_loss.append(float(ls.mean()))
    a = np.arange(1000)

    if epoch % 500 == 0:
        plt.plot(a, (m.v.detach()*a)/(m.k.detach()+a))
        plt.scatter(x, y)
        plt.title(f'Epoch: {epoch}')
        plt.show()
    #print(f'epoch {epoch + 1}, loss {float(ls.mean()):f}, k:{m.k.detach()}, v: {m.v.detach()}')
#with torch.no_grad():
    #train_loss = square_loss(m.forward(x), y)
    #print(f'epoch {epoch + 1}, loss {float(train_loss.mean()):f}')
plt.plot(np.arange(num_epochs), all_loss)
plt.title(f'k:{m.k.detach()}, v: {m.v.detach()}')