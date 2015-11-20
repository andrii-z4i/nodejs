# C1 := {establish_connection, close_connection, send_data, receive_data}
# C2 := {build_url, build_payload, parse_data}
# 
# C3 := {send_data_by_url}
# Client ==> C3 (network)

class Connection(object):
    def __init__(self, url):
        super(Connection, self).__init__()
        self._url = url

    def send(self, data, callback):
        new_data = {"raw_data": "hello"}
        print "sending data to url %s" % self._url
        callback(new_data)


class Network(object):
    def __init__(self):
        super(Network, self).__init__()
        self._data = None

    def establish_connection(self, url):
        print "establishing connection..."
        return Connection(url)

    def close_connection(self, conection):
        print "destroying connection..."
        del conection

    def send_data(self, conection, data):
        print "sending data..."
        conection.send(data, self.receive_data)

    def receive_data(self, data):
        print "receiving data..."
        self._data = data

    def get_data(self):
        print "returning data..."
        return self._data

class Parser(object):
    def __init__(self):
        super(Parser, self).__init__()

    def build_url(self, host, port):
        print "building url...."
        return "http://%s:%d/" % (host, port)

    def build_payload(self, data):
        print "building payload...."
        return {"data": data}

    def parse_data(self, data):
        print "parsing raw data...."
        return data["raw_data"] 

class SystemFacade(object):
    def __init__(self):
        super(SystemFacade, self).__init__()
        self._network_object = Network()
        self._parser = Parser()

    def send_data_by_url(self, host, port, payload):
        _url = self._parser.build_url(host, port)
        _payload = self._parser.build_payload(payload)
        _connection = self._network_object.establish_connection(_url)
        self._network_object.send_data(_connection, _payload)

        _raw_data = self._network_object.get_data()
        self._network_object.close_connection(_connection)
        return self._parser.parse_data(_raw_data)

sender = SystemFacade()
data = sender.send_data_by_url("127.0.0.1", 8080, "Hello world")
print data


