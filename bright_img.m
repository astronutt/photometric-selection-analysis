function brightness= bright_img(img1)

%calculate brightness
%brightness = mean2(img1(0:16, 0:16));
brightness = mean(img1, 'all');