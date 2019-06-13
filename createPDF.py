#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      demolakstate
#
# Created:     13/06/2019
# Copyright:   (c) demolakstate 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 5)

        self.cell(180, 3, "Plat Owners Index", 0, 0, 'C')
        self.ln(4)
        self.cell(180, 3, 'Name                                                  Sec#            TNP-RNG      Acres                              Name                                                  Sec#            TNP-RNG      Acres                             Name                                                  Sec#            TNP-RNG      Acres', 0, 0, 'L')

        # Line break
        self.ln(5)




    # generate pdf
def generatePDF(lines, pages, n):
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



        pdf.y = top
        offset = offset + 70
        start = end
        end = end + n
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




        start = end
        end = end + n
        pdf.add_page()

        #pdf.y = top

    pdf.output("temp.pdf")


