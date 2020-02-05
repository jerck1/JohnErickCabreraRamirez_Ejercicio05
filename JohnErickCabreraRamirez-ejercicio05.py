#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


toss=np.array(["s","c","c","c","c"])


# In[14]:


def P(H):
    return 1


# In[9]:


#def P(event,data):
 #   p=np.count_nonzero(toss == event)/np.size(toss)
  #  return p


# In[34]:


H=np.arange(0,1.1,0.1)
H


# In[35]:


def P_obs_H(nc,ns,H):
    P=H**nc*(1-H)**ns
    return P


# In[36]:


P_obs_H(np.count_nonzero(toss == "s"),np.count_nonzero(toss == "c"),H)


# In[37]:


def P_H_obs(nc,ns,H,toss):
    p=P_obs_H(nc,ns,H)*P(H)/np.size(toss)
    return p


# In[38]:


y=P_H_obs(np.count_nonzero(toss == "s"),np.count_nonzero(toss == "c"),H,toss)


# In[39]:


plt.figure(figsize=(8,8))
plt.plot(H,y)
plt.xlabel("H")
plt.ylabel('P(H|obs)')


# In[48]:


def x_max(y):
    for i in range(np.size(y)-1):
        if np.diff(y)[i]*np.diff(y)[i+1]<0 :
            print (y[i]+y[i+1])/2


# In[49]:


x_max(y)


# In[32]:


np.diff(y)


# In[40]:


np.diff(np.diff(y))


# In[41]:


np.abs(-1)


# In[ ]:




