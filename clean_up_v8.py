#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      demolakstate
#
# Created:     26/06/2019
# Copyright:   (c) demolakstate 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

# siteaddVerification function takes geodataset and returns a csv file delimited by semicolon - opens in excel menu from data -> from text ...
# Author:      demolakstate
# Created:     26/06/2019
def sitaddVerification(add_par):

    #fc = r'H:\Morris\MR_Geodatabases\911 NG\MR_KSNG911.gdb\ADD_PAR'
    fc = add_par
    out = add_par

    # set path to out csv
    ind = out.rfind('\\')
    out = out[:ind]
    ind = out.rfind('\\')
    out = out[:ind]



    fields = ['SitusAddre', 'LABEL', 'ZIP_1', 'POSTCO', 'PID', 'NGADDID']

    print('{0}            <==>                 {1}'.format('SitusAddre', 'LABEL'))

    with open('{0}\ADD_PAR.csv'.format(out), 'w') as f:
        f.writelines('SitusAddress; PID; LABEL; ADDID')
        f.write('\n')

        for row in arcpy.da.SearchCursor(fc, fields):
            if row[0] is None or row[1] is None:
                print('{0}            <==>                 {1}'.format(row[0], row[1]))
                f.writelines('{0};{1};{2}, {3}, KS {4};{5}'.format(row[0], row[4], row[1], row[3], row[2], row[5]))
                f.write('\n')


            elif row[0].upper().replace(' ', '').replace(',', '').lstrip('0') != row[1].upper().replace(' ', '').replace(',', '').lstrip('0') + row[3].upper().replace(' ', '').replace(',', '') + 'KS' + str(row[2]).replace(' ', '').upper() :
                print('{0}  |   {1}       <==>                 {2}, {3}, KS {4} | {5}'.format(row[0], row[4], row[1], row[3], row[2], row[5]))
                f.writelines('{0};{1};{2}, {3}, KS {4};{5}'.format(row[0], row[4], row[1], row[3], row[2], row[5]))
                f.write('\n')








