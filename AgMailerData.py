#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      demolakstate
#
# Created:     22/05/2019
# Copyright:   (c) demolakstate 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import system modules
import os
import sys
import arcpy
sys.path.append("H:\\Python Scripts\\KM_Utility")
from KM_Utility import GetCountyDictionary

#allow for overwrites
arcpy.env.overwriteOutput = True

# get inputs from user
inputDialog_1 = arcpy.GetParameterAsText(0).strip()
outputPath = inputDialog_1  # output folder

l_outputPath = os.path.split(outputPath)
l_outputPath = l_outputPath[0]  # get the first part of the tuple


ind = l_outputPath.rfind("\\")      # index of the last "\"
l_outputPath = l_outputPath[:ind]


os.chdir(l_outputPath)      # change directory to output location


#retrieve the county's abbrevations
def GetCountyNameAbbreviation(check):
    abbr = ''
    county_dict = GetCountyDictionary("ABBRS")
    for county in county_dict:
        if county in check:
            abbr = county_dict[county]


    return abbr


# Set local variables
out_folder_path = os.getcwd()         # get current working directory
l_inputDialog_1 = inputDialog_1.upper().split('\\')
out_name = "{0}_Appraiser_AguseQuestionnaire.gdb".format(GetCountyNameAbbreviation(l_inputDialog_1))


if not os.path.exists(out_name):
    arcpy.CreateFileGDB_management(out_folder_path, out_name)

os.chdir(out_name)             # change directory

working_directory = os.getcwd()         # get current working directory


inputDialog_1 = inputDialog_1[:-13]     # remove the last 13 characters, this correspond to "Parcels_ORION" part

inputDialog_2 = arcpy.GetParameterAsText(1).strip()
num = inputDialog_2[9:]
num = int(num)

# extract comparison operator
comp = inputDialog_2[6:8]

if comp == "==":
    comp = '='


arcpy.env.workspace = r"{0}".format(inputDialog_1)

featureClass = "Parcels_ORION"
featureLayer = "FeatureLayer"

arcpy.MakeFeatureLayer_management(featureClass, featureLayer, """ ("PropTypeCo" = 'A' or "PropTypeCo" = 'F') and "ACRES" {0} {1} """.format(comp, num))
print featureLayer

# list of fields in feature layer
fields = "*"

with arcpy.da.SearchCursor(featureLayer, fields) as sc:
    for row in sc:
        print row[25] + " " + str(row[3])


out_featureclass = os.path.join(working_directory, "Parcels_ORION_New")

# conver feature layer to feature class and save
arcpy.CopyFeatures_management(featureLayer, out_featureclass)

arcpy.AddMessage("OUTPUT saved to {0}".format(out_featureclass))