format long

D = dir('bad_ch2/*.fits');

egs_cbright = zeros([length(D) 1]);
egs_brightness = zeros([length(D) 1]);
egs_stdev = zeros([length(D) 1]);
egs_stdev_weighted = zeros([length(D) 1]);
ccf = zeros([length(D) 1]);
bmax = zeros([length(D) 1]);
bmin = zeros([length(D) 1]);
bvar = zeros([length(D) 1]);

for i = 1:1:length(D)
    filename = D(i).name;
    imageData = fitsread(filename,'primary');
    
    J = medfilt2(imageData);

    maxB = max(imageData(:));
    minB = min(imageData(:));

    range = [0 1 minB maxB];

    new_img_data = egs_linear_mapping(imageData, range); %linear mapping of vector

    %imshow(new_img_data)
    
    inum = num2str(i);
    group = 'badc2';
    png = '.png';
    pngname = [inum group png];
    
    %imwrite(new_img_data, pngname);
    

    egs_cbright(i) = egs_central_imaging(new_img_data); %run stats function
    egs_brightness(i) = bright_img(new_img_data);
    egs_stdev(i) = stdev(new_img_data);
    egs_stdev_weighted(i) = std(new_img_data, 1, 'all');
    ccf(i) = corr2(imageData, J);
    bmax(i) = max(new_img_data, [], 'all');
    bmin(i) = min(new_img_data, [], 'all');
    bvar(i) = var(new_img_data, [], 'all');
end

x = zeros([length(D) 1]);
for z = 1:1:length(D)
    x(z) = z;
end

figure(1)
scatter(x, egs_cbright, 'r')
title("Brightness of Central 9 Pixels (bad IRAC)");
xlabel("Source #");
ylabel("Brightness");
% 
figure(2)
scatter(x, egs_brightness, 'r')
title("Brightness of Whole Image (bad IRAC)");
xlabel("Source #");
ylabel("Brightness");

figure(3)
scatter(x, egs_stdev, 'r')
title("Standard Devation Within Source (bad IRAC)");
xlabel("Source #");
ylabel("Standard Deviation");

figure(4)
scatter(x, egs_stdev_weighted, 'r')
title("Standard Devation: Vector Weighted (bad IRAC)");
xlabel("Source #");
ylabel("Std. Dev.");

figure(5)
scatter(x, ccf, 'r')
title("Correllation Coefficient (bad IRAC)");
xlabel("Source #");
ylabel("Coeff.");

figure(6)
scatter(x, bmax, 'r')
title("Maximum Value (bad IRAC)");
xlabel("Source #");
ylabel("Brightness");

figure(7)
scatter(x, bmin, 'r')
title("Minimum Value (bad IRAC)");
xlabel("Source #");
ylabel("Brightness");

figure(6)
scatter(x, bvar, 'r')
title("Variance (bad IRAC)");
xlabel("Source #");
ylabel("Variance");


    %imwrite(new_img_data,'egs_id_70849.png'); %convert to png

    %new_img = imread('egs_id_70849.png');

    %new_img1 = imrotate(new_img,180); %rotate and flip
    %new_img2= fliplr(new_img1);

%range_back = [minB maxB 0 1];

%img_back = egs_linear_mapping(new_img_data, range_back); %linear mapping of vector

%egs_central_imaging(img_back)

%egs_central_imaging(imageData)