
# coding: utf-8

# In[1]:

from astropy.io import fits as pyfits
import numpy as np
import matplotlib.pyplot as plt

contrast, header = pyfits.getdata('20050702.1702.HW.R.P.contrast.fits',header=True)

rdc, header = pyfits.getdata('20050702.1702.HW.R.P.rdc.fits',header=True)


# In[3]:

f, axarr = plt.subplots(2, 2) 
plt.subplots_adjust(hspace = 0.55,wspace = 0.5)
figure = plt.gcf()

axarr[0,0].imshow(contrast, cmap='gray') #shows the image for the contrast file
axarr[0,0].set_title('Red Continuum: Contrast') 
axarr[0,0].set_ylabel('Pixel Location')          
axarr[0,0].set_xlabel('Pixel Location')
axarr[0,0].invert_yaxis()

                                         
axarr[0,1].imshow(rdc, cmap='gray') 
axarr[0,1].set_title('Red Continuum: RDC') 
axarr[0,1].set_ylabel('Pixel Location')          
axarr[0,1].set_xlabel('Pixel Location')
axarr[0,1].invert_yaxis()

axarr[1,0].plot(contrast[1024]) #Plots the cut through the center of the image
axarr[1,0].set_title('Red Continuum: Contrast Slice') 
axarr[1,0].set_ylabel('Normalized Intensity')          
axarr[1,0].set_xlabel('Pixel Location')

axarr[1,1].plot(rdc[1024]) 
axarr[1,1].set_title('Red Continuum: RDC Slice') 
axarr[1,1].set_ylabel('Intensity (Photon Counts)')          
axarr[1,1].set_xlabel('Pixel Location')

figure.savefig('Wilson_project3Ai.png',format='png')
plt.show()


# In[ ]:




# In[ ]:



