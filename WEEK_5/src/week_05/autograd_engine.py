import math
class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data,(self, other) , '+')
        def _backward():
            self.grad += out.grad * 1
            other.grad += out.grad * 1
        out._backward = _backward 
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        mul_out = Value(self.data * other.data,(self, other), '*')
        def _backward():
            self.grad += mul_out.grad * other.data
            other.grad += mul_out.grad * self.data
        mul_out._backward = _backward
        return mul_out
    
    def __pow__(self, other):
        pow_out = Value(self.data ** other, (self,), '**')
        def _backward():
            self.grad += pow_out.grad * (other*(self.data **(other - 1)))
        pow_out._backward = _backward
        return pow_out

    def relu(self):
        reLu_out = Value(max(0,self.data),(self,), 'ReLU')
        def _backward():
            if self.data > 0:
                self.grad += reLu_out.grad * 1
            else:
                self.grad += reLu_out.grad * 0
        reLu_out._backward = _backward
        return reLu_out
    
    def tanh(self):
        tanh_out = Value(math.tanh(self.data), (self,), 'tanh')
        def _backward():
            self.grad += tanh_out.grad * (1 - (tanh_out.data)**2)
        tanh_out._backward = _backward
        return tanh_out

    def backward(self):
        topo, visited = [], set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()

    def __repr__(self):
        return f'Value(data={self.data:.4f}, grad={self.grad:.4f})'
    
def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

from graphviz import Digraph

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a * b
d = e + c
f = Value(-2.0, label='f')
L = d * f
print(L)
print(L.backward)

x1 = Value(2.0); x2 = Value(0.0)
w1 = Value(-3.0); w2 = Value(1.0)
b = Value(6.8813735870195432)
n = x1*w1 + x2*w2 + b
o = n.tanh()
o.backward()
print('x1.grad (yours):', x1.grad) 
print('x2.grad (yours):', x2.grad) 


def draw_dot(root):
    nodes, edges = trace(root)
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
    for n in nodes:
        dot.node(name=str(id(n)), label=f"{n.label} | data {n.data:.4f} | grad {n.grad:.4f}", shape='record')
        if n._op:
            dot.node(name=str(id(n)) + n._op, label=n._op)
            dot.edge(str(id(n)) + n._op, str(id(n)))
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    return dot

dot = draw_dot(L)
dot.render('week5_graph', view=True)

        














