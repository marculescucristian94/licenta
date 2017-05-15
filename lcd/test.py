import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

while True:
    mylcd.lcd_display_text('Awaiting connection...')
    sleep(1)
    mylcd.lcd_clear()
    sleep(1)

