from tkinter import *
from tkinter import ttk
from tkcalendar import *
import mysql.connector
from tkinter import messagebox
from datetime import *

oysdb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='ogr_ynt_sistemi'

    )



mycursor = oysdb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS ogrenci (id INT AUTO_INCREMENT PRIMARY KEY, ogrenci_adi VARCHAR(30),"
                 "ogrenci_soyadi VARCHAR(30), ogrenci_no VARCHAR(30), durum VARCHAR(30), bolum VARCHAR(30),"
                 "dogum_tarihi VARCHAR(30), adres TEXT)")


class Anasayfa(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Öğrenci Yönetim Sistemi")
        self.wm_resizable(False, False)


        self.frame1 = Frame(self, height=150, bg="#f6eec9")
        self.frame1.pack(fill=X)
        self.frame2 = Frame(self, height=450, bg="#fed39f")
        self.frame2.pack(fill=X)

        self.baslik = Label(self.frame1, text="ÖĞRENCİ", font=("Garamond", 35, "bold"), bg="#f6eec9")
        self.baslik.place(x=200, y=40)
        self.baslik = Label(self.frame1, text="YÖNETİM SİSTEMİ", font=("Garamond", 25, "bold"), bg="#f6eec9")
        self.baslik.place(x=150, y=85)

        self.dugme1 = Button(self.frame2, text="ÖĞRENCİ EKLEME ", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=ogr_ekleme)
        self.dugme1.place(x=150, y=60, width=300)

        self.dugme2 = Button(self.frame2, text="ÖĞRENCİ GÜNCELLEME", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=ogr_guncelle)
        self.dugme2.place(x=150, y=100, width=300)

        self.dugme3 = Button(self.frame2, text="ÖĞRENCİ SİLME", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=ogr_sil)
        self.dugme3.place(x=150, y=140, width=300)

        self.dugme4 = Button(self.frame2, text="ÖĞRENCİ ARAMA", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#fed39f", command=ogr_arama)
        self.dugme4.place(x=150, y=180, width=300)

class ogr_ekleme(Toplevel):
    pass
class ogr_guncelle(Toplevel):
    pass
class ogr_sil(Toplevel):
    pass
class ogr_arama(Toplevel):
    pass
if  __name__=="__main__":

    app= Anasayfa()
    app.mainloop()