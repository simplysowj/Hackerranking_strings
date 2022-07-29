#!/usr/bin/env python
# coding: utf-8

# You are given a string s and width w .
# Your task is to wrap the string into a paragraph of width w .

# In[1]:


import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:




