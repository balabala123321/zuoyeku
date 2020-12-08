#!/usr/bin/env python
# coding: utf-8

# In[64]:


class BMI:
    def __init__(self,xingming,nianling,tizhong,shengao):
        self.xingming = xingming
        self.nianling = nianling
        self.tizhong = tizhong
        self.shengao = shengao
        self.bmi = tizhong/(shengao*shengao)
        t = self.bmi
        if t<18.5:
            n = "偏瘦"
        elif t>=18.5 and t<24:
            n = "正常"
        else:
            n = "偏胖"
        self.jiankang = n
    def chaBMI(self):
        print("{n}".format(n=self.xingming),"的BMI是：{n}".format(n=self.bmi),"健康状况是：{n}".format(n=self.jiankang))
    def chanianling(self):
        print("{n}".format(n=self.xingming),"的年龄是：{n}".format(n=self.nianling)) 
    def chatizhong(self):
        print("{n}".format(n=self.xingming),"的体重是：{n}".format(n=self.tizhong)) 
    def chashengao(self):
        print("{n}".format(n=self.xingming),"的身高是：{n}".format(n=self.shengao))   


# In[65]:


bmi1 = BMI("张三",18,70,1.75)


# In[66]:


bmi1.chaBMI()


# In[67]:


bmi1.chanianling()


# In[68]:


bmi1.chatizhong()


# In[69]:


bmi1.chashengao()


# In[ ]:




