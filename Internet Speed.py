#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speedtest
st = speedtest.Speedtest()
option = int(input('''What Speed you want to test 
1 Download Speed
2 Upload Speed
3 Ping
Enter Your Choice: '''))
if option ==1:
    print(st.download(),'b/s')
elif option ==2:
    print(st.upload(),'b/s')
elif option ==3:
    servernames=[]
    st.get_servers(servernames)
    print(st.results.ping,'b/s')
else:
    print("Enter correct choice")


# In[ ]:




