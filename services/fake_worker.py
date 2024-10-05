from time import sleep
from services import Service, StopFlag

class FakeWorker(Service):
    '''
    A fake worker that does some work every 3 seconds
    
    Args:
        stop (Event): An instance of threading.Event to stop the worker
    '''

    def __init__(self, stop: StopFlag):
        super().__init__(stop, name="FakeWorker", daemon=False)

    def run(self):
        print("Start 1")
        sleep(1)
        try:
            while not self.stop.is_set():
                print("SVC1: Doing some work...")
                sleep(3)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("End 1")