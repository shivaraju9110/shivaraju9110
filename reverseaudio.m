inputFile = '/home/rguktrkvalley/Documents/IMG-20220801-WA0003.jpg';

imageData = imread(inputFile);
redChannel = imageData(:,:,1);
greenChannel = imageData(:,:,2);
blueChannel = imageData(:,:,3);

redOutputFile = 'red_channel.csv';
greenOutputFile = 'green_channel.csv';
blueOutputFile = 'blue_channel.csv';
csvwrite(redOutputFile, redChannel);
csvwrite(greenOutputFile, greenChannel);
csvwrite(blueOutputFile, blueChannel);

disp('Red, green, and blue channels saved to separate CSV files successfully!');