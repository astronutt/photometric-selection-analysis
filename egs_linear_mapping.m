function v_out = egs_linear_mapping(v_in, range)
% function for linear mapping between two ranges
% inputs:
% v_in: the input vector you want to map, range [min(vin),max(vin)]
% range: the range of the resulting vector
% output:
% vout: the resulting vector in range rout
% usage:
% >> v1 = linspace(-2,9,100);
% >> v2 = linmap(v1,[-5,5]);
%
a = range(3); %min
b = range(4); %max
c = range(1); %min
d = range(2); %max
v_out = ((c+d) + (d-c)*((2*v_in - (a+b))/(b-a)))/2;
end