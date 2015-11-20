import abc

class IDevice(object):

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def forward(self):
        pass

class OldDevice(IDevice):

    def __init__(self):
        super(OldDevice, self).__init__()

    def play(self):
        print "do play"

    def stop(self):
        print "do stop"

    def forward(self):
        print "do forward"


class AdapterDevice(IDevice):

    def set_device(self, device):
        self._device = device

    def fast_forward(self):
        print  "doesn't support by device" 

    def play(self):
        self._device.play()

    def stop(self):
        self._device.stop()

    def forward(self):
        self._device.forward()
     

class Client(object):

    def __init__(self, device):
        self._device = device
    
    def play(self):
        self._device.play()

    def stop(self):
        self._device.stop()

    def forward(self):
        self._device.forward()

    def fast_forward(self):
        self._device.fast_forward()

# introduce base functionality in interface
# modify our old class by inheritance of interface
# study our client to communicate with interface
# introduce adapter hides old functionality of old device
# provide to client adapter

old_device = OldDevice()
adapter = AdapterDevice()
adapter.set_device(old_device)
c = Client(adapter)

c.play()
c.stop()
c.forward()
c.fast_forward()