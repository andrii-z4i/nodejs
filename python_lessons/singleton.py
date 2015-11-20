import random
import threading
import time

class Logger(object):
    __data = {}

    @staticmethod
    def getLogger():
        print Logger.__data
        if 'object' in Logger.__data:
            return Logger.__data['object']
        else:
            Logger.__data['object'] = Logger()
            return Logger.__data['object']

    def __init__(self, **kwargs):
        super(Logger, self).__init__(**kwargs)
        self._log_file = random.randint(10, 100) 

    def __print_me(self):
        print self, self._log_file

    def info(self, text_to_log):
        self.__print_me()
        print "info: %s" % text_to_log

    def warn(self, text_to_log):
        print "warn: %s" % text_to_log

    def err(self, text_to_log):
        print "err: %s" % text_to_log


def do_calculation(a, b, name):
    print "do_calculation <<%s>>" % str(name)
    logger = Logger.getLogger()  # eb50
    logger.info(a)
    logger.info(b)
    time.sleep(random.randint(1, 5))
    c = a + b
    logger.info(c) 

threads = []
for i in range(100):
    threads.append(threading.Thread(target=do_calculation, args=(random.randint(100, 500), random.randint(100, 500), i)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()