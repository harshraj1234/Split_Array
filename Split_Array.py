#!/usr/bin/env python
# coding: utf-8

# In[38]:


def split_list(a_list):
    half = len(a_list)//3
    return a_list[:half], a_list[half:half+2],a_list[half+2:]

A = [1,2,3,4,5,6]
B,C,D = split_list(A)
print(B)
print(C)
print(D)


# In[39]:


res1=B[0]+B[1]
res2=C[0]+C[1]
res3=D[0]+D[1]
print("res1:",res1)
print("res2:",res2)
print("res3:",res3)


# In[40]:


B.append(res1)
C.append(res2)
D.append(res3)
print(B)
print(C)
print(D)


# In[41]:


M=[]
M.append(B)
M.append(C)
M.append(D)
print(M)

