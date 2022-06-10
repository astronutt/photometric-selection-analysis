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
import tensorflow as tf
import random

filename = 'IRACClassifications.cat' #CHANGE FILE HERE

t = Table.read(filename, format='ascii')

ra = t['RA']
dec = t['Dec']
coords = numpy.zeros((len(ra),2))
ids = t['id']

hdul = astropy.io.fits.open("egs_ch1_lores_collage_pass2_resid.fits")
fn = get_pkg_data_filename('egs_ch1_lores_collage_pass2_resid.fits')
hdul.info()
f = fits.open(fn)
w = WCS(f[0].header)



data = hdul[0].data

indata = fits.getdata('egs_ch1_lores_collage_pass2_resid.fits')
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
                cutout = Cutout2D(data2, (cpx, cpy), size=margin, mode='partial', fill_value=0)
                hdu = fits.PrimaryHDU(cutout.data)
                save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/good_ch1/'
                file_name = "goodCh1_id_" + str(ids[ind2])
                completeName = os.path.join(save_path, file_name + ".fits")
                hdu.writeto(completeName, overwrite=True)
                pictures.append(cutout)
                quality.append(0)
            except NoOverlapError:
                print(ids[ind2])
        elif(t['badirac'][ind2] == 1):
            try:
                cutout = Cutout2D(data2, (cpx, cpy), size=margin, mode='partial', fill_value=0)
                hdu = fits.PrimaryHDU(cutout.data)
                save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/bad_ch1/'
                file_name = "badCh1_id_" + str(ids[ind2])
                completeName = os.path.join(save_path, file_name + ".fits")
                hdu.writeto(completeName, overwrite=True)
                pictures.append(cutout)
                quality.append(1)
            except NoOverlapError:
                print(ids[ind2])
    ind2+=1

pictures_test = np.array(random.sample(pictures, len(pictures)//5))
quality_test = np.array(random.sample(quality, len(quality)//5))

pictures = np.array(random.sample(pictures, int(len(pictures)*0.8)))
quality = np.array(random.sample(quality, int(len(quality)*0.8)))



'''
    filename = 'IRACClassifications.cat'  # CHANGE FILE HERE

    t = Table.read(filename, format='ascii')

    ra = t['RA']
    dec = t['Dec']
    coords = numpy.zeros((len(ra), 2))
    ids = t['id']

    hdul = astropy.io.fits.open("egs_ch1_lores_collage_pass2_resid.fits")
    fn = get_pkg_data_filename('egs_ch1_lores_collage_pass2_resid.fits')
    hdul.info()
    f = fits.open(fn)
    w = WCS(f[0].header)

    data = hdul[0].data

    indata = fits.getdata('egs_ch1_lores_collage_pass2_resid.fits')
    data2 = np.copy(indata)

    index = 0

    for i in ra:
        coords[index] = (w.wcs_world2pix([[ra[index], dec[index]]], 1))
        index += 1

    margin = int(10 / .6)

    ind2 = 0
    for i in ra:

        if (t['sample'][ind2] >= 5):
            cpx = round(coords[ind2, 0])
            cpy = round(coords[ind2, 1])

            if (t['badirac'][ind2] == 0):  # GOOD DATA
                try:
                    # cutout = Cutout2D(data2, (cpx, cpy), size=margin, mode='partial', fill_value=0)
                    cutout = Cutout2D(data2, (cpx, cpy), size=margin, mode='strict')
                    hdu = fits.PrimaryHDU(cutout.data)
                    save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/ch1_good_NE/'
                    file_name = "gCh1NE_id_" + str(ids[ind2])
                    completeName = os.path.join(save_path, file_name + ".fits")
                    hdu.writeto(completeName, overwrite=True)
                except NoOverlapError:
                    print(ids[ind2])
                except PartialOverlapError:
                    cutoutE = Cutout2D(data2, (cpx, cpy), size=margin, mode='partial', fill_value=0)
                    hdu = fits.PrimaryHDU(cutoutE.data)
                    save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/ch1_good_EDGE/'
                    file_name = "gCh1E_id_" + str(ids[ind2])
                    completeName = os.path.join(save_path, file_name + ".fits")
                    hdu.writeto(completeName, overwrite=True)
            elif (t['badirac'][ind2] == 1):  # BAD DATA
                try:
                    # %cutout = Cutout2D(data2, (cpx, cpy), size=margin, mode='partial', fill_value=0)
                    cutout = Cutout2D(data2, (cpx, cpy), size=margin, mode='strict')
                    hdu = fits.PrimaryHDU(cutout.data)
                    save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/ch1_bad_NE/'
                    file_name = "bCh1NE_id_" + str(ids[ind2])
                    completeName = os.path.join(save_path, file_name + ".fits")
                    hdu.writeto(completeName, overwrite=True)
                except NoOverlapError:
                    print(ids[ind2])
                except PartialOverlapError:
                    cutoutE = Cutout2D(data2, (cpx, cpy), size=margin, mode='partial', fill_value=0)
                    hdu = fits.PrimaryHDU(cutoutE.data)
                    save_path = 'C:/Users/sjbru/PycharmProjects/pythonProject/ch1_bad_EDGE/'
                    file_name = "bCh1E_id_" + str(ids[ind2])
                    completeName = os.path.join(save_path, file_name + ".fits")
                    hdu.writeto(completeName, overwrite=True)
        ind2 += 1
'''