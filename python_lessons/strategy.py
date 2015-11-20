from abc import abstractmethod, ABCMeta  # abstract methods
from random import randint
#     Base (Human)    <--- Call center manager (what is your name? what is your age? Do you want to buy our product?) 
# 		^ ^------------------
#		| 					|
#  Specific1 (Old man)  Specific2 (Young wooman)


class IStrategy(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def do_prepare(self):
		pass

	@abstractmethod
	def do_behave(self):
		pass

	@abstractmethod
	def do_finish(self):
		pass


class RunFaster(IStrategy):
	"""docstring for RunFaster"""
	def __init__(self):
		super(RunFaster, self).__init__()
		
	def do_prepare(self):
		print "I am ready"

	def do_behave(self):
		print "I am running very fast"

	def do_finish(self):
		print "I finish my run"


class RunSlowly(IStrategy):
	"""docstring for RunSlowly"""
	def __init__(self):
		super(RunSlowly, self).__init__()
		
	def do_prepare(self):
		print "I am ready"

	def do_behave(self):
		print "I am running very slow" 

	def do_finish(self):
		print "I finish my run"


class Human(object):

	def __init__(self, name):
		super(Human, self).__init__()
		self._weather = 0
		self._health = 0  # -1 - bad/ 0 - so..so / 1 - very good
		self._name = name

	def wakeup(self):
		print "%s: I am waking up..." % (self._name)

	def check_weather(self, degree):
		self._weather = degree

	def check_health(self, health):
		self._health = health

	# IStrategy * make_decision_how_to_run() {
	#	return new RunFaster();
	# }	

	#  -------------
	#  | IStrategy | 
	#  -------------
	#  | RunFaster |
	#  -------------
	#

	def make_decision_how_to_run(self):
		if self._weather > 15 and self._health >= 0:
			return RunFaster()
		else:
			return RunSlowly()

	def do_run(self):
		print "==========="
		object_run = self.make_decision_how_to_run()  # IStrategy
		object_run.do_prepare()
		object_run.do_behave()
		object_run.do_finish()
		print "==========="


for i in range(10):

	human = Human(str(i + 1000))

	human.wakeup()
	human.check_health(randint(-1, 1))
	human.check_weather(randint(10, 20))
	human.do_run()