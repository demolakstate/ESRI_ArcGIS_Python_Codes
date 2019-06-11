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

import arcpy, textwrap
from operator import itemgetter

from fpdf import FPDF
import webbrowser
import math


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 5)
        self.cell(180, 3, 'Name                                                  Sec#            TNP-RNG      Acres                              Name                                                  Sec#            TNP-RNG      Acres                             Name                                                  Sec#            TNP-RNG      Acres', 0, 0, 'L')
        # Line break
        self.ln(5)


workspace = arcpy.GetParameterAsText(0)

# eliminate the feature class
ind = workspace.rfind('\\')
workspace =  workspace[:ind]


#arcpy.env.workspace = r'H:\Clark\CA_Geodatabases\CA_Appraiser_ORION.gdb'
arcpy.env.workspace = workspace

featureClass = 'Parcels_ORION_erased'

output_file = r'H:\_Tutorials\Output\out\PlatOwnerIndex_14.txt'


fields = ['PartyNames', 'Section', 'TNP_RNG', 'ACRES']
# loop through the feature class to identify needed elements
##with arcpy.da.SearchCursor(featureClass, fields) as cursor:
##    arcpy.AddMessage('Name Sec# Twp Acres')
##    for row in cursor:
##        if row[0] is not None:
##            #print(u'{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
##            arcpy.AddMessage('{0}, {1}, {2}, {3}'.format(row[0][:40], row[1], row[2], row[3]))


#lines = [row for row in sorted(arcpy.da.SearchCursor(featureClass, fields), key=lambda column: column[0]) if row[0] is not None]  # sort by PartyNames

#lines = [row for row in sorted(arcpy.da.SearchCursor(featureClass, fields), key=lambda column: (column[0], column[2], column[1])  ) if row[0] is not None]  # sort by PartyNames
lines = [row for row in sorted(arcpy.da.SearchCursor(featureClass, fields), key=itemgetter(0,2,1)  ) if row[0] is not None]  # sort by PartyNames


arcpy.AddMessage(lines)



#with open(output_file, 'r') as f:

#lines = f.readlines()

#lines = list(lines)

print("length of the list", len(lines))

# get number of pages
pages = len(lines)/246.0

arcpy.AddMessage("Number of pages 1st = {0}".format(pages))
pages = math.ceil(pages)

print("Number of pages", pages)
arcpy.AddMessage("Number of pages = {0}".format(pages))

# number of lines on a page
n = 87


#lines = f.readlines()
#pdf = FPDF(orientation='P', unit='mm', format='letter')

pdf = PDF()
    #pdf = CustomPDF()
pdf.set_font("Times", size=5)
pdf.add_page()


top = pdf.y

start = 0
end = n
#end = start + 82

for i in range(int(pages)):
    #
    offset = pdf.x + 70


    for line in lines[start:end]:


        w, x, y, z = line

        w = str(w)
        w = w.replace('\n', '')
        w = w[:20]

        w = w.ljust(20)

        x = x.rjust(2)

        y = y.ljust(7)

        z = round(z,1)
        z = str(z)


        #pdf.multi_cell(100, 3, line, 0, 'L')
        Top_in = pdf.y
        offset_in = pdf.x + 30
        pdf.multi_cell(25, 3, w, 0, 'L')

        pdf.y = Top_in
        pdf.x = offset_in
        offset_in = offset_in + 10

        pdf.multi_cell(10, 3, x, 0, 'L')

        pdf.y = Top_in
        pdf.x = offset_in
        offset_in = offset_in + 10
        pdf.multi_cell(15, 3, y, 0, 'L')


        pdf.y = Top_in
        pdf.x = offset_in
        pdf.multi_cell(10, 3, z, 0, 'L')





















    pdf.y = top
    #offset = pdf.x + 70
    start = end
    end = end + n
    for line in lines[start:end]:



##        w, x, y, z = line
##        #p = str(w) + ' ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n'
##        #f.write(p)
##        w = w[:40].replace('\n', '')
##
##
##        # Wrap
##        #wrapper = textwrap.TextWrapper(width=20)
##       # w = wrapper.fill(text=w)
##        w = '{:<40}'.format(w)
##
##        x = x.ljust(2)
##
##        y = y.ljust(7)
##
##        z = round(z,1)
##
##        line = '{0}    {1}    {2}    {3}'.format(w, x, y, z)
##        arcpy.AddMessage(line)

        w, x, y, z = line

        w = str(w)
        w = w.replace('\n', '')
        w = w[:20]

        w = w.ljust(20)

        x = x.rjust(2)

        y = y.ljust(7)

        z = round(z,1)
        z = str(z)



























            # Reset y coordinate


            # Move to computed offset
        pdf.x = offset


        Top_in = pdf.y
        offset_in = pdf.x + 30
        pdf.multi_cell(25, 3, w, 0, 'L')

        pdf.y = Top_in
        pdf.x = offset_in
        offset_in = offset_in + 10

        pdf.multi_cell(10, 3, x, 0, 'L')

        pdf.y = Top_in
        pdf.x = offset_in
        offset_in = offset_in + 10
        pdf.multi_cell(15, 3, y, 0, 'L')


        pdf.y = Top_in
        pdf.x = offset_in
        pdf.multi_cell(10, 3, z, 0, 'L')





        #offset = pdf.x + 70




        #pdf.multi_cell(100, 3, line, 0, 'L')


    pdf.y = top
    offset = offset + 70
    start = end
    end = end + n
    for line in lines[start:end]:



##        w, x, y, z = line
##        #p = str(w) + ' ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n'
##        #f.write(p)
##        w = w.replace('\n', '')
##        w = w[:40]
##
##        # Wrap
##        #wrapper = textwrap.TextWrapper(width=20)
##       # w = wrapper.fill(text=w)
##        w = '{:<40}'.format(w)
##
##        x = x.ljust(2)
##
##        y = y.ljust(7)
##
##        z = round(z,1)
##
##        line = '{0}    {1}    {2}    {3}'.format(w, x, y, z)
##        arcpy.AddMessage(line)

        w, x, y, z = line

        w = str(w)
        w = w.replace('\n', '')
        w = w[:20]

        w = w.ljust(20)

        x = x.rjust(2)

        y = y.ljust(7)

        z = round(z,1)
        z = str(z)














            # Reset y coordinate
    #
        pdf.x = offset


        #pdf.multi_cell(100, 3, line, 0, 'L')
        Top_in = pdf.y
        offset_in = pdf.x + 30
        pdf.multi_cell(25, 3, w, 0, 'L')

        pdf.y = Top_in
        pdf.x = offset_in
        offset_in = offset_in + 10

        pdf.multi_cell(10, 3, x, 0, 'L')

        pdf.y = Top_in
        pdf.x = offset_in
        offset_in = offset_in + 10
        pdf.multi_cell(15, 3, y, 0, 'L')


        pdf.y = Top_in
        pdf.x = offset_in
        pdf.multi_cell(10, 3, z, 0, 'L')


        #






    #offset = pdf.x - 140

        #pdf.multi_cell(100, 3, line, 0, 'L')

    start = end
    end = end + n
    pdf.add_page()

    #pdf.y = top

pdf.output("KM_36.pdf")



# append pdfs
x = r'H:\_Tutorials\Output\out\final'
finalFile = r"{0}.pdf".format(x)

finalPDF = arcpy.mapping.PDFDocumentCreate(finalFile)

finalPDF.appendPages(r'H:\_Tutorials\Output\out\SampleCoPlatBook.pdf')
finalPDF.appendPages(r'H:\_Tutorials\Scripts\Plat_Owners_Index\KM_36.pdf')





#webbrowser.open_new('KM_36.pdf')
webbrowser.open_new(r'H:\_Tutorials\Output\out\final.pdf')

