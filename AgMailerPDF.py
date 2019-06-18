#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
# This scripts takes in a Map Document (.mxd) with enabled data driven page, and creates a PDF file from the data
# Output pdf is stored in
#
# Author:      demolakstate
#
# Created:     24/05/2019
# Copyright:   (c) demolakstate 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# must have enabled data driven page in map Document and set to Layout view

import arcpy, os

arcpy.env.overwriteOutput = True

# get input from the user dialog box
mxdPath = arcpy.GetParameterAsText(0)

mxd = arcpy.mapping.MapDocument(mxdPath)

x = os.path.splitext(mxdPath)[0].strip()

arcpy.AddMessage("x {0}".format(x))


finalFile = r"{0}.pdf".format(x)

finalPDF = arcpy.mapping.PDFDocumentCreate(finalFile)


for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  currentPage = str(mxd.dataDrivenPages.currentPageID)          # returns the current page number


  pageCount = str(mxd.dataDrivenPages.pageCount)                # returns total number of pages in the map dodument
  print 'Exporting page %s of %s' % (currentPage, pageCount)

  tmpPDF = r"{0}".format(x) + str(pageNum) + ".pdf"


  arcpy.mapping.ExportToPDF(mxd, tmpPDF)
  print tmpPDF

  finalPDF.appendPages(tmpPDF)
  os.remove(tmpPDF)                 # delete temporary pdf from disk

  arcpy.AddMessage("SUCCESS! finalFile saved to {0}".format(finalFile))


  del tmpPDF

del mxd

