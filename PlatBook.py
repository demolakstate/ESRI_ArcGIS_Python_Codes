#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      demolakstate
#
# Created:     29/05/2019
# Copyright:   (c) demolakstate 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Script to automate Plat Directory Plat Books and Wall Maps

# Import system modules
import os
import sys
import arcpy
sys.path.append("H:\\Python Scripts\\KM_Utility")
from KM_Utility import GetCountyDictionary, UpdateCountySoils, GetCoordSys

#arcpy.env.workspace = r"H:\Comanche\CM_Geodatabases\CM_Appraiser_ORION.gdb\Parcels_ORION"
#arcpy.env.workspace = r"H:\Comanche\CM_Geodatabases\CM_Appraiser_ORION.gdb"
#arcpy.env.workspace = arcpy.GetParameterAsText(0).strip()[:-13]
workspace = arcpy.GetParameterAsText(0).strip()[:-13]
arcpy.env.workspace = workspace
erase_features = arcpy.GetParameterAsText(1).strip()

# Set overwrite option
arcpy.env.overwriteOutput = True

featureClass = "Parcels_ORION"
featureLayer = "featurelayer"
#featureLayer_erased = "feature_erased"
featureClass_erased = os.path.join(workspace, "Parcels_ORION_erased")
#erase_features =





#where_clause = """'TU_GroupCo' NOT LIKE '00%'"""
#out_path = r'H:\_Tutorials\Output\out'
inputDialog_1 = arcpy.GetParameterAsText(0).strip()
ind = inputDialog_1.rfind("\\") #.rfind("\\") # return the index of the first \

inputDialog_1 = inputDialog_1[:ind]

ind = inputDialog_1.rfind("\\") #.rfind("\\") # return the index of the second \

inputDialog_1 = inputDialog_1[:ind]

arcpy.AddMessage("input dialog {0}".format(inputDialog_1))








# erase features
arcpy.Erase_analysis(featureClass, erase_features, featureClass_erased)






out_path = r'{0}'.format(inputDialog_1)

#where_clause = "(TU_GroupCo NOT LIKE '00%') AND ACRES >= 10 AND ACRES < 20"
where_clause = "ACRES >= 10 AND ACRES < 20"
#try:
#arcpy.MakeFeatureLayer_management(featureClass, featureLayer, ['PID', 'ACRES', 'PropertyNu', 'QuickRefID', 'PartNames', 'TU_GroupCo'])
arcpy.MakeFeatureLayer_management(featureClass_erased, featureLayer, where_clause)



# erase features
#arcpy.Erase_analysis(featureLayer, erase_features, featureLayer_erased, '#')











# Select only those whose 'TU_GroupCo' NOT LIKE '00%'
#arcpy.SelectLayerByAttribute_management(featureLayer, "SUBSET_CONSTRUCTION", "TU_GroupCo NOT LIKE '00%'")

# change working directory to out_path
os.chdir(out_path)


#county_dict = GetCountyDictionary("ABBRS")
#arcpy.AddMessage("county list {0}".format(county_dict))

#retrieve the county's abbrevations
def GetCountyNameAbbreviation(check):
    abbr = ''

##    if 'COMMANCHE' in check:
##        abbr = 'CM'
##
##    if 'CLAY' in check:
##        abbr = 'CY'

    county_dict = GetCountyDictionary("ABBRS")
    for county in county_dict:
        if county in check:
            abbr = county_dict[county]


    return abbr





l_inputDialog_1 = inputDialog_1.upper().split('\\')
#out_name = 'CM_Plat_Directory.gdb'
out_name = '{0}_Plat_Directory.gdb'.format(GetCountyNameAbbreviation(l_inputDialog_1))

out_folder_path = os.getcwd()         # get current working directory

# create the geodatabase file if it does not exist
if not os.path.exists(out_name):
    arcpy.CreateFileGDB_management(os.getcwd(), out_name)


#out_path = os.path.join(out_path, 'CO_Plat_Directory')


# change working directory to the created geodatabase
print "working directory", os.getcwd()
os.chdir(out_name)





### save the new feature layer
##
##arcpy.CreateFeatureClass_management(os.getcwd(), 'Parcels_ORION_plat')



#out_featureclass = os.path.join(out_path, "Parcels_ORION_New")

#print("working directory ", os.getcwd())

# add increment field to featureLayer
#arcpy.management.AddField(featureLayer, 'Increment', 'DOUBLE', None, 0)
arcpy.management.AddField(featureLayer, 'Increment', 'DOUBLE')
arcpy.management.AddField(featureLayer, 'Legend_Label', 'TEXT')
arcpy.management.AddField(featureLayer, 'TRS', 'TEXT')


#extract selected fields from feature class
#myFields = ['PID', 'ACRES', 'PropertyNu', 'QuickRefID', 'PartyNames', 'TU_GroupCo','Section', 'Township', 'Range', 'STR', 'TNP_RNG']
myFields = ['PID', 'ACRES', 'PropertyNu', 'QuickRefID', 'PartyNames', 'TU_GroupCo','Section', 'Township', 'Range', 'STR', 'TNP_RNG', 'Increment', 'Legend_Label', 'TRS']

#myFields = ['PropertyNu']

# create an empty field mapping object
mapS = arcpy.FieldMappings()
# for each field, create an individual field map, and add it to the field mapping object
for field in myFields :
    map = arcpy.FieldMap()
    map.addInputField(featureLayer, field)
    mapS.addFieldMap(map)




# field to update values on
#fields = ['TNP_RNG', 'Section', 'TRS', 'PartyNames', 'Increment', 'Legend_Label']
fields = ['TNP_RNG', 'Section', 'TRS', 'PartyNames', 'Increment', 'Legend_Label']



### Create update cursor for feature class
##with arcpy.da.UpdateCursor(featureLayer, fields) as cursor:
##    #counter = -10     # initialize counter to 1 for the first Increment value
##
##    unique_values = set(row[0] for row in cursor) # get unique values in 'TNP_RNG'
##
##    arcpy.AddMessage("unique_values {0}".format(unique_values))
##
##    # create a counter holding dictionary for each unique value
##    #counter = [-10 for unique_value in unique_values]
##    counter_dict = {unique_value : -10 for unique_value in unique_values}
##
##    arcpy.AddMessage("counter_dict {0}".format(counter_dict))
##
##
##    for row in cursor:
##        #row[2] = row[0] + '-' + row[1]
##
##        #for unique_value in unique_values:
##            #arcpy.AddMessage("unique_value {0}".format(unique_values))
##            #arcpy.AddMessage("unique_value..................")
##            #if u'{0}'.format(row[0]) == unique_value:
##            #if row[0] == '35S-21W':
##            #    row[3] = int(counter_dict.get(unique_value) + 1)
##            row[3] = 0
##
##
####        if row[0] == '06S-01E':
####            row[3] = counter
##
##
##        # Update the cursor with the updated list
##            cursor.updateRow(row)
##
####    for unique_value in unique_values:
####        for row in cursor:
####    ##        row[2] = row[0] + '-' + row[1]
####
####
####                arcpy.AddMessage("unique_value {0}".format(unique_value))
####                if u'{0}'.format(row[0]) == unique_value:
####                #if row[0] == '06S-04E':
####                    row[3] = int(counter_dict.get(unique_value) + 1)
####                    #row[3] = 0
####
####
####    ##        if row[0] == '06S-01E':
####    ##            row[3] = counter
####
####
####            # Update the cursor with the updated list
####                cursor.updateRow(row)
####            #counter = counter + 1        # update the counter value
##
##


with arcpy.da.UpdateCursor(featureLayer, fields) as cursor:

    global counter_dict

    unique_values = {row[0] for row in cursor} # get unique values in 'TNP_RNG'

    arcpy.AddMessage("unique_values {0}".format(unique_values))

    # create a counter holding dictionary for each unique value
    #counter = [-10 for unique_value in unique_values]
    counter_dict = {unique_value : 0 for unique_value in unique_values}

    arcpy.AddMessage("counter_dict {0}".format(counter_dict))

##    #arcpy.AddMessage("Testing {0}".format(counter_dict['20S-30']))
##    for row in cursor:
##
##        if  row[0] == "06S-04E":
##
##            #counter_dict['06S-04E'] = counter_dict['06S-04E'] + 1
##            #row[3] = counter_dict['06S-04E']
##            row[3] = 2
##
##
####        if  not counter_dict.get('{0}'.format(row[0])) is None:
####
####            counter_dict['{0}'.format(row[0])] = counter_dict['{0}'.format(row[0])] + 1
####            row[3] = counter_dict['{0}'.format(row[0])]
##
##
##
##
##            cursor.updateRow(row)



with arcpy.da.UpdateCursor(featureLayer, fields) as cursor:


    for row in cursor:

        #if  row[0] == "06S-04E":
        if counter_dict[row[0]] is not None:
            counter_dict[row[0]] = counter_dict[row[0]] + 1
            row[4] = counter_dict[row[0]]

            #counter_dict['06S-04E'] = counter_dict['06S-04E'] + 1
            #row[3] = counter_dict['06S-04E']
            #row[3] = 2


        cursor.updateRow(row)



with arcpy.da.UpdateCursor(featureLayer, fields) as cursor:
   # counter = 1     # initialize counter to 1 for the first Increment value



    for row in cursor:
        row[2] = str(row[0]) + '-' + str(row[1])
        #row[5] = str(row[4]) + '-' + str(row[3])


##        if row[0] == "27S-33W":
##            row[3] = counter
##            counter = counter + 1        # update the counter value



        # Update the cursor with the updated list
        cursor.updateRow(row)



with arcpy.da.UpdateCursor(featureLayer, fields) as cursor:
   # counter = 1     # initialize counter to 1 for the first Increment value



    for row in cursor:
        #row[2] = str(row[0]) + '-' + str(row[1])
        if row[4] is not None and row[3] is not None:
            row[5] = str(int(row[4])) + '-' + str(row[3][:40])       # first 40 characters from PartyNames


##        if row[0] == "27S-33W":
##            row[3] = counter
##            counter = counter + 1        # update the counter value



        # Update the cursor with the updated list
        cursor.updateRow(row)





# copy the feature class using the fields you want
arcpy.FeatureClassToFeatureClass_conversion(featureLayer, os.getcwd(), "Parcels_ORION_plat", "#", mapS)

arcpy.AddMessage("plat....{0}".format(os.getcwd()))

#arcpy.env.workspace = os.getcwd()

# Feature to point
arcpy.FeatureToPoint_management("Parcels_ORION_plat", os.path.join(os.getcwd(), "Parcels_ORION_point"), 'INSIDE')

print("working_directory ", os.getcwd())








# Get unique values from TRS field of Parcels_Orion_plat
fc = os.path.join(os.getcwd(), "Parcels_ORION_plat")
field_TRS = ['TRS']

values = [row[0] for row in arcpy.da.SearchCursor(fc, field_TRS)]
uniqueValues = set(values)

arcpy.AddMessage("TRS {0}".format(uniqueValues))

in_features = os.path.join(os.getcwd(), "Parcels_ORION_plat")
#out_path = r'H:\Comanche\CM_Geodatabases\CM_Plat_Directory.gdb\Plat_Book'




# create the out path
arcpy.AddMessage("out path directory {0}".format(os.getcwd()))

out_path = os.getcwd()
#index_out_path = out_path.rfind('\\')
#out_path = out_path[:index_out_path]

os.chdir(out_path)

plat_book = 'Plat_Book'

arcpy.AddMessage("out path directory............... {0}".format(os.getcwd()))

spatial_reference = GetCoordSys(GetCountyNameAbbreviation(l_inputDialog_1))

if not os.path.exists(plat_book):
    #arcpy.CreateFeatureDataset_management(out_path, plat_book) # projection file
    arcpy.CreateFeatureDataset_management(out_path, plat_book, spatial_reference) # projection file















    #arcpy.CreateFileGDB_management(out_path, plat_book)
    arcpy.AddMessage("Testing ..")


#arcpy.AddMessage("list directories {0}".format(os.listdir(out_path)))
#os.chdir(plat_book)
change_path = os.path.join(os.getcwd(), "Plat_Book")
#os.chdir(change_path)

arcpy.AddMessage("changed path {0}".format(change_path))




#out_path = r'H:\_Tutorials\Output\out'
out_path = os.getcwd()

arcpy.AddMessage("out path {0}".format(out_path))
#out_path = os.path.join(os.getcwd(), "Plat_Book")


#out_path = r'H:\_Tutorials\Output\out'


#where_clause_2 ="TRS = "
fieldname = 'TRS'


for uniqueValue in uniqueValues:
    if uniqueValue is not None:
        name = uniqueValue.strip().replace('-', '_').replace(' ', '')
        #arcpy.FeatureClassToFeatureClass_conversion(in_features, out_path,'T_{0}'.format(name), """{0} = '{1}'""".format(arcpy.AddFieldDelimiters(in_features, fieldname), uniqueValue))
        arcpy.FeatureClassToFeatureClass_conversion(in_features, out_path,'T_{0}'.format(name), """{0} = '{1}'""".format(arcpy.AddFieldDelimiters(in_features, fieldname), uniqueValue))
        #arcpy.FeatureClassToFeatureClass_conversion(in_features, out_path,'T_{0}'.format(name))
        #arcpy.FeatureClassToFeatureClass_conversion(in_features, out_path,'T_{0}'.format(name), """{0} = '21S-05E'""".format(arcpy.AddFieldDelimiters(in_features, fieldname)))
        arcpy.FeatureClassToGeodatabase_conversion('T_{0}'.format(name), change_path )
        #arcpy.Rename_management(os.path.join(change_path, 'T_{0}'.format(name)), 'T_{0}'.format(name)[:-2] )



# Clean up

arcpy.AddMessage('current location {0}'.format(os.getcwd()))
#dirs = os.listdir(os.getcwd())    # list files and directories


# set workspace to clean up
arcpy.env.workspace = os.getcwd()


featureclasses = arcpy.ListFeatureClasses('T*')             # list all the feature classes starting with letter T
for fc in featureclasses:
    arcpy.AddMessage("To delete {0}".format(fc))
    arcpy.Delete_management(fc)


##for file in dirs:
##    #if file.startswith('T'):
##       arcpy.AddMessage('files {0}'.format(file))











# convert feature layer to feature class and save
#arcpy.CopyFeatures_management(featureLayer, out_featureclass)

##except:
##    print(arcpy.GetMessages())


