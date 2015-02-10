# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# select_TBD_in_city.py
# Created on: 2014-07-01 16:05:42.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
SLAMM_landuse = "SLAMM_landuse"

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(SLAMM_landuse, "NEW_SELECTION", "( \"SLAMM_LAND\" = 'TBD_COMM' AND \"IN_CITY\" = 'YES')")

mxd = arcpy.mapping.MapDocument('CURRENT')
df = arcpy.mapping.ListDataFrames(mxd, "Layers") [0]
#df.zoomToSelectedFeatures()
arcpy.RefreshActiveView()





