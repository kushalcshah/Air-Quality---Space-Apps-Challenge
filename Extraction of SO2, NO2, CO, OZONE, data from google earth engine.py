Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
var collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_SO2')
.select('SO2_column_number_density')
.filterDate('2020-03-01', '2020-03-07');
var band_viz = {  
min: 0.0, 
max: 0.0005, 
palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red'] };

Map.addLayer(collection.mean(), band_viz, 'S5P SO2');

var roi = ee.FeatureCollection("users/kushalpg190490/india");
Map.addLayer(roi,{ }, 'India');
Export.image.toDrive({
 image: collection, 
 description: 'Before_SO2',
 scale: 2000, 
 region: roi  });
