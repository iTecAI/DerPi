import serial

uart = serial.Serial('/dev/serial0', 115200)
rbuf = ''

def tx(cmd):
    global uart
    uart.write(eval('b"' + cmd + '"'))
    
def rx():
    global uart, rbuf
    ret = uart.read()[len(rbuf) - 1:]
    rbuf = rbuf + ret
    print(ret)
    return ret
    
def call(number):
    tx('ATD' + number + ';')

def hangup():
    tx('ATH')

