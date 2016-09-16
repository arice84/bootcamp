import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import skimage.io
#import scipy.stats
import bootcamp_utils as booU
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)
import skimage.exposure
import skimage.morphology
import skimage.filters

#load images
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

#show the pase image
# plt.imshow(phase_im, cmap=plt.cm.viridis)

#Plot the histogram of the phase image
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

#apply a threashold to image
thresh = 325
im_phase_thresh = phase_im < thresh
plt.close()

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)

#show the fluorecence image
with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

#slice out region with hot pixel
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)

#generate a structural element
selem = skimage.morphology.square(3)
cfp_filt = skimage.filters .median(cfp_im, selem)
with sns.axes_style('dark'):
    plt.imshow(cfp_filt[150:250, 450:550]/ cfp_im.max(), cmap=plt.cm.viridis)

# histogram of media filtered image
cfp_hist, cfp_bins = skimage.exposure.histogram(cfp_filt)
plt.close()
plt.plot(cfp_bins, cfp_hist)
plt.xlabel('pixel value')
plt.ylabel('counts')

# histogram of media filtered image
cfp_thresh = cfp_filt > 120
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)

#apply and otsu threashold
plt.close()
phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu = phase_im < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

with sns.axes_style('dark'):
    plt.figure()
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
    plt.title('phase otsu')

    plt.figure()
    plt.imshow(cfp_otsu, cmap=plt.cm.Greys_r)
    plt.title('cfp otsu')
