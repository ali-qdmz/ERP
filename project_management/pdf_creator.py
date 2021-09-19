from fpdf import FPDF
import re
import arabic_reshaper
# 297 x 210 mm
def create_mto_pdf():
    class PDF(FPDF):
        def lines(self):
            self.rect(2, 2, 292.0,205.0)
            self.line(30,2,30,207)
            self.line(80,2,80,207)
            self.line(95,45,95,207)
            self.line(120,45,120,207)
            self.line(150,45,150,207)
            self.line(175,45,175,207)
            self.line(185,53,185,207)
            self.line(215,53,215,207)
            self.line(215,2,215,45)
            self.line(225,53,225,207)
            self.line(235,53,235,207)
            self.line(245,53,245,207)
            self.line(265,45,265,207)
            self.line(275,53,275,207)
            self.line(9,45,9,207)
            self.line(70,53,70,207)
            self.line(138,53,138,207)
            self.line(284,53,284,207)
            pos = 63.5
            for i in range(17):
                pdf.line(2, pos + 6, 294, pos + 6)
                pos += 8
            self.line(2,15,80,15)
            self.line(2,25,80,25)
            self.line(2,35,80,35)
            self.line(2,45,294,45)
            self.line(95,49,175,49)
            self.line(2,53,294,53)
            self.line(2,57,215,57)
            self.line(2,61,294,61)
        def imagex(self):
                self.set_xy(214.5,12.0)
                self.image("C:/Users/Royal-ali/PycharmProjects/erp/static/images/logo.png",  link='', type='', w=80, h=25)
        def titles(self):
                self.set_xy(20.0,10.0)
                self.set_font('Arial', 'B', 16)
                self.set_text_color(0, 0, 0)
                self.cell(w=250.0, h=45.0, align='C', txt="MTO- Planning", border=0)
        def texts_persian(self,text,pos,font_size):
                self.set_xy(pos[0],pos[1])
                self.set_text_color(0.0, 0.0, 0.0)
                expression = r"^[a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z]"
                yourstring = text
                if (re.search(expression, yourstring) is None):
                    pdf.add_font('DejaVu', '', 'C:/Users/Royal-ali/Fonts/BTraffic.ttf', uni=True)
                    pdf.set_font('DejaVu', '', font_size)
                    arabic_string = arabic_reshaper.reshape(yourstring)
                    arabic_string = arabic_string[::-1]
                    w = pdf.get_string_width(arabic_string) + 6
                    pdf.cell(w, 9, arabic_string, 0, 1, 'L', 0)

    #             self.multi_cell(0,3,text_english)
        def title_persian(self,text,pos,font_size):
                self.set_xy(pos[0],pos[1])
                self.set_text_color(0.0, 0.0, 0.0)
                expression = r"^[a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z]"
                yourstring = text
                if (re.search(expression, yourstring) is None):
                    pdf.add_font('DejaVu', '', 'C:/Users/Royal-ali/Fonts/BTraffic.ttf', uni=True)
                    pdf.set_font('DejaVu', '', font_size)
                    arabic_string = arabic_reshaper.reshape(yourstring)
                    arabic_string = arabic_string[::-1]
                    w = pdf.get_string_width(arabic_string) + 6
                    pdf.cell(w, 9, arabic_string, 0, 1, 'L', 0)

    #             self.multi_cell(0,3,text_english)

        def texts_english(self,text,pos,font_size):
                self.set_xy(pos[0],pos[1])
                self.set_text_color(0.0, 0.0, 0.0)
                self.set_font('Arial', '', font_size)
                self.multi_cell(0,3,text)

    # pdf = PDF()#pdf object
    # pdf=PDF(orientation='L') # landscape
    # pdf=PDF(unit='mm') #unit of measurement
    # pdf=PDF(format='A4',orientation='L') #page format. A4 is the default value of the format, you don't have to specify it.

    #default
    pdf = PDF(orientation='L', unit='mm', format='A4')
    # pdf.add_font("Arial", style="", fname="DejaVuSans.ttf", uni=True)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.lines()
    pdf.imagex()
    pdf.titles()

    pdf.texts_persian("خریدار ",(15,0.5),8)
    pdf.texts_persian("کد فرم / ویرایش: ",(40,0.5),8)
    pdf.texts_persian("نام دستگاه ",(55,13),8)
    pdf.texts_persian("کد پروژه فرعی",(13.5,13),6.5)
    pdf.texts_persian("نام مجموعه",(15.5,23),7.5)
    pdf.texts_persian("شماره دستور کار ",(53,23),8)
    pdf.texts_persian("شماره مدرک ",(50,33),8)
    pdf.texts_persian("تاریخ تهیه ",(13.5,33),7.5)
    pdf.texts_persian("تهیه کننده:",(12,42.5),8)
    pdf.texts_persian("صفحه",(2,42),6)
    pdf.texts_persian("تایید کننده:",(46.5,42.5),8)
    pdf.texts_persian("تعداد دستگاه:",(79.5,42.5),7)
    pdf.texts_persian("اقلام برشی :",(105,42.5),6.5)
    pdf.texts_persian("اقلام ریخته :",(135,42.5),6.5)
    pdf.texts_persian("اقلام استاندارد :",(158,42.5),6.5)
    pdf.texts_persian("شرح دستور کار: ",(243,44),8)
    pdf.texts_persian("شماره سریال:",(276,42.5),7.5)
    pdf.title_persian("لیست مواد اولیه و اقلام استاندارد-برنامه ریزی",(94,8.5),16)
    pdf.texts_persian("موجود",(217,50),6)
    pdf.texts_persian("در",(220,52),6)
    pdf.texts_persian("انبار",(218.5,54.5),6)
    pdf.texts_persian("نیاز",(227,50),6)
    pdf.texts_persian("به مدل",(226,52),6)
    pdf.texts_persian("ریخته",(226.5,54.5),6)
    pdf.texts_persian("برونسپاری",(234.5,52.5),6)
    pdf.texts_persian("زمان تحویل به",(247,51),6.5)
    pdf.texts_persian(" تولید",(252,54),6.5)
    pdf.texts_persian("خرید",(266,50),6)
    pdf.texts_persian("اقلام",(266.75,52.5),6)
    pdf.texts_persian("ساختنی",(265.75,54.5),6)
    pdf.texts_persian("خرید",(276,50),6)
    pdf.texts_persian("استاندارد",(275,53),6)
    pdf.texts_persian("ریخته گری",(283.5,52),6)
    pdf.texts_persian("ردیف",(1.75,54.5),7)
    pdf.texts_persian("کد قطعه / فایل",(40,54.25),8)
    pdf.texts_persian("نام قطعه",(13,54.25),8)
    pdf.texts_persian("ویرایش",(69.75,54.25),8)
    pdf.texts_persian("نوع مواد",(81.5,54.25),8)
    pdf.texts_persian("شرح قطعه",(100.5,54.25),8)
    pdf.texts_persian("جنس",(125.5,54.25),8)
    pdf.texts_persian("تعداد",(140.5,54.25),8)
    pdf.texts_persian("ابعاد مواد خام",(153,54.25),8)
    pdf.texts_persian("وزن",(176,54.25),8)
    pdf.texts_persian("توضیحات",(192,54.25),8)


    pdf.texts_english(": Client /",(5,3.75),8)
    pdf.texts_english(":Machine Name /",(33.75,16),8)
    pdf.texts_english(":SP.Cod /",(3,16),6.5)
    pdf.texts_english(":collection /",(2,26),7.5)
    pdf.texts_english(":Work Order No /",(31.75,26),8)
    pdf.texts_english(":Doc No /",(38,36),8)
    pdf.texts_english(":Date /",(6,36),7.5)
    pdf.texts_english("CUT",(98,45.5),7.5)
    pdf.texts_english("CAST",(125,45.5),7.5)
    pdf.texts_english("STD",(152,45.5),7.5)
    pdf.texts_english("POS",(2,53.5),6.5)
    pdf.texts_english("Part name",(12,53.5),6.5)
    pdf.texts_english("SPS-part / file NO",(38,53.5),6.5)
    pdf.texts_english("Ver",(72,53.5),6.5)
    pdf.texts_english("Material Type",(79.5,53.5),6.5)
    pdf.texts_english("Description",(100,53.5),6.5)
    pdf.texts_english("Material",(124,53.5),6.5)
    pdf.texts_english("QTY",(141,53.5),6.5)
    pdf.texts_english("Raw Material dimension",(149.5,53.5),6.25)
    pdf.texts_english("Mass-Kg",(174.25,53.5),6.5)
    pdf.texts_english("Remark",(194,53.5),6.5)
    pdf.set_author('Eser SAYGIN')
#     pdf.output('test.pdf','F')
    return pdf
