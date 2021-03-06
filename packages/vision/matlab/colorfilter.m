function A = colorfilter(IMG, ...
    channel1Low, channel1High, ...
    channel2Low, channel2High, ...
    channel3Low, channel3High)
%COLORFILTER Filters an image for the specified color ranges.
%   If given a HxWx3 image, this will filter that image for the
%   given color channels. This will work on any image in a color
%   space that has 3 channels. This will return a binary image
%   where 1's represent pixels that passed the filter, and 0's
%   represent those that didn't.
%
%   Ex. RGB, HSV, etc. NOT grayscale

% Check dimensions
size_ = size(IMG);
size_of_size = size(size_);
if size_of_size(2) ~= 3 || size_(3) ~= 3
    error(['IMG does not have valid dimensions. ',...
        'The image must be HxWx3.']);
end

% First statement is for no loop around
% Second is for loop around if the low channel is greater than the high
% channel
if channel1High >= channel1Low
    channel1Filter = (IMG(:,:,1) <= channel1High) & ...
        (IMG(:,:,1) >= channel1Low);
else
    channel1Filter = (IMG(:,:,1) <= channel1High) | ...
        (IMG(:,:,1) >= channel1Low);
end
if channel2High >= channel2Low
    channel2Filter = (IMG(:,:,2) <= channel2High) & ...
        (IMG(:,:,2) >= channel2Low);
else
    channel2Filter = (IMG(:,:,2) <= channel2High) | ...
        (IMG(:,:,2) >= channel2Low);
end
if channel3High >= channel3Low
    channel3Filter = (IMG(:,:,3) <= channel3High) & ...
        (IMG(:,:,3) >= channel3Low);
else
    channel3Filter = (IMG(:,:,3) <= channel3High) | ...
        (IMG(:,:,3) >= channel3Low);
end

A = channel1Filter & channel2Filter & channel3Filter;

end