function brightness= stdev(img1)

%calculate brightness
%brightness = mean2(img1(0:16, 0:16));
brightness = std(img1, 0, 'all');