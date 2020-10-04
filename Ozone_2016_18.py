Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
var collection = ee.ImageCollection('TOMS/MERGED')
  .select('ozone')
  .filterDate('2018-01-01', '2019-01-01');

var band_viz = {
  min: 100,
  max: 500,
  palette: ['1621A2', 'cyan', 'green', 'yellow', 'orange', 'red']
};
var table3 = ee.FeatureCollection('users/shahzeel999/India')
Export.image.toDrive({
image: collection,
description: 'Before_O3_2',
scale: 2000,
region: table3});
