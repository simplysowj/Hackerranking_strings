#!/usr/bin/env python
# coding: utf-8

# In[1]:


def split_and_join(line):
    
    # write your code here
    line=line.split(" ")
    #print(line)
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:




