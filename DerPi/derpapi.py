import time, os
from ascii_func import ctrl

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

def tx(cmd, echar=True):
    global uart
    if echar:
        cmd = cmd + '\r\n'
    uart.write(cmd.encode())
    
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
def store(key=None, data='XXC-NONE-~~~(*)', app=None):
    curdir = os.getcwd()
    if app == None:
        try:
            if curdir.endswith('DerPi'):
                to_open = 'data\\os.mvh'
                datafile = open(to_open, 'r')
            else:
                to_open = '..\\..\\data\\' + curdir.split('\\')[len(curdir.split('\\')) - 1] + '.mvh'
                datafile = open(to_open, 'r')
        except:
            pass
    else:
        try:
            if curdir.endswith('DerPi'):
                to_open = 'data\\' + app + '.mvh'
                datafile = open(to_open, 'r')
            else:
                to_open = '..\\..\\data\\' + app + '.mvh'
                datafile = open(to_open, 'r')
        except OSError:
            raise NameError ('Unknown app ' + app)
    try:
        curdata = eval(datafile.read())
        datafile.close()
    except OSError:
        curdata = {}
    except NameError:
        curdata = {}
    datafile = open(to_open, 'w')
    if data == 'XXC-NONE-~~~(*)':
        del curdata[str(key)]
    else:
        if key == None and type(data) == dict:
            curdata = data
        else:
            curdata[str(key)] = data
    datafile.write(str(curdata))
    datafile.close()

def retrieve(key=None, app=None):
    curdir = os.getcwd()
    if app == None:
        try:
            if curdir.endswith('DerPi'):
                to_open = 'data\\os.mvh'
                datafile = open(to_open, 'r')
            else:
                to_open = '..\\..\\data\\' + curdir.split('\\')[len(curdir.split('\\')) - 1] + '.mvh'
                datafile = open(to_open, 'r')
        except:
            return {}
    else:
        try:
            if curdir.endswith('DerPi'):
                to_open = 'data\\' + app + '.mvh'
                datafile = open(to_open, 'r')
            else:
                to_open = '..\\..\\data\\' + app + '.mvh'
                datafile = open(to_open, 'r')
        except OSError:
            raise NameError ('Unknown app ' + app)
    try:
        curdata = eval(datafile.read())
        datafile.close()
    except OSError:
        curdata = {}
    if key == None:
        return curdata
    else:   
        try:
            return curdata[str(key)]
        except KeyError:
            return None

def sendSMS(number, sms_txt):
    tx('AT+CMGF=1')
    num = ''
    for i in str(number):
        if i in '1234567890':
            num += i
    tx('AT+CMGS="' + num + '"')
    tx(sms_txt)
    tx(ctrl('z'))
    
#app end messages
class SignalException(Exception):
    def __init__(self):
        pass
class Shutdown(SignalException):
    def __init__(self):
        pass
class EndApp(SignalException):
    def __init__(self):
        pass

if __name__ == "__main__":
    sendSMS(1234567890, 'hi')
    print(rx())
    uart.close()

