#!/usr/bin/env python
# coding: utf-8

# In[52]:


class loan(object):
    def __init__(self, name):
        self._name = name
        
    def who(self):
        print(self._name)
    
    def setPV(self, PV):
        self._PV = PV
        print("Present Value = ", self._PV)
        
    def setRate(self, ratePct):
        self._ratePct = ratePct
        print("Rate = {:.2f}%".format(self._ratePct))
            
    def setMonths(self, months):
        self._months = months
        print(self._months, "Months")
        
    def computePmt(self):
        r = self._ratePct/100/12
        self._Pmt = self._PV * (r * (1 + r)**self._months) / ((1 + r)**self._months - 1)
        print("Payment = ${:.2f}".format(self._Pmt))
        return self._Pmt
    
    def computeRate(self, Pmt, PV, months, acc):
        self._topR = 100
        self._botR = 0
        self.setPV(PV)
        self.setMonths(months)
        
        while(True):
            self._currRate = (self._topR + self._botR) / 2
            self.setRate(self._currRate)
            self._currPmt = self.computePmt()
            if(abs(self._currPmt - Pmt) < 1*10**-acc):
                self._currRate = round(self._currRate, acc)
                print("Rate = {:.2f}%".format(self._currRate))
                return self._currRate
            elif(self._currPmt > Pmt):
                self._topR = self._currRate
            else:
                self._botR = self._currRate


# In[53]:


loan_test = loan("Jim")


# In[54]:


loan_test.setPV(10000)
loan_test.setRate(5)
loan_test.setMonths(48)
loan_test.computePmt()


# In[56]:


loan_test.computeRate(Pmt=230.29, PV=10000, months=48, acc=2)


# In[ ]:




