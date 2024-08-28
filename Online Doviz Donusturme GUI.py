import requests
import json
import tkinter as tk
import time
from tkinter import ttk

form = tk.Tk()
form.title('Online Doviz Cevirici')
form.geometry('685x465+650+300')
form.resizable(width=False,height=False)
form.config(bg='#f5efde')

####################### -------- LUTFEN OKUYUNUZ (ONEMLI !) -------- #######################
'''
ilk olarak 'https://www.exchangerate-api.com' sitesine gidiniz.
'Get Free Key' kismina tiklayip, kayit olduktan sonra, API Keyinizi ucretsiz bir sekilde aliniz.
En son 'my_api' kisminda iki tirnagin icersine API Keyinizi yapistiriniz. (my_api, donusturme fonksiyonunun icinde)
Eger 'exchangerate-api.com' sitesi kapanmadiysa veya bu sitede herhangi bir sorun cikmassa, bu kod sorunsuz calisacaktir.
Kod calismiyorsa belli ki sitede bir sorun vardir.
Ayrica 'requests' modulunu kurmaniz gerekli, eger modulunuz yoksa konsola "pip install requests" yazmaniz yeterli. Otomatik olarak kurulacaktir
'''
####################### -------- LUTFEN OKUYUNUZ (ONEMLI !) -------- #######################

def donusturme():
    try:
        hataLabel.config(text='')
#-----------------------------------------------------------------#
        my_api = ''            #API Keyini buraya yapistir.          
#-----------------------------------------------------------------#
        api_url = f'https://v6.exchangerate-api.com/v6/{my_api}/latest/'
        bozulanDoviz = bozulan_Doviz_Entry.get()
        alinanDoviz = alinan_Doviz_Entry.get()
        miktar = int(miktar_Entry.get())
        result = requests.get(api_url+bozulanDoviz)
        result = json.loads(result.text)
        standart = ('{:.2f} {} = {:.2f} {}'.format(result["conversion_rates"][bozulanDoviz],bozulanDoviz,result["conversion_rates"][alinanDoviz],alinanDoviz))
        donusum = ('{:.2f} {} = {:.2f} {}'.format(miktar,bozulanDoviz,miktar*result["conversion_rates"][alinanDoviz],alinanDoviz))
        standart_Label.config(text=standart)
        donusum_Label.config(text=donusum)
    except:
        hataLabel.config(text='(HATA) donusturme basarisiz')

def zaman():
    now = time.strftime('%H:%M:%S')
    zaman_Label.config(text=now)
    zaman_Label.after(1000,zaman)

hataLabel = tk.Label(form,text='',fg='red',font='sans 31 bold',bg='#f5efde')
hataLabel.place(x=64,y=270)

mainLabel = tk.Label(form,text='Online Doviz Donusturme',fg='#1477e0',font='sans 42 bold',bg='#c3c7a5')
mainLabel.pack(side=tk.TOP,fill=tk.Y)

bozulan_Doviz_Label = tk.Label(form,text='Bozulacak\ndoviz',fg='red',font='sans 18 bold',bg='#f5efde')
bozulan_Doviz_Label.place(x=30,y=90)

alinan_Doviz_Label = tk.Label(form,text='Alinacak\ndoviz',fg='red',font='sans 18 bold',bg='#f5efde')
alinan_Doviz_Label.place(x=280,y=90)

miktar_Label = tk.Label(form,text='Donusecek\nmiktar',fg='red',font='sans 18 bold',bg='#f5efde')
miktar_Label.place(x=523,y=90)

bozulan_Doviz_Entry = tk.Entry(form,text='Bozulacak\ndoviz',font='sans 9 bold')
bozulan_Doviz_Entry.place(x=21,y=165)

alinan_Doviz_Entry = tk.Entry(form,text='Alinacak\ndoviz',font='sans 9 bold')
alinan_Doviz_Entry.place(x=261,y=165)

miktar_Entry = tk.Entry(form,text='Donusecek\nmiktar',font='sans 9 bold')
miktar_Entry.place(x=519,y=165)

donustur_Button = tk.Button(form,text='Donustur',font='sans 21 bold',bg='#c3c7a5',fg='#219a25',command=donusturme)
donustur_Button.place(x=38,y=372)

liste_Label = tk.Label(form,text='Para birimleri listesi',fg='#1477e0',font='sans 18 bold',bg='#f5efde')
liste_Label.place(x=226,y=360)

zaman_Label = tk.Label(form,text='',fg='#dc48e1',font='sans 32 bold',bg='#f5efde')
zaman_Label.place(x=480,y=372)

api_Label = tk.Label(form,text='Online API: www.exchangerate-api.com',fg='#794fdf',font='sans 13 bold',bg='#f5efde')
api_Label.place(x=370,y=437)

standart_Label = tk.Label(form,text='',fg='black',font='sans 16 bold',bg='#f5efde')
standart_Label.place(x=70,y=230)

donusum_Label = tk.Label(form,text='',fg='red',font='sans 26 bold',bg='#f5efde')
donusum_Label.place(x=65,y=280)

para_birimleri = [
    "USD: Amerika Birleşik Devletleri",
    "AED: Birleşik Arap Emirlikleri",
    "AFN: Afganistan",
    "ALL: Arnavutluk",
    "AMD: Ermenistan",
    "ANG: Hollanda Antilleri",
    "AOA: Angola",
    "ARS: Arjantin",
    "AUD: Avustralya",
    "AWG: Aruba",
    "AZN: Azerbaycan",
    "BAM: Bosna-Hersek",
    "BBD: Barbados",
    "BDT: Bangladeş",
    "BGN: Bulgaristan",
    "BHD: Bahreyn",
    "BIF: Burundi",
    "BMD: Bermuda",
    "BND: Brunei",
    "BOB: Bolivya",
    "BRL: Brezilya",
    "BSD: Bahamalar",
    "BTN: Bhutan",
    "BWP: Botsvana",
    "BYN: Beyaz Rusya",
    "BZD: Belize",
    "CAD: Kanada",
    "CDF: Kongo",
    "CHF: İsviçre",
    "CLP: Şili",
    "CNY: Çin",
    "COP: Kolombiya",
    "CRC: Kosta Rika",
    "CUP: Küba",
    "CVE: Yeşil Burun Adaları",
    "CZK: Çekya",
    "DJF: Cibuti",
    "DKK: Danimarka",
    "DOP: Dominik Cumhuriyeti",
    "DZD: Cezayir",
    "EGP: Mısır",
    "ERN: Eritre",
    "ETB: Etiyopya",
    "EUR: Euro Bölgesi",
    "FJD: Fiji",
    "FKP: Falkland Adaları",
    "FOK: Faroe Adaları",
    "GBP: İngiltere",
    "GEL: Gürcistan",
    "GGP: Guernsey",
    "GHS: Gana",
    "GIP: Cebelitarık",
    "GMD: Gambiya",
    "GNF: Gine",
    "GTQ: Guatemala",
    "GYD: Guyana",
    "HKD: Hong Kong",
    "HNL: Honduras",
    "HRK: Hırvatistan",
    "HTG: Haiti",
    "HUF: Macaristan",
    "IDR: Endonezya",
    "ILS: İsrail",
    "IMP: Man Adası",
    "INR: Hindistan",
    "IQD: Irak",
    "IRR: İran",
    "ISK: İzlanda",
    "JEP: Jersey",
    "JMD: Jamaika",
    "JOD: Ürdün",
    "JPY: Japonya",
    "KES: Kenya",
    "KGS: Kırgızistan",
    "KHR: Kamboçya",
    "KID: Kiribati",
    "KMF: Komor Adaları",
    "KRW: Güney Kore",
    "KWD: Kuveyt",
    "KYD: Cayman Adaları",
    "KZT: Kazakistan",
    "LAK: Laos",
    "LBP: Lübnan",
    "LKR: Sri Lanka",
    "LRD: Liberya",
    "LSL: Lesotho",
    "LYD: Libya",
    "MAD: Fas",
    "MDL: Moldova",
    "MGA: Madagaskar",
    "MKD: Kuzey Makedonya",
    "MMK: Myanmar",
    "MNT: Moğolistan",
    "MOP: Makao",
    "MRU: Moritanya",
    "MUR: Mauritius",
    "MVR: Maldivler",
    "MWK: Malavi",
    "MXN: Meksika",
    "MYR: Malezya",
    "MZN: Mozambik",
    "NAD: Namibya",
    "NGN: Nijerya",
    "NIO: Nikaragua",
    "NOK: Norveç",
    "NPR: Nepal",
    "NZD: Yeni Zelanda",
    "OMR: Umman",
    "PAB: Panama",
    "PEN: Peru",
    "PGK: Papua Yeni Gine",
    "PHP: Filipinler",
    "PKR: Pakistan",
    "PLN: Polonya",
    "PYG: Paraguay",
    "QAR: Katar",
    "RON: Romanya",
    "RSD: Sırbistan",
    "RUB: Rusya",
    "RWF: Ruanda",
    "SAR: Suudi Arabistan",
    "SBD: Solomon Adaları",
    "SCR: Seyşeller",
    "SDG: Sudan",
    "SEK: İsveç",
    "SGD: Singapur",
    "SHP: Saint Helena",
    "SLE: Sierra Leone",
    "SLL: Sierra Leone",
    "SOS: Somali",
    "SRD: Surinam",
    "SSP: Güney Sudan",
    "STN: São Tomé ve Príncipe",
    "SYP: Suriye",
    "SZL: Esvatini",
    "THB: Tayland",
    "TJS: Tacikistan",
    "TMT: Türkmenistan",
    "TND: Tunus",
    "TOP: Tonga",
    "TRY: Türkiye",
    "TTD: Trinidad ve Tobago",
    "TVD: Tuvalu",
    "TWD: Tayvan",
    "TZS: Tanzanya",
    "UAH: Ukrayna",
    "UGX: Uganda",
    "UYU: Uruguay",
    "UZS: Özbekistan",
    "VES: Venezuela",
    "VND: Vietnam",
    "VUV: Vanuatu",
    "WST: Samoa",
    "XAF: CFA Frangı BEAC",
    "XCD: Doğu Karayip Doları",
    "XDR: SDR (Özel Çekme Hakları)",
    "XOF: CFA Frangı BCEAO",
    "XPF: CFP Frangı",
    "YER: Yemen",
    "ZAR: Güney Afrika",
    "ZMW: Zambiya",
    "ZWL: Zimbabve"
]

combo = ttk.Combobox(form, values=para_birimleri,font='sans 13 bold')
combo.set("Doviz listesi")
combo.place(x=242,y=400)

zaman()

tk.mainloop()