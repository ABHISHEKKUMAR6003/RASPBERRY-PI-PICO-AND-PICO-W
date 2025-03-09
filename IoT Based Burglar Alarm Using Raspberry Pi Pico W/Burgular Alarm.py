from machine import Pin, PWM
from time import sleep
import urequests
import network

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print('Waiting for connection...')
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print('wifi connected ...')
    print(wlan.ifconfig())

connect()

pir = Pin(18,Pin.IN)
buzzer = PWM(Pin(13))
buzzer.freq(1000)

def tone():
    buzzer.duty_u16(1000)

def noTone():
    buzzer.duty_u16(0)

def send(message): #Function to send a message to telegram
    s= "https://api.telegram.org/bot{BOT_TOKEN}:AAGadAFJuAH7lvGpBawo3FnRlufaxDJLOxQ/sendMessage?chat_id={CHAT_ID}&text={}".format(message)
    so = urequests.get(s)
send("DEVICE IS ON!")

while(1):
    if(pir.value()==1):
        send("BURGLER ALERT!!!!")
        tone()
        sleep(10)
    else:
        noTone()
    
