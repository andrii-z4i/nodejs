import threading
import logging
import time


class DoCalculations(threading.Thread):

    def __init__(self, start, finish, semaphore, control, logging):
        super(DoCalculations, self).__init__()
        self._from = start
        self._to = finish
        self._logger = logging
        self._results = []
        self._semaphore = semaphore
        self._control_thread = control

    def run(self):
        self._control_thread.register(self)
        with self._semaphore:
            self._logger.debug("start run (%s)" % self.ident);
            for i in range(self._from, self._to):
                time.sleep(0.1)
                self._results.append(i*i*i)
            self._logger.debug("finish run (%s)" % self.ident);
        self._control_thread.unregister(self)

    def get_results(self):
        return self._results


class ControlThread(object):

    def __init__(self, event, logging):
        super(ControlThread, self).__init__()
        self._objects = []
        self._lock = threading.Lock()
        self._event = event
        self._logger = logging

    def register(self, thread):
        with self._lock:
            self._objects.append(thread.ident)
            self._logger.debug("registered %s thread" % thread.ident)

    def unregister(self, thread):
        with self._lock:
            if thread.ident in self._objects:
                self._objects.remove(thread.ident)
                self._logger.debug("unregistered %s thread" % thread.ident)
            if not len(self._objects):
                self._event.set()
                self._logger.debug("notifying the waiter")



if __name__ == '__main__':
    semaphore = threading.Semaphore(5)
    logging.basicConfig(level=logging.DEBUG)
    event = threading.Event()
    c_thread = ControlThread(event, logging)
    threads = [DoCalculations(i*100, i*100 + 10, semaphore, c_thread, logging) for i in range(100)]

    for thread in threads:
        thread.start()

    event.wait()
    logging.debug("finished")
    for thread in threads:
        print thread.get_results()


