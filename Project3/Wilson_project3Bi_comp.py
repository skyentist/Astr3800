
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

from astropy.io import fits as pyfits
import numpy as np
import matplotlib.pyplot as plt

rdck, headerk = pyfits.getdata('20050702.1702.HW.K.P.rdc.fits',header=True)

rdcr, headerr = pyfits.getdata('20050702.1702.HW.R.P.rdc.fits',header=True)


# In[3]:

import glob
filesk = glob.glob('*.K.P.rdc.fits')#sticks all of the calcium rdc files into one array to use later
filesr = glob.glob('*.R.P.rdc.fits')
juldate = np.zeros(0)

for i in filesk:#this will extract all of the JULDATE's from the calcium headers
    headerk = pyfits.getheader(i)
    juldate = np.append(juldate,headerk['JULDATE'])
    
avgk = np.zeros(0)

for i in filesk:#This extracts the AVGWIDTH data from the calcium headers
    headerk = pyfits.getheader(i)
    avgk = np.append(avgk,headerk['AVGWIDTH'])
    
rmsak = np.zeros(0)

for i in filesk: #Extracts the RMSA data from the calcium headers
    headerk = pyfits.getheader(i)
    rmsak = np.append(rmsak,headerk['RMSA'])
    
avgr = np.zeros(0)

for i in filesr: #This extracts the AVGWIDTH data from the red continuum headers
    headerr = pyfits.getheader(i)
    avgr = np.append(avgr,headerr['AVGWIDTH'])
    
rmsar = np.zeros(0)

for i in filesr: #This extracts the RMSA data from the red continuum headers
    headerr = pyfits.getheader(i)
    rmsar = np.append(rmsar,headerr['RMSA'])
    


# In[4]:

save('Wilson_project3Bi.dat',('juldate','avgk','rmsak','avgr','rmsar'),(juldate,avgk,rmsak,avgr,rmsar))


# In[ ]:




# In[ ]:



