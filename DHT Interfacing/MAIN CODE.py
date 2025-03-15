from machine import Pin, I2C
from time import sleep
from dht import DHT22
import OLED
sda = Pin(6)
scl = Pin(7)
i2c = I2C(1,sda=sda,scl=scl,freq=400000)
i2c.scan()
display = OLED.SSD1306_I2C(128,64,i2c)
sensor = DHT22(Pin(22))


while(1):
    display.fill(0)
    display.text("HELLO :)",0,0)
    display.hline(0,20,128,1)
    display.vline(0,21,64,1)
    sensor.measure()
    t=sensor.temperature()
    h=sensor.humidity()
    display.text("TEMP:"+str(t)+" C",2,25)
    display.text("HUMIDITY:"+str(h)+"%",2,40)
    display.show()
    print("Temperature: {}C Humidity: {:.0f}%".format(t,h))
    sleep(0.1)
    
