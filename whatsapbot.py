from selenium import webdriver
import smtplib
import time


#download mozilla firefox before use this command
#pls fill path.
path = 'C:\\xx\xxx\xxx\geckodriver.exe'

browser = webdriver.Firefox(executable_path=path)

def mailgonder(mesaj):

    sahip='yyy.yyy@gmail.com' #this is sender e mail if you want change this.
    alıcı='xxx_xxx@hotmail.com' #this is receiver e mail pls fill
    giris='yyy.yyy@gmail.com'#this is sender e mail if you want change this.
    sifre='password' # this is sender password pls fill.

    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(giris,sifre)
    server.sendmail(sahip,alıcı,mesaj)
    server.quit()

browser.get('https://web.whatsapp.com/')

kontrol = True
kontrol2 = True
kontrol3 = False
time.sleep(10)
while True:


     try:
         time.sleep(10)
         ONLINE_STATUS_LABEL = "/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span"
         browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
         if kontrol:
             msg1="online"
             mailgonder(msg1)
             baslangıc = time.time()
             kontrol=False
             kontrol2=True
             kontrol3=True

     except:
         kontrol = True
         if kontrol2==True:
             msg="ofline"
             mailgonder(msg)
             if kontrol3==True:
                 bitis = time.time() - baslangıc
                 mailgonder(str(bitis))
                 baslangıc=time.time()
             kontrol2=False
