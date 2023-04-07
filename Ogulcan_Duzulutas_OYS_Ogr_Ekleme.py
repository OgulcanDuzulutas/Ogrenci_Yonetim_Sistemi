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
   
    def __init__(self):
      Toplevel.__init__(self)
      self.wm_geometry("600x400+400+100")
      self.wm_title("Öğrenci Ekleme")
      self.wm_resizable(False, False)
        
      self.frame1 = Frame(self, height=50, bg="#f6eec9")
      self.frame1.pack(fill=X)
      self.frame2 = Frame(self, height=550, bg="#fed39f")
      self.frame2.pack(fill=X)
      self.baslik = Label(self.frame1, text="Öğrenci Bilgileri Giriniz", font=("Garamond", 25, "bold"), bg="#f6eec9")
      self.baslik.place(x=150,y=5)
      
      Label(self.frame2, text="Öğrenci Adı", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=50)
      Label(self.frame2, text="Öğrenci Soyadı", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=80)
      Label(self.frame2, text="Öğrenci Numarası", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=110)
      Label(self.frame2, text="Öğrencilik Durumu", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=140)
      Label(self.frame2, text="Bölümü", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=170)
      Label(self.frame2, text="Doğum Tarihi", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=200)
      Label(self.frame2, text="Adres", bg="#fed39f", font=("Garamond", 15, "bold")).place(x=60, y=230)
      
      self.ad = Entry(self.frame2, font=("Garamond", 15, "bold"))
      self.ad.place(x=300, y=50, width=250)
      self.soyadi = Entry(self.frame2, font=("Garamond", 15, "bold"))
      self.soyadi.place(x=300, y=80, width=250)
      self.numarasi = Entry(self.frame2, font=("Garamond", 15, "bold"))
      self.numarasi.place(x=300, y=110, width=250)
      self.sayi = IntVar(self.frame2)
      self.durum0 = Radiobutton(self.frame2, text="Aktif", variable=self.sayi, value=1)
      self.durum0.place(x=300, y=140)
      self.durum1 = Radiobutton(self.frame2, text="Dondurulmuş", variable=self.sayi, value=2)
      self.durum1.place(x=360, y=140)
      self.durum2 = Radiobutton(self.frame2, text="Mezun", variable=self.sayi, value=3)
      self.durum2.place(x=470, y=140)
      self.bolum = ttk.Combobox(self.frame2, font=("Garamond", 15, "bold"), state="readonly",
                                values=["BOTE", "BESYO", "TARİH", "MİMARLIK", "HUKUK", "TIP", "MATEMATİK", "KİMYA"])
      self.bolum.place(x=300, y=170, width=250)
      self.dogum_tarihi = DateEntry(self.frame2, font=("Garamond", 15, "bold"), locale="tr_TR")
      self.dogum_tarihi.place(x=300, y=200, width=250)
      self.adres = Text(self.frame2, font=("Garamond", 15, "bold"), height=3)
      self.adres.place(x=300, y=230, width=250)
      
      Button(self.frame2, text="KAYDET", command=self.kaydet,
             font=("Garamond", 15, "bold")).place(x=60, y=300, width=125)
      
    def kaydet(self):
      sql = "INSERT INTO ogrenci (ogrenci_adi, ogrenci_soyadi, ogrenci_no, durum, bolum, dogum_tarihi, adres) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (self.ad.get(), self.soyadi.get(), self.numarasi.get(), self.sayi.get(), self.bolum.get(),
               self.dogum_tarihi.get(), self.adres.get('1.0', END))
      mycursor.execute(sql, val)
      oysdb.commit()
      self.temizle()
    def temizle(self):

        messagebox.showinfo("Başarılı", "Kayıt başarılı!")
        self.bolum.set("")
        self.ad.delete(0, END)
        self.soyadi.delete(0, END)
        self.numarasi.delete(0, END)
        self.adres.delete("1.0", END)
        self.sayi.set(0)
        self.focus()
class ogr_guncelle(Toplevel):
    pass
class ogr_sil(Toplevel):
    pass
class ogr_arama(Toplevel):
    pass
if  __name__=="__main__":

    app= Anasayfa()
    app.mainloop()