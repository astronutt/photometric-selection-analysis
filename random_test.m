%set red exposure to 5000, green to 10000

%imaging('Max1.png') - imaging('test-dark2.png')
%imaging('min1.png') - imaging('test-dark2.png')
%imaging('min2.png') - imaging('test-dark2.png')

%imaging('rlp2-080.png') - imaging('rlp2dark.png')
%imaging('LPf-080.png') - imaging('LPfdark.png')

imaging('red_max.png') - imaging('red_max_min_dark.png')
imaging('red_min.png') - imaging('red_max_min_dark.png')