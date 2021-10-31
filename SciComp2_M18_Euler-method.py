#!/usr/bin/env python
# coding: utf-8

# ### 26.1
# Given
# 
# **$ \frac{\partial y}{\partial x} = -200,000y + 200,000e^{-x} - e^{-x} $**
# 
# * (a) Estimate the step-size required to maintain stability using the explicit Euler method.
# * (b) If y(0) = 0, use the implicit Euler to obtain a solution from x = 0 to 2 using a step size of 0.1.

# ### (a) Explicit Euler
# $y_{i+1} = y_{i} + \frac{\partial y_{i}}{\partial x}h = y_{i} + (-200,000y_{i} + 200,000e^{-x_{i}} - e^{-x_{i}})h $
# 
# Substituting (26.3) equation:
# 
# $\frac{\partial y}{\partial x} = -(-200,000)y$
# 
# $y_{i+1} = y_{i}(1 + 200,000h)$
# 
# To maintain stability: |1 + 200,000h| < 1, so h < 2/200000 = 1e-05
# 

# ### (b) Implicit Euler
# $y_{i+1} = y_{i} + (\frac{\partial y}{\partial x})h = y_{i} + (-200,000y_{i+1} + 200,000e^{-x_{i+1}} - e^{-x_{i+1}})h$
# 

# Isolate $y_{i+1}$:
# 
# $y_{i+1} = \frac{y_{i} + 200,000*e^{-x_{i+1}}*h - e^{-x_{i+1}}*h}{1+200,000h}$

# In[1]:


import math
import decimal


# In[2]:


def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)


# In[3]:


def equation(prev_y, x, h):
    dividend = prev_y + 200000*math.exp(-x)*h - math.exp(-x)*h
    divisor = 1 + 200000*h
    quotient = dividend/divisor
    return quotient


# In[4]:


equation(0, 0, 0.1)


# In[5]:


def euler(y0, xLower, xUpper, h):
    yVals = [y0]
    xVals = []
    for x in float_range(xLower, xUpper+0.001, h): 
        prev_y = yVals[-1]
        y = equation(prev_y, x, h)
        xVals.append(x)
        yVals.append(y)
    return (xVals, yVals[1:])


# In[6]:


xVals, yVals = euler(0, 0, 2, 0.1)


# In[7]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(xVals, yVals)

ax.set(xlabel='x', ylabel='y')
ax.grid()
plt.show()


# In[ ]:




