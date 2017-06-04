import fingerpi as fp
import time

DELAY_TIME = 0.1
BAUD_RATE = 115200

def CycleUntilPressed(f):
    presence_count = 0
    while presence_count < 5:
        response = f.IsPressFinger()
        if response[0]['Parameter'] == 0:
            presence_count += 1
        time.sleep(DELAY_TIME)

def CycleUntilNotPressed(f):
    presence_count = 10
    while not presence_count <= 0:
        response = f.IsPressFinger()
        if not response[0]['Parameter'] == 0:
            presence_count -= 1
        time.sleep(DELAY_TIME)

def CheckFingerPress(f):
    f.CmosLed(True)
    time.sleep(DELAY_TIME)
    print 'Checking finger presence... Put your finger in the scanner...'
    finger_pressed = 0
    while True:
        response = f.IsPressFinger()
        if response[0]['Parameter'] == 0:
            print 'Finger is pressed!'
        else:
            print 'Finger is not pressed!'
        time.sleep(DELAY_TIME)

def capture(f, phase):
    print 'Place your fingerprint now and please keep it pressed'
    f.CmosLed(True)
    time.sleep(DELAY_TIME)
    CycleUntilPressed(f)
    if phase == 1:
        print 'Starting 1st phase of enrollment, please do not lift your finger...'
        print f.CaptureFinger(True)
        time.sleep(DELAY_TIME)
        print f.Enroll1()
        time.sleep(DELAY_TIME)
        print '1st phase complete. Please lift your finger for a moment...'
        f.CmosLed(False)
        time.sleep(DELAY_TIME)
        CycleUntilNotPressed(f)
    elif phase == 2:
        print 'Starting 2nd phase of enrollment, please do not lift your finger...'
        print f.CaptureFinger(True)
        time.sleep(DELAY_TIME)
        print f.Enroll2()
        time.sleep(DELAY_TIME)
        print '2nd phase complete. Please lift your finger for a moment...'
        f.CmosLed(False)
        time.sleep(DELAY_TIME)
        CycleUntilNotPressed(f)
    elif phase == 3:
        print 'Starting final phase of enrollment, please do not lift your finger...'
        print f.CaptureFinger(True)
        time.sleep(DELAY_TIME)
        print f.Enroll3()
        time.sleep(DELAY_TIME)
        f.CmosLed(False)
        time.sleep(DELAY_TIME)
                
## Doesn't really work...
def EnrollFingerPrint(f):
##  100: left thumb 101: right thumb
    id = 50
    print 'Starting fingerprint enroll process...'
    print f.EnrollStart(id)
    time.sleep(DELAY_TIME)
    for phase in xrange(1, 4):
        capture(f, phase)
    print 'Fingerprint enroll completed, registered at id: ' + str(id)

def MatchID(id):
    f = fp.FingerPi(port = '/dev/ttyAMA0')
    print 'Opening connection...'
    f.Open(extra_info = False, check_baudrate = False)
    time.sleep(DELAY_TIME)
    print 'Setting baudrate to: ' + str(BAUD_RATE)
    f.ChangeBaudrate(BAUD_RATE)
    time.sleep(DELAY_TIME)
    print 'Starting fingerprint matching, please put your finger in the scanner...'
    f.CmosLed(True)
    time.sleep(DELAY_TIME)
    CycleUntilPressed(f)
    f.CaptureFinger(False)
    time.sleep(DELAY_TIME)
    f.CmosLed(False)
    time.sleep(DELAY_TIME)
    response = f.Identify()
##  Modified base.py line 107 to make this work    
    if response[0]['ACK']:
	if id == response[0]['Parameter']:
		print 'Given id matched with fingerprint id!'
	else:
		print 'Given id does not match with fingerprint id!'
    else:
	print 'Your fingerprint did not match with any stocked fingerprint!' 
    print 'Closing connection...'
    f.Close()

'''
if __name__ == '__main__':
    f = fp.FingerPi(port = '/dev/ttyAMA0')
    print 'Opening connection...'
    f.Open(extra_info = False, check_baudrate = False)
    time.sleep(DELAY_TIME)
    print 'Setting baudrate to: ' + str(BAUD_RATE)
    f.ChangeBaudrate(BAUD_RATE)
    time.sleep(DELAY_TIME)
##    EnrollFingerPrint(f)
##    print f.GetEnrollCount()
##    GetFingerID(f)
##    CheckFingerPress(f)
    f.DeleteAll()
    print 'Closing connection...'
    f.Close()
'''
MatchID(0)
