import time

try:
    import serial
except:
    import pyserial as serial

try:
    uart = serial.Serial('/dev/serial0', 115200, timeout=0.5)
except:
    print('Raspi not detected. Please install on raspberry pi to gain access to serial commands')
    uart = open('fake_serial.txt', 'wb+')
rbuf = ''

def tx(cmd):
    global uart
    uart.write(str(cmd + '\r\n').encode())
    
def rx():
    global uart
    _lines = []
    line = 'x'
    while len(line) > 0:
        line = uart.readline()
        _lines.append(line)
    lines = []
    for i in _lines:
        try:
            string = str(i.splitlines()[0])
            lines.append(string[2:len(string) - 1])
        except:
            pass
    return lines
    
def call(number):
    tx('ATD' + number + ';')

def hangup():
    tx('ATH')

def collision(pos, size, mouse_pos):
    return mouse_pos[0] >= pos[0] and mouse_pos[0] <= pos[0] + size[0] and mouse_pos[1] >= pos[1] and mouse_pos[1] <= pos[1] + size[1]

