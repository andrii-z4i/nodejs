import random

class ServiceManager(object):

	def __init__(self):
		super(ServiceManager, self).__init__()
		self._observers = {}

	def on(self, car_type, observer_object):
		if car_type not in self._observers:
			self._observers[car_type] = []

		self._observers[car_type].append(observer_object)
		print "%s and I registered for waiting for %s" % (observer_object, car_type)


	def notify(self, car_type):
		if car_type not in self._observers:
			return

		for observer_object in self._observers[car_type]:
			observer_object.update()

class Client(object):

	def __init__(self, name, surname):
		super(Client, self).__init__()
		self._name = name
		self._surname = surname

	def update(self):
		print "received notification for %s %s" % (self._name, self._surname)

	def __repr__(self):
		return "I am %s %s" % (self._name, self._surname)

	def __str__(self):
		return "I am %s %s" % (self._name, self._surname)


clients = [Client(str(random.randint(111,999)), str(random.randint(1111,9999))) for i in range(10)]

manager = ServiceManager()
manager.on('VW Golf VII', clients[0])
manager.on('VW Golf VII', clients[1])
manager.on('VW Golf VII', clients[2])
manager.on('VW Golf VII', clients[3])
manager.on('Lada Kalina', clients[4])
manager.on('Lada Kalina', clients[5])
manager.on('Lada Kalina', clients[6])
manager.on('VW Toareg', clients[7])
manager.on('VW Toareg', clients[8])
manager.on('VW Toareg', clients[9])


manager.notify('VW Toareg')
manager.notify('Lada Kalina')
manager.notify('VW')