import multiprocessing 
import logging
import time
from multiprocessing.managers import BaseManager
from multiprocessing import Manager


logger = multiprocessing.get_logger()
logger.setLevel(logging.INFO)
logger.info("starting")

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s/%(processName)s]%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class DoCalculations(multiprocessing.Process):

    def __init__(self, start, finish, semaphore, control):
        super(DoCalculations, self).__init__()
        self._from = start
        self._to = finish
        self._logger = logger
        self._results = []
        self._semaphore = semaphore
        self._control_thread = control

    def run(self):
        self._control_thread.register(self.ident)
        with self._semaphore:
            self._logger.debug("start run (%s)" % self.ident);
            for i in range(self._from, self._to):
                time.sleep(0.1)
                self._results.append(i*i*i)
            self._logger.debug("finish run (%s)" % self.ident);
        self._control_thread.unregister(self.ident, self._results)

    def get_results(self):
        return self._results

class ControlManager(BaseManager):
    pass


class ControlThread(object):

    def __init__(self, event):
        super(ControlThread, self).__init__()
        self._objects = []
        self._lock = multiprocessing.Lock()
        self._event = event
        self._logger = logger

    def __init__(self):
        super(ControlThread, self).__init__()
        self._objects = []
        self._results = {}
        self._lock = multiprocessing.Lock()
        self._event = None 
        self._logger = logger 

    def set_event(self, event):
        self._event = event

    def set_results_container(self, results):
        self._results = results

    def __str__(self):
        return "<%s: %s>" % ("ControlThread", self._objects)

    def register(self, thread_id):
        with self._lock:
            self._objects.append(thread_id)
            self._logger.info("registered %s thread in %s" % (thread_id, self))

    def unregister(self, thread_id, results):
        with self._lock:
            if thread_id in self._objects:
                self._objects.remove(thread_id)
                self._results[thread_id] = results
                self._logger.info("unregistered %s thread" % thread_id)
            if not len(self._objects):
                self._event.set()
                self._logger.info("notifying the waiter")

    def results(self):
        return self._results



if __name__ == '__main__':

    ControlManager.register('ControlThread', ControlThread)

    manager = ControlManager()
    common_manager = Manager()
    manager.start()

    semaphore = common_manager.Semaphore(5)
    logger.info('info from main process')

    event = common_manager.Event()
    c_thread = manager.ControlThread()
    c_thread.set_event(event)
    threads = [DoCalculations(i*100, i*100 + 10, semaphore, c_thread) for i in range(100)]

    for thread in threads:
        thread.start()

    event.wait()
    logger.info("finished")
    
    for item in c_thread.results():
        print item, c_thread.results()[item]


