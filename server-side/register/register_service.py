import FPS, sys

def checkFingerPress():
    fps.SetLED(True) # Turns ON the CMOS LED
    FPS.delay(0.1) # wait 1 second
    print 'Checking finger presence... Put your finger in the scanner...'
    presenceCount = 0
    while True:
        if fps.IsPressFinger():
            presenceCount += 1
            if presenceCount == 3:
                print 'Your finger is in the scanner!'
                FPS.delay(0.1)
                fps.SetLED(False)
                FPS.delay(0.5)
                print 'Enrolled fingerprints: ' + str(fps.GetEnrollCount())
                FPS.delay(0.5)
                fps.Close()
                return
        FPS.delay(0.1)

def cycleUntilPressed(fps, delayTimer = 0.5):
    presenceCount = 0
    while True:
        if fps.IsPressFinger():
            presenceCount += 1
            if presenceCount == 3:
                FPS.delay(delayTimer)
                return
        FPS.delay(delayTimer)

def cycleUntilNotPressed(fps, delayTimer = 0.5):
    recentPresses = 5
    while True:
        if fps.IsPressFinger():
            continue
        else:
            recentPresses -= 1
            if recentPresses == 0:
                FPS.delay(delayTimer)
                return
        FPS.delay(delayTimer)

def capture(fps, phase, delayTimer = 0.5):
    print 'Place your fingerprint now and please keep it pressed'
    fps.SetLED(True)
    FPS.delay(delayTimer)
    cycleUntilPressed(fps)
    if phase == 1:
        print 'Starting 1st phase of enrollment, please do not lift your finger...'
        if fps.CaptureFinger() == False:
            print 'Something went wrong while capturing your fingerprint'
            return False
        else:
            FPS.delay(delayTimer)
            if fps.Enroll1() != 0:
                print 'Some error occured at Enroll1'
                return False
            FPS.delay(delayTimer)
            print '1st phase complete. Please lift your finger for a moment...'
            fps.SetLED(False)
            FPS.delay(delayTimer)
            cycleUntilNotPressed(fps)
            return True
    elif phase == 2:
        print 'Starting 2nd phase of enrollment, please do not lift your finger...'
        if fps.CaptureFinger() == False:
            print 'Something went wrong while capturing your fingerprint'
            return False
        else:
            FPS.delay(delayTimer)
            if fps.Enroll2() != 0:
                print 'Some error occured at Enroll2'
                return False
            FPS.delay(delayTimer)
            print '2nd phase complete. Please lift your finger for a moment...'
            fps.SetLED(False)
            FPS.delay(delayTimer)
            cycleUntilNotPressed(fps)
            return True
    elif phase == 3:
        print 'Starting final phase of enrollment, please do not lift your finger...'
        if fps.CaptureFinger() == False:
            print 'Something went wrong while capturing your fingerprint'
            return False
        else:
            FPS.delay(delayTimer)
            if fps.Enroll3() != 0:
                print 'Some error occured at Enroll3'
                return False
            FPS.delay(delayTimer)
            print 'Final phase complete. Fingerprint has been registered!'
            fps.SetLED(False)
            FPS.delay(delayTimer)
            return True

def enrollFingerprint(delayTimer = 0.5):
    fps = FPS.FPS_GT511C3(device_name='/dev/ttyAMA0', baud=9600, timeout=2, is_com=False)
    fps.UseSerialDebug = False
    print 'Starting fingerprint enroll process...'
    # Taken ids: 0 (stoia), 1 (stoia), 69 (cu informatii in db), 100, 101
    id = 169
    if fps.EnrollStart(id) != 0:
        print 'Some error occured at EnrollStart'
        FPS.delay(delayTimer)
    	fps.Close()
        return -1
    FPS.delay(delayTimer)
    for i in xrange(1, 4):
        if not capture(fps, i):
	    FPS.delay(delayTimer)
            fps.Close()
            return -1
    return id
        
def fingerprintID(fps, delayTimer = 0.5):
    print 'Starting fingerprint mathing...'
    print 'Place your fingerprint now and please keep it pressed'
    fps.SetLED(True)
    FPS.delay(delayTimer)
    cycleUntilPressed(fps)
    if fps.CaptureFinger() == False:
            print 'Something went wrong while capturing your fingerprint'
            return False
    FPS.delay(delayTimer)
    id = fps.Identify1_N()
    if id == 200:
        print 'No match found'
    else:
        print 'Fingerprint matched with id: ' + str(id)
    FPS.delay(delayTimer)
    fps.SetLED(False)
    FPS.delay(delayTimer)
    
    
'''        
if __name__ == '__main__':
    fps = FPS.FPS_GT511C3(device_name='/dev/ttyAMA0',baud=9600,timeout=2,is_com=False)
    fps.UseSerialDebug = False
    enrollFingerprint(fps)
##    fingerprintID(fps)
##    if fps.CheckEnrolled(0) == True:
##        print '0 is enrolled'
##    FPS.delay(0.5)
##    if fps.CheckEnrolled(69) == True:
##        print '69 is enrolled'
##    FPS.delay(0.5)
##    if fps.CheckEnrolled(100) == True:
##        print '100 is enrolled'
##    FPS.delay(0.5)
##    if fps.CheckEnrolled(57) == True:
##        print '57 is enrolled'
##    FPS.delay(0.5)
##    print 'Enrolled fingerprints: ' + str(fps.GetEnrollCount())
    FPS.delay(0.5)
    fps.Close()
'''
#enrollFingerprint()
