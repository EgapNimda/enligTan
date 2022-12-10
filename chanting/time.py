
import requests
import time
from requests_html import HTMLSession
from datetime import date


def scraping():
    session = HTMLSession()
    res = session.get("https://www.timeanddate.com/moon/phases/")

    sel = 'body > div.main-content-div > main > article > section.fixed > div.row.dashb.pdflexi > div > table > tbody'
    table = res.html.find(sel, first=False)
    j = ''
    for i in table:
        j+=(i.text.replace("\n"," "))
        l = j.split(" ")

    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    emp = []
    for i in range(len(l)):
        j = i + 1 
        if j < len(l):
            if(l[j] in months):
                word = l[i]+"/"+str(month_converter(l[j]))
                emp.append(word)    
    return emp

def month_converter(month):
    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    if(months.index(month) + 1 < 10):
        return "0"+str(months.index(month) + 1)
    else:
        return months.index(month) + 1


def monk_day():
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    period = scraping()
    return day[:len(day)-5] in period



