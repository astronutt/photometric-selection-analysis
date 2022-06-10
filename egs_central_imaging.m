function brightness= egs_central_imaging(img1)

J = imadjust(img1);
%figure
%imshow(J)
%imshow(img1)
%hold on

%Mark Center 
%center = round([16 16]/2);
center = [9 9];
%plot(center(1),center(2),'*r')

%calculate brightness
brightness = mean2(img1(center(2)-2:center(2)+2, center(1)-2:center(1)+2));