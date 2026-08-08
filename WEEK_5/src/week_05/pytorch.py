import torch
x1t = torch.tensor([2.0], requires_grad=True)
x2t = torch.tensor([0.0], requires_grad=True)
ot = torch.tanh(x1t*(-3.0) + x2t*(1.0) + 6.8813735870195432)
ot.backward()
print('x1.grad (torch):', x1t.grad.item()) 
print('x2.grad (torch):', x2t.grad.item()) 