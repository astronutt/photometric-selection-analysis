function brightness= imaging(img_name)

img1 = imread(img_name);

[y,x] = size(img1) ;
%imshow(img1) 
%hold on

%Mark Center 
center = round([x y]/2);
%plot(center(1),center(2),'*r')

%calculate brightness
brightness = mean2(img1(center(2)-10:center(2)+10, center(1)-10:center(1)+10));
