import astropy
from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import Table
import numpy as np
from astropy.utils.data import get_pkg_data_filename

#fits_image_filename = fits.util.get_testdata_filepath('test0.fits')
#fits_image_filename = astropy.io.fits.open("lores.fits")

t = Table.read('EGS_candidates_all.cat', format='ascii')

hdul = astropy.io.fits.open("egs_ch1_lores_collage_pass2_resid.fits")
fn = get_pkg_data_filename('egs_ch1_lores_collage_pass2_resid.fits')
hdul.info()
f = fits.open(fn)
w = WCS(f[0].header)

data = hdul[0].data

x = 215.1384124756
y = 52.9991989136

print("Original WCS coords:",x,y)

coords = w.wcs_world2pix([[x,y]], 1)

print("Converted to pixels: ", coords)

check = w.wcs_pix2world([[coords[0,0], coords[0,1]]], 1)
print("Converted back: ", check)

marginX = int(10/0.6)
marginY = int(10/0.6)

cpx = round(coords[0,0])
cpy = round(coords[0,1])

print(cpx - marginX, cpx + marginX, cpy - marginY, cpy + marginY)

n = data[cpy - marginY : cpy + marginY, cpx - marginX : cpx + marginX]
#n = data[ cpx - marginX : cpx + marginX, cpy - marginY : cpy + marginY]

hdu = fits.PrimaryHDU(n)

#name = 'stamp1.fits'

#hdu.writeto(name)
#print(data[275, 1800])