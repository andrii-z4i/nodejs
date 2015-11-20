import abc

class OldDevice(object):

    def __init__(self):
        super(OldDevice, self).__init__()

    def play(self):
        print "do play"

    def stop(self):
        print "do stop"

    def forward(self):
        print "do forward"


class AdapterDevice(object):

    def set_device(self, device):
        self._device = device

    def fast_forward(self):
        print  "doesn't support by device" 

    def start_play(self):
        self._device.play()

    def stop_play(self):
        self._device.stop()

    def forward_music(self):
        self._device.forward()
     

class Client(object):

    def __init__(self, device):
        self._device = device
    
    def play(self):
        self._device.start_play()

    def stop(self):
        self._device.stop_play()

    def forward(self):
        self._device.forward_music()

    def fast_forward(self):
        self._device.fast_forward()

# learn our client to communicate with adapter class 
# introduce adapter which hides functionality of old device
# provide to client adapter

old_device = OldDevice()
adapter = AdapterDevice()
adapter.set_device(old_device)
c = Client(adapter)

c.play()
c.stop()
c.forward()
c.fast_forward()