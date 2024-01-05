#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.db import models

class Device(models.Model):
    admin = models.CharField(max_length=100)
    # Add other fields as needed

