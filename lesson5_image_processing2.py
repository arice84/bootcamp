import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import scipy.stats
#import bootcamp_utils as booU
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)
sns.set_style('dark')

import skimage.io
import skimage.segmentation
import skimage.measure
import skimage.filters

#load images
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
#show image
plt.imshow(phase_im, cmap=plt.cm.viridis)

im_blur = skimage.filters.gaussian(phase_im, 50.0)

#show te bulurred image
plt.imshow(im_blur, cmap=plt.cm.viridis)

#convert our phase image to a float
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

#show both
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('orignianl')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

#apply otsu threashold
plt.close('all')
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh
plt.imshow(seg, cmap=plt.cm.Greys_r)

# label bactera
seg_lab , num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close('all')
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

# compute region properties and extract area of each object (ie cell)
ip_dist = 0.063 #µm per pixel
props = skimage.measure.regionprops(seg_lab)

# get areas an an array
areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab) > 0
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
