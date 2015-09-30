
# coding: utf-8

# In[5]:

import numpy as np

def save(filename, names, data):
    """
    filename = a string specifying the name of the file to be saved
    names = a tuple of the variable names given as strings
    data = a tuple of arrays
    """

    fyl  = open(filename, 'wb')

    for i, name in enumerate(names):
        fyl.write(name + '\n') # \n = a linebreak

        var = data[i]
        shape = var.shape
        shape = ','.join(np.array(shape,dtype=str))
        fyl.write(shape+'\n')
        
        dtype = str(var.dtype)
        fyl.write(dtype+'\n')

        var_str = var.flatten().tobytes()
        fyl.write(var_str+'\n\n')

    fyl.close()
        



def restore(filename):
    """
    filename = a string specifying the name of the file to be restored
    """

    fyl = open(filename,'rb')

    data = []
    
    print("Restoring variables: \n")
    while True:
        var_name = fyl.readline()
        if var_name == "": break
        print(var_name)

        shape = fyl.readline().replace('\n', '') # I CHANGED THIS
        shape = shape.split(',')
        shape = np.array(shape,dtype=int)
        
        dtype = fyl.readline().replace('\n','')  # I CHANGED THIS

        data_str = ""
        line = ""
        while line != '\n':
            data_str += line
            line = fyl.readline()

        array = np.fromstring(data_str[:-1],dtype=dtype)
        array = array.reshape(shape)
        data.append(array) 

    fyl.close()
    return data


# In[6]:

juldate,avgk,rmsak,avgr,rmsar = restore('Wilson_project3Bi.dat')#need to restore the variables from before to plot them


# In[42]:

import numpy as np
import matplotlib.pyplot as plt

f, axarr = plt.subplots(1, 2,figsize = (13,8)) 
plt.subplots_adjust(hspace = 0.55,wspace = 0.5)
figure = plt.gcf()

axarr[0].plot(juldate,avgr,'r',label='Avgwidth Red continuum') #plots the AVDWIDTH vs. juldate
axarr[0].plot(juldate,avgk,'b',label='Avgwidth Calcium') 
axarr[0].set_title('AVGWIDTH Over Time') 
axarr[0].set_ylabel('AVGWIDTH')          
axarr[0].set_xlabel('Time')
axarr[0].legend()
                                         
axarr[1].plot(juldate, rmsar,'r',label='RMSA Red Continuum') #plots RMSA vs. juldate
axarr[1].plot(juldate, rmsak,'b',label='RMSA Calcium') 
axarr[1].set_title('RMSA Over Time') 
axarr[1].set_ylabel('RMSA')          
axarr[1].set_xlabel('Time')
axarr[1].legend()

figure.savefig('Wilson_project3Bii.png',format='png')
plt.show()


# In[ ]:



