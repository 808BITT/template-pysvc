from threading import Thread, Event


class StopFlag(Event):
    '''
    A flag to stop all services.
    '''
    def __init__(self):
        super().__init__()


class Service(Thread):
    '''
    A base class for services that run in their own thread.


    Must implement the run method in subclass.
    
    Args:
        stop (Event): An instance of threading.Event to stop the service
        name (str): The name of the service
        daemon (bool): Whether the service is a daemon thread
    '''
    def __init__(self, stop: StopFlag, **kwargs):
        name = kwargs.get("name", "Service")
        daemon = kwargs.get("daemon", False)
        
        assert isinstance(stop, Event), "stop must be an instance of threading.Event"
        assert isinstance(name, str), "name must be a string"
        assert isinstance(daemon, bool), "daemon must be a boolean"

        super().__init__(name=name, daemon=daemon)
        self.stop = stop
        # super().start()

    def run(self):
        raise NotImplementedError("You must implement the run method in your subclass")


class ServiceManager:
    def __init__(self):
        self.stop_flag = Event()
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def start(self):
        for service in self.services:
            service.start()

    def wait_for_stop(self):
        for service in self.services:
            service.join()

    def stop(self):
        print("Stopping services...")
        self.stop_flag.set()
        for service in self.services:
            service.join()
        print("Services stopped")

