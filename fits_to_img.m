filename='egs_ch1_lores_collage_pass2_resid.fits';
imageData = fitsread(filename,'primary');

maxB = max(imageData(:));
minB = min(imageData(:));
range = [0 1 minB maxB];
new_img_data = egs_linear_mapping(imageData, range);

imshow(new_img_data)