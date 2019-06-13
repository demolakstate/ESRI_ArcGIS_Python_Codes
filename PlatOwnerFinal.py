#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      demolakstate
#
# Created:     07/06/2019
# Copyright:   (c) demolakstate 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy, textwrap, os
from operator import itemgetter


import webbrowser
import math

from createPDF import generatePDF


sys.path.append("H:\\Python Scripts\\KM_Utility")
from KM_Utility import GetCountyDictionary



# clean up
if os.path.exists(os.path.join(os.getcwd(), 'temp.pdf')):
    os.remove('temp.pdf')


workspace = arcpy.GetParameterAsText(0)
inputDialog_1 = workspace               #for county name check

pdfPath = arcpy.GetParameterAsText(1)

# eliminate the feature class
ind = workspace.rfind('\\')
workspace =  workspace[:ind]

#arcpy.env.workspace = r'H:\Clark\CA_Geodatabases\CA_Appraiser_ORION.gdb'
arcpy.env.workspace = workspace

featureClass = 'Parcels_ORION_erased'

fields = ['PartyNames', 'Section', 'TNP_RNG', 'ACRES']

#lines = [row for row in sorted(arcpy.da.SearchCursor(featureClass, fields), key=lambda column: (column[0], column[2], column[1])  ) if row[0] is not None]  # sort by PartyNames
lines = [row for row in sorted(arcpy.da.SearchCursor(featureClass, fields), key=itemgetter(0,2,1)  ) if row[0] is not None]  # sort by PartyNames


arcpy.AddMessage(lines)

# number of lines on a page
n = 84

# get number of pages
pages = len(lines)/(n * 3.0)

arcpy.AddMessage("Number of pages 1st = {0}".format(pages))
pages = math.ceil(pages)

print("Number of pages", pages)
arcpy.AddMessage("Number of pages = {0}".format(pages))

# create the pdf
generatePDF(lines, pages, n)


# store current directory where temp.pdf is saved
w_directory = os.getcwd()


#retrieve the county's abbrevations
def GetCountyNameAbbreviation(check):
    abbr = ''

    county_dict = GetCountyDictionary("ABBRS")
    for county in county_dict:
        if county in check:
            abbr = county_dict[county]


    return abbr


l_inputDialog_1 = inputDialog_1.upper().split('\\')

pdfName = "{0}_PlatBookFinal.pdf".format(GetCountyNameAbbreviation(l_inputDialog_1))

#set path to save pdf
j = inputDialog_1.find('\\', 3)
inputDialog_1 = inputDialog_1[:j]


# change path
dirName = "{0}_Plat_Directory".format(GetCountyNameAbbreviation(l_inputDialog_1))

os.chdir(inputDialog_1)

if not os.path.exists(dirName):
    os.mkdir(dirName)

os.chdir(dirName)

# append pdfs
#x = r'H:\_Tutorials\Output\out\final'
if os.path.exists(pdfName):
    os.remove(pdfName)

x = os.getcwd()         #put final file in current directory
#finalFile = r"{0}.pdf".format(x)
finalFile = os.path.join(x, pdfName)

finalPDF = arcpy.mapping.PDFDocumentCreate(finalFile)

#finalPDF.appendPages(r'H:\_Tutorials\Output\out\SampleCoPlatBook.pdf')
finalPDF.appendPages(pdfPath)
#finalPDF.appendPages(r'H:\_Tutorials\Scripts\Plat_Owners_Index\temp.pdf')
finalPDF.appendPages(os.path.join(w_directory,'temp.pdf'))


#os.remove(os.path.join(w_directory,'temp.pdf'))

arcpy.AddMessage('working directory {0}'.format(os.getcwd()))

# clean up
if os.path.exists(os.path.join(w_directory,'temp.pdf')):
    os.remove(os.path.join(w_directory,'temp.pdf'))



arcpy.AddMessage("Success! Output saved to {0}".format(finalFile))



