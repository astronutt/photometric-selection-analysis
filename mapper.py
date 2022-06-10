import astropy
import numpy
from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import Table
import numpy as np
import os.path
from astropy.utils.data import get_pkg_data_filename
from astropy.nddata import Cutout2D
from astropy.nddata.utils import NoOverlapError

from matplotlib import image
from matplotlib import pyplot as plt
import tensorflow as tf
import random

PICCYWICCY = image.imread('ch1.jpeg')

filename = 'IRACClassifications.cat' #CHANGE FILE HERE

t = Table.read(filename, format='ascii')

ra = t['RA']
dec = t['Dec']
coords = numpy.zeros((len(ra),2))
ids = t['id']

hdul = astropy.io.fits.open('egs_ch2_lores_collage_pass2_resid.fits')
fn = get_pkg_data_filename('egs_ch2_lores_collage_pass2_resid.fits')
hdul.info()
f = fits.open(fn)
w = WCS(f[0].header)



data = hdul[0].data

indata = fits.getdata('egs_ch2_lores_collage_pass2_resid.fits')
data2 = np.copy(indata)

index = 0

for i in ra:
    coords[index] = (w.wcs_world2pix([[ra[index],dec[index]]], 1))
    index+=1

margin = int(10/.6)

ind2 = 0

pictures = []
quality = []

for i in ra:

    if(t['sample'][ind2] >= 5):
        cpx = round(coords[ind2, 0])
        cpy = round(coords[ind2, 1])

        if(t['badirac'][ind2] == 0):
            try:
                plt.plot(cpx, cpy, marker='^', color="blue", alpha=0.4)
                #hdu = fits.PrimaryHDU(cutout.data)
                #save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/good_ch1/'
                #file_name = "goodCh1_id_" + str(ids[ind2])
                #completeName = os.path.join(save_path, file_name + ".fits")
                #hdu.writeto(completeName, overwrite=True)
                #pictures.append(cutout)
                #quality.append(0)
            except NoOverlapError:
                print(ids[ind2])
        elif(t['badirac'][ind2] == 1):
            try:
                plt.plot(cpx, cpy, marker='^', color="red", alpha=0.4)
                #hdu = fits.PrimaryHDU(cutout.data)
                #save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/bad_ch1/'
                #file_name = "badCh1_id_" + str(ids[ind2])
                #completeName = os.path.join(save_path, file_name + ".fits")
                #hdu.writeto(completeName, overwrite=True)
                #pictures.append(cutout)
                #quality.append(1)
            except NoOverlapError:
                print(ids[ind2])
    ind2+=1

plt.imshow(PICCYWICCY)
plt.show()