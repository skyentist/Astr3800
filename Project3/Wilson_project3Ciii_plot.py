
# coding: utf-8

# In[37]:

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


# In[38]:

from astropy.io import fits as pyfits
import numpy as np
import matplotlib.pyplot as plt
import glob

filesr = glob.glob('*.R.P.rdc.fits')
widthr = np.zeros(0)

for i in filesr: #This will extract all of the red continuum AVGWIDTH data from their files
    headerr = pyfits.getheader(i)
    widthr = np.append(widthr,headerr['AVGWIDTH'])
    
    
filesk = glob.glob('*.K.P.rdc.fits')
widthk = np.zeros(0)

for i in filesk: #This does the same but for calcium
    headerk = pyfits.getheader(i)
    widthk = np.append(widthk,headerk['AVGWIDTH'])


# In[39]:

juldate,averager,averagek,variancer,variancek = restore('Wilson_project3Cii.dat')


# In[ ]:




# In[40]:

f, axarr = plt.subplots(2,2) #This part of the code takes the two histograms and puts them in the same image
plt.subplots_adjust(hspace = 0.55,wspace = 0.5)
figure = plt.gcf()

axarr[0,0].scatter(widthr,averager,color='R') #creates a scatter plot of 1st moment Vs. AVGWIDTH
axarr[0,0].set_title('Scatter Plot of Red Continuum 1st moment') 
axarr[0,0].set_ylabel('Average')          
axarr[0,0].set_xlabel('AVGWIDTH')


axarr[0,1].scatter(widthk,averagek,color='B')
axarr[0,1].set_title('Scatter Plot of Calcium 1st moment') 
axarr[0,1].set_ylabel('Average')          
axarr[0,1].set_xlabel('AVGWIDTH')

axarr[1,0].scatter(widthr,variancer,color='G') #creates a scatter plot of 2nd moment Vs. AVGWIDTH
axarr[1,0].set_title('Scatter Plot of Red Continuum 2nd moment') 
axarr[1,0].set_ylabel('Variance')          
axarr[1,0].set_xlabel('AVGWIDTH')

axarr[1,1].scatter(widthk,variancek,color='C')
axarr[1,1].set_title('Scatter Plot of Calcium 2nd moment') 
axarr[1,1].set_ylabel('Variance')          
axarr[1,1].set_xlabel('AVGWIDTH')

figure.savefig('Wilson_project3Ciii.png',format='png')
plt.show()


# In[ ]:




# In[ ]:



