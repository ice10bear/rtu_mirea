from sys import maxsize
import numpy as np
class Stack:  
    def __init__(self):
        self.stack = [] #1

    def isEmpty(self):
        #global nop
        #nop+=3
        return len(self.stack) == 0 #3

    def push(self, item):
        #global nop
        #nop+=2
        return self.stack.append(item) #2

    def pop(self):
        #global nop
        #nop+=9
        if self.isEmpty(): #4
            return str(-maxsize - 1)  #3
        return self.stack.pop() #2

    def peek(self):
        #global nop
        #nop+=9
        if self.isEmpty(): #4
            return self.stack #1
        return self.stack[len(self.stack) - 1] #4

    def sort(self):
        #global nop
        #nop+=7
        if self.isEmpty() != True: #4
            x = self.stack.pop() #2
            self.sort()
            self.insert(self.stack, x) #n + n + 6
        return self.stack #1

    def insert(self, stack, x):
        #global nop
        if len(stack) > 0: # 2
            #nop+=6
            y = self.stack[-1] #2
            if x < y: #1
                self.stack.pop() #1
                self.insert(self.stack, x)
                self.push(y) #2
            else:
                self.push(x) #2

        else:
            #nop+=1
            self.stack.append(x) #1

stack = Stack()
d = np.random.randint(0, 100, size=25)

for i in list(d):
    stack.push(i)

print(stack.stack)
print("===")
print(stack.sort())

import matplotlib.pyplot as plt
import time
import numpy as np
import time
import sys
from scipy.interpolate import interp1d
sys.setrecursionlimit(20000)
from scipy.interpolate import make_interp_spline, BSpline

n = [10,50,100,500,1000,2500,5000,7000,10000]
def filler(count):
    d = np.random.randint(0, 100, size=count)
    s = Stack()
    for i in d:
        s.push(i)
    return s

timey = []
nop_arr = []
for i in n:
    x = filler(i)
    st = time.monotonic()
    x.sort()
    timey.append((time.monotonic() - st))
plt.figure(figsize=(12, 7))

n = np.array(n)
timey = np.array(timey)


xnew = np.linspace(n.min(), n.max(), 300) 
spl = make_interp_spline(n, timey, k=3)  # type: BSpline
power_smooth = spl(xnew)
plt.grid(True)
plt.plot(xnew, power_smooth, label="dependence")
plt.title("Т(n)")
plt.xlabel("Array size")
plt.ylabel("milliseconds ")
plt.legend()
plt.show()

for i in range(len(n)):
  print(n[i],timey[i])


