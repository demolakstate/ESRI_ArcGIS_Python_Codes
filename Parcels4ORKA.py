#------------------------------------------------------------------
# Parcels for DASC ORKA creation tool
# Created by Chris Swanson 07/11/2017
# Edited by Jason Balluch 09/13/2017
# Edited by Jason Balluch 11/29/2017
# Edited by Jason Balluch 1/29/2018
#------------------------------------------------------------------


#To call from command line use the following command:
#H:\>C:\Python27\ArcGIS10.5\python.exe "H:\Python Scripts\DASC_ORKA_Export Scripts\Parcels4ORKA.py"

#import module
import arcpy, os,  ftplib
from time import strftime
import os.path
import shutil

from zipfile import ZipFile 




#Set date variable for output path
Date = strftime("%Y%m%#d")

#County Variables
Chase =      "H:\\Chase\\CS_Geodatabases\\CS_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Chautauqua = "H:\\Chautauqua\\CQ_Geodatabases\\CQ_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Clark =      "H:\\Clark\\CA_Geodatabases\\CA_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Clay =       "H:\\Clay\\CY_Geodatabases\\CY_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Comanche =   "H:\\Comanche\\CM_Geodatabases\\CM_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Elk =        "H:\\Elk\\EK_Geodatabases\\EK_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Grant =      "H:\\Grant\\GT_Geodatabases\\GT_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Gray =       "H:\\Gray\\GY_Geodatabases\\GY_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Harper =     "H:\\Harper\\HP_Geodatabases\\HP_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Haskell =    "H:\\Haskell\\HS_Geodatabases\\HS_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Hodgeman =   "H:\\Hodgeman\\HG_Geodatabases\\HG_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Lane =       "H:\\Lane\\LE_Geodatabases\\LE_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Logan =      "H:\\Logan\\LG_Geodatabases\\LG_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Marshall =   "H:\\Marshall\\MS_Geodatabases\\MS_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Meade =      "H:\\meade\\ME_Geodatabases\\ME_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Ness =       "H:\\Ness\\NS_Geodatabases\\NS_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Ottawa =     "H:\\Ottawa\\OT_Geodatabases\\OT_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Rice =       "H:\\Rice\\RC_Geodatabases\\RC_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Rush =       "H:\\Rush\\RH_Geodatabases\\RH_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Scott =      "H:\\Scott\\SC_Geodatabases\\SC_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Sherman =    "H:\\Sherman\\SH_Geodatabases\\SH_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Smith =      "H:\\Smith\\SM_Geodatabases\\SM_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Stanton =    "H:\\Stanton\\ST_Geodatabases\\ST_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Trego =      "H:\\Trego\\TR_Geodatabases\\TR_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Wallace =    "H:\\Wallace\\WA_Geodatabases\\WA_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Washington = "H:\\Washington\\WS_Geodatabases\\WS_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
Wichita =    "H:\\Wichita\\WH_Geodatabases\\WH_Appraiser_Parcels.gdb\\Land_Ownership\\Parcel_Boundaries"
out_path =   "R:\\DASC_ORKA\\" + Date

#create output path directory
if not os.path.exists(out_path):
	os.makedirs(out_path)
else:
	shutil.rmtree(out_path)
	os.makedirs(out_path)

if os.path.exists(out_path):
	
	
	arcpy.AddMessage("exporting Chase Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Chase, out_path, "ChaseCoKS_Parcels.shp")
	arcpy.AddMessage("Chase Parcels for ORKA complete")
		
	arcpy.AddMessage("exporting Chautauqua Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Chautauqua, out_path, "ChautauquaCoKS_Parcels.shp")
	arcpy.AddMessage("Chautauqua Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Clark Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Clark, out_path, "ClarkCoKS_Parcels.shp")
	arcpy.AddMessage("Clark Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Clay Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Clay, out_path, "ClayCoKS_Parcels.shp")
	arcpy.AddMessage("Clay Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Comanche Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Comanche, out_path, "ComancheCoKS_Parcels.shp")
	arcpy.AddMessage("Comanche Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Elk Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Elk, out_path, "ElkCoKS_Parcels.shp")
	arcpy.AddMessage("Elk Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Grant Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Grant, out_path, "GrantCoKS_Parcels.shp")
	arcpy.AddMessage("Grant Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Gray Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Gray, out_path, "GrayCoKS_Parcels.shp")
	arcpy.AddMessage("Gray Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Harper Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Harper, out_path, "HarperCoKS_Parcels.shp")
	arcpy.AddMessage("Harper Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Haskell Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Haskell, out_path, "HaskellCoKS_Parcels.shp")
	arcpy.AddMessage("Haskell Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Hodgeman Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Hodgeman, out_path, "HodgemanCoKS_Parcels.shp")
	arcpy.AddMessage("Hodgeman Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Lane Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Lane, out_path, "LaneCoKS_Parcels.shp")
	arcpy.AddMessage("Lane Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Logan Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Logan, out_path, "LoganCoKS_Parcels.shp")
	arcpy.AddMessage("Logan Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Marshall Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Marshall, out_path, "MarshallCoKS_Parcels.shp")
	arcpy.AddMessage("Marshall Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Meade Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Meade, out_path, "MeadeCoKS_Parcels.shp")
	arcpy.AddMessage("Meade Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Ness Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Ness, out_path, "NessCoKS_Parcels.shp")
	arcpy.AddMessage("Ness Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Ottawa Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Ottawa, out_path, "OttawaCoKS_Parcels.shp")
	arcpy.AddMessage("Ottawa Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Rice Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Rice, out_path, "RiceCoKS_Parcels.shp")
	arcpy.AddMessage("Rice Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Rush Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Rush, out_path, "RushCoKS_Parcels.shp")
	arcpy.AddMessage("Rush Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Scott Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Scott, out_path, "ScottCoKS_Parcels.shp")
	arcpy.AddMessage("Scott Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Sherman Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Sherman, out_path, "ShermanCoKS_Parcels.shp")
	arcpy.AddMessage("Sherman Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Smith Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Smith, out_path, "SmithCoKS_Parcels.shp")
	arcpy.AddMessage("Smith Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Stanton Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Stanton, out_path, "StantonCoKS_Parcels.shp")
	arcpy.AddMessage("Stanton Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Trego Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Trego, out_path, "TregoCoKS_Parcels.shp")
	arcpy.AddMessage("Trego Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Wallace Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Wallace, out_path, "WallaceCoKS_Parcels.shp")
	arcpy.AddMessage("Wallace Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Washington Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Washington, out_path, "WashingtonCoKS_Parcels.shp")
	arcpy.AddMessage("Washington Parcels for ORKA complete")
	
	arcpy.AddMessage("exporting Wichita Parcels for ORKA")
	arcpy.FeatureClassToFeatureClass_conversion (Wichita, out_path, "WichitaCoKS_Parcels.shp")
	arcpy.AddMessage("Wichita Parcels for ORKA complete")
else:
	arcpy.AddMessage("The output path does not exist")





# code to upload file to kansasgis.org via FTP
os.chdir("R:\\DASC_ORKA\\{0}".format(Date))	# change working directory
#arcpy.AddMessage('Working directory... {0}' os.getcwd())

#zip(Date) # zip the created folder

#shutil.make_archive(Date, 'zip', Date)  	# zip folder

files = os.listdir('.')	 # list files in the directory

#with ftplib.FTP('backup.kansasgis.org') as ftp:
ftp = ftplib.FTP('backup.kansasgis.org')




ftp.login('KIMBLE', passwd='BaqadusBaz865') 
#if not os.path.exists(Date):
ftp.mkd('{0}_8'.format(Date)) # make directory on the remote server

ftp.cwd('{0}_8'.format(Date)) # change directory

#filename = '{0}.zip'.format(Date)



#myzip = ZipFile(filename)

for filename in files:
	arcpy.AddMessage('file ..{0}'.format(filename))
	#ftp.storbinary(Date + '/' + filename, open(filename))
	ftp.storbinary('_%s' % filename, open(filename, 'rb'))


#ftp.storbinary('Date.zip', myzip)

#myzip.close()

ftp.dir()
ftp.quit()
arcpy.AddMessage('done!')
print('Good bye')















#found on the internets-edit to work with FTP uploads for ATCI and T.R.
#import os
#import upload
#import download
#import zipfile
#import ConfigParser
#import ftputil
#
#def main():
#
#    #create a folder Temp on d drive for later use
#    path = r'C:\Temp'
#    os.mkdir(path)
#
#    #parse all the  values at config.ini file
#    config = ConfigParser.ConfigParser()
#    config.readfp(open('config.ini'))
#    server = config.get('main', 'Server')
#    username = config.get('main', 'Username')
#    password = config.get('main', 'Password')
#    uploads = config.get('main', 'Upload folder')
#    downloads = config.get('main', 'Download folder') 
#
#    #connect to ftp
#    ftp = ftputil.FTPHost(server, username, password)
#
#    dirlist = ftp.listdir(downloads)
#
#    for list in dirlist:
#        ftp.chdir(downloads)
#        target = os.path.join(path, list)
#        ftp.download(list, target)
#
#
#    #########################################################
#    #   THis section is where algo fails but the program run#
#    ########################################################
#
#    #zipping files
#    absolute_path = r'D:\Temp'
#    dirlist = os.listdir(absolute_path)
#    filepath = r'D:\Temp\project2.zip'
#    for list in dirlist:
#        get_file = os.path.join(absolute_path, list)
#        zip_name = zipfile.ZipFile(filepath, 'w')
#        zip_name.write(get_file, 'Project2b\\' + list)
#