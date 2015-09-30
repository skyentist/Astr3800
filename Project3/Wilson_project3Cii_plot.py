
# coding: utf-8

# In[1]:

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


# In[2]:

juldate,averager,averagek,variancer,variancek = restore('Wilson_project3Cii.dat')


# In[5]:

import matplotlib.pyplot as plt
f, axarr = plt.subplots(2,1) #This part of the code takes the two histograms and puts them in the same image
plt.subplots_adjust(hspace = 0.55,wspace = 0.5)
figure = plt.gcf()

axarr[0].plot(juldate,averager,label = 'Red Continuum',color='R')#plot of 1st moment vs. time
axarr[0].plot(juldate,averagek,label = "Calcium")
axarr[0].set_title('1st Moment for Both Filters') 
axarr[0].set_ylabel('Average')          
axarr[0].set_xlabel('Time of Day')
axarr[0].legend(loc=5) #I needed to change the location of the legend so it didn't overlap with the data

axarr[1].plot(juldate,variancer,label = 'Red Continuum',color='R')#plot of 2nd moment vs. time
axarr[1].plot(juldate,variancek,label = "Calcium")
axarr[1].set_title('2nd Moment for Both Filters') 
axarr[1].set_ylabel('Variance')          
axarr[1].set_xlabel('Time of Day')
axarr[1].legend(loc=5)

figure.savefig('Wilson_project3Cii.png',format='png')
plt.show()


# In[ ]:



