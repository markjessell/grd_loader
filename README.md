# grd_loader 0.1   

Plugin to load a Geosoft(c) GRD format file as a temporary QGIS raster layer    
   
## Install   

Save repository to disk as a zip file. Use QGIS Plugin Manager to load directly from zip file.

### Usage   

Once the QGIS Plugin is installed, click on the ![grd_icon](icon.png) icon from the Plugins Toolbar . From here you can search for a GRD format file and load it as a raster grid. If this GRD has an associated xml file you can then just click on the OK button to load the grid. If no XML is present, manually enter the numeric EPSG code (e.g. 4326 = WGS 84 Lat/Long), then cick on the OK button    

### Credits    
Plugin construction-Mark Jessell using QGIS Plugin Builder Plugin    
GRD parser- modified from Fatiando a Terra code with help from Loop Project    