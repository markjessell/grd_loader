# grd_loader 0.1   

Plugin to load a geosoft GRD format file as a temporary QGIS raster layer    
   
## Install   

Save repository to disk and zip resulting directory. Use QGIS Plugin Manager to load directly from resulting zip file.

### Usage   

Once the QGIS Plugin is installed, click on the ![grd_icon](icon.png) icon. Form here you can search for a grd format file and load it. If this GRD has an associated xml file you can then just click on the OK button to load the grid. If no XML is present, manually enter the EPSG code (e.g. 4326 = WGS 84 Lat/Long), then cick on the OK button    

### Credits    
Plugin construction-Mark Jessell using QGIS Plugin Builder Plugin    
grd parser- modified from Fatiando a Terra team code with help from Loop Project    