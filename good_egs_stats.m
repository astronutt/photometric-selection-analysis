format long

D = dir('good_ch2/*.fits');

egs_gcbright = zeros([length(D) 1]);
egs_gbrightness = zeros([length(D) 1]);
egs_gstdev = zeros([length(D) 1]);
egs_gstdev_weighted = zeros([length(D) 1]);
gccf = zeros([length(D) 1]);
gmax = zeros([length(D) 1]);
gmin = zeros([length(D) 1]);
gvar = zeros([length(D) 1]);

for i = 1:1:length(D)
    filename = D(i).name;
    imageData = fitsread(filename,'primary');
    
    J = medfilt2(imageData);

    maxB = max(imageData(:));
    minB = min(imageData(:));

    range = [0 1 minB maxB];

    new_img_data = egs_linear_mapping(imageData, range); %linear mapping of vector

    %imshow(new_img_data)

    egs_gcbright(i) = egs_central_imaging(new_img_data); %run stats function
    egs_gbrightness(i) = bright_img(new_img_data);
    egs_gstdev(i) = stdev(new_img_data);
    egs_gstdev_weighted(i) = std(new_img_data, 1, 'all');
    gccf(i) = corr2(imageData, J);
    gmax(i) = max(new_img_data, [], 'all');
    gmin(i) = min(new_img_data, [], 'all');
    gvar(i) = var(new_img_data, [], 'all');
end

x = zeros([length(D) 1]);
for z = 1:1:length(D)
    x(z) = z;
end

figure(1)
scatter(x, egs_gcbright)
title("Brightness of Central 9 Pixels (good IRAC)");
xlabel("Source #");
ylabel("Brightness");

figure(2)
scatter(x, egs_gbrightness)
title("Brightness of Whole Image (good IRAC)");
xlabel("Source #");
ylabel("Brightness");

figure(3)
scatter(x, egs_gstdev)
title("Standard Devation Within Source (good IRAC)");
xlabel("Source #");
ylabel("Standard Deviation");

figure(4)
scatter(x, egs_gstdev_weighted)
title("Standard Devation: Vector Weighted (good IRAC)");
xlabel("Source #");
ylabel("Std. Dev.");

figure(5)
scatter(x, gccf)
title("Correllation Coefficient");
xlabel("Source #");
ylabel("Coeff.");

figure(6)
scatter(x, gvar)
title("Variance (good IRAC)");
xlabel("Source #");
ylabel("Variance");