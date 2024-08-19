#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system(' pip install deepface==0.0.81')
get_ipython().system(' pip install tensorflow==2.15.1')


# In[4]:


from deepface import DeepFace  #import deepface library


# In[8]:


def verify_images(image1_path, image2_path):
  result = DeepFace.verify(img1_path=image1_path, img2_path=image2_path)  # to calculate similarity between 2 images
  similarity_score = result["distance"]  # to get similarity score
  print(similarity_score)
  return similarity_score


# In[11]:


x = verify_images("C:/Users/marwa/Downloads/A1.jpg","C:/Users/marwa/Downloads/A2.jpg")
print(x)


# In[ ]:





# In[ ]:





# In[ ]:




