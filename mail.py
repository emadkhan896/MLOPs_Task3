#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("emadkhan896@gmail.com", "*************")


    # message
message1 = "accuracy is less than 90%.Try again"
    

    # sending the mail 
s.sendmail("emadkhan896@gmail.com.com", "1706237@kiit.ac.in", message1)
    

    # terminating the session 
s.quit()

