
# coding: utf-8

# In[30]:

from astropy.io import fits as pyfits
import numpy as np
import matplotlib.pyplot as plt

contrast1R = pyfits.getdata('20050702.1702.HW.R.P.contrast.fits') #These arguments pull the data from the fits files 
contrast2R = pyfits.getdata('20050702.1720.HW.R.P.contrast.fits') #and stores them in their specified array
contrast3R = pyfits.getdata('20050702.1740.HW.R.P.contrast.fits')

contrast1R = contrast1R.flatten()#Since the data is pulled out as a multidimensional array, it needs to be flattened
contrast2R = contrast2R.flatten()#this argument takes the array defined above and redefines it as flattened
contrast3R = contrast3R.flatten()

contrast1K = pyfits.getdata('20050702.1702.HW.K.P.contrast.fits')
contrast2K = pyfits.getdata('20050702.1720.HW.K.P.contrast.fits') #This is the same process but for the calcium contrast
contrast3K = pyfits.getdata('20050702.1740.HW.K.P.contrast.fits')

contrast1K = contrast1K.flatten()
contrast2K = contrast2K.flatten()
contrast3K = contrast3K.flatten()


# In[48]:

f, axarr = plt.subplots(2, 1) #This part of the code takes the two histograms and puts them in the same image
plt.subplots_adjust(hspace = 0.55,wspace = 0.5)
figure = plt.gcf()

contrast1R = contrast1R[np.where(contrast1R > -0.05)]#This will clip off the pixels that are off the solar limb
contrast2R = contrast2R[np.where(contrast2R > -0.05)]#Without this, there is another bump in intensity. but according
contrast3R = contrast3R[np.where(contrast3R > -0.05)]#to the project this is just the pixels off the limb

contrast1R = contrast1R[np.where(contrast1R < 0.05)]#I also clipped higher values because there was nothing there and  
contrast2R = contrast2R[np.where(contrast2R < 0.05)]#this allows us to have a closer look at the data centered at 0 
contrast3R = contrast3R[np.where(contrast3R < 0.05)]

axarr[0].hist(contrast1R,bins=50,normed = 'True',alpha = 0.5,label='1702')#This begins the first histogram argument. I won't be
axarr[0].hist(contrast2R,bins=50,normed = 'True',alpha = 0.5,label='1720')#including the comp file because the normed = true statement
axarr[0].hist(contrast3R,bins=50,normed = 'True',alpha = 0.5,label='1740')#makes it a PDF so the computation is taken care of here.
axarr[0].set_title('Red Continuum PDFS') 
axarr[0].set_ylabel('Frequency')          
axarr[0].set_xlabel('Intensity')
axarr[0].legend()

contrast1K = contrast1K[np.where(contrast1K > -0.1)]#This is the same as the clipping above, but I had to clip different  
contrast2K = contrast2K[np.where(contrast2K > -0.1)] #sections because it has a different range
contrast3K = contrast3K[np.where(contrast3K > -0.1)] 

contrast1K = contrast1K[np.where(contrast1K < 0.3)]  
contrast2K = contrast2K[np.where(contrast2K < 0.3)] 
contrast3K = contrast3K[np.where(contrast3K < 0.3)] 

axarr[1].hist(contrast1K,bins=50,normed = 'True',alpha=0.5,label='1702')
axarr[1].hist(contrast2K,bins=50,normed = 'True',alpha=0.5,label='1720')
axarr[1].hist(contrast3K,bins=50,normed = 'True',alpha=0.5,label='1740')
axarr[1].set_title('Calcium PDFS') 
axarr[1].set_ylabel('Frequency')          
axarr[1].set_xlabel('Intensity')
axarr[1].legend()

figure.savefig('Wilson_project3Ci.png',format='png')
plt.show()


# In[ ]:




# In[ ]:



