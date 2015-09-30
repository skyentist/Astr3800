
# coding: utf-8

# In[85]:

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


# In[11]:

from astropy.io import fits as pyfits
import numpy as np


import glob
filesr = glob.glob('*.R.P.rdc.fits')#makes an array of all of the red continuum file names
juldate = np.zeros(0)

for i in filesr:#extracts the time of day from them
    headerr = pyfits.getheader(i)
    juldate = np.append(juldate,headerr['JULDATE'])#time of day for red continuum


# In[64]:

filesr = glob.glob('*.R.P.rdc.fits')
juldate = np.zeros(0)

for i in filesr:
    headerr = pyfits.getheader(i)
    juldate = np.append(juldate,headerr['JULDATE'])
    


# In[41]:

namesr = glob.glob('*.R.P.contrast.fits')#this is an array that contains the names of all of the R contrast files
averager = np.zeros(0)#This will serve as my array for the R averages (1st moment)
for i in namesr:
    meta = pyfits.getdata(i)#holds the temporary data for each contrast.fits files
    meta = meta.flatten()#flattens the temporary data
    data,bins = np.histogram(meta, bins=50,normed='True')#data is the PDFS values for the ith fits file
    metaaverage = np.mean(data)#calculates the 1st moment for each of the contrast files
    averager = np.append(averager,metaaverage)#stores the ith average and records the rest of the iterations
    


# In[59]:

namesk = glob.glob('*.K.P.contrast.fits')#this is an array that contains the names of all of the calcium contrast files
averagek = np.zeros(0)#This will serve as my array for the calcium averages (1st moment)
for i in namesk:
    meta = pyfits.getdata(i)#holds the temporary data for each contrast.fits files
    meta = meta.flatten()#flattens the temporary data
    data,bins = np.histogram(meta, bins=50,normed='True')#data is the PDFS values for the ith fits file
    metaaverage = np.mean(data)#calculates the 1st moment for each of the contrast files
    averagek = np.append(averagek,metaaverage)#stores the ith average and records the rest of the iterations
    


# In[72]:

namesr2 = glob.glob('*.R.P.contrast.fits')#this is an array that contains the names of all of the R contrast files
variancer = np.zeros(0)#This will serve as my array for the R variances (2nd moment)
for i in namesr2:
    meta = pyfits.getdata(i)#holds the temporary data for each contrast.fits files
    meta = meta.flatten()#flattens the temporary data
    data,bins = np.histogram(meta, bins=50,normed='True')#data is the PDFS values for the ith fits file
    metav = np.var(data)#calculates the 2nd moment for each of the contrast files
    variancer = np.append(variancer,metav)#stores the ith variance and records the rest of the iterations
    


# In[74]:

namesk2 = glob.glob('*.K.P.contrast.fits')#this is an array that contains the names of all of the calcium contrast files
variancek = np.zeros(0)#This will serve as my array for the calcium variances (2nd moment)
for i in namesk2:
    meta = pyfits.getdata(i)#holds the temporary data for each contrast.fits files
    meta = meta.flatten()#flattens the temporary data
    data,bins = np.histogram(meta, bins=50,normed='True')#data is the PDFS values for the ith fits file
    metav = np.var(data)#calculates the 2nd moment for each of the contrast files
    variancek = np.append(variancek,metav)#stores the ith variance and records the rest of the iterations
    


# In[86]:

save('Wilson_project3Cii.dat',('juldate','averager','averagek','variancer','variancek'),(juldate,averager,averagek,variancer,variancek))


# In[84]:




# In[ ]:



