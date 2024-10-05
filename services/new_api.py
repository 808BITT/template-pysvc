from time import sleep
from services import Service


class SimpleApi(Service):
    '''
    A simple API that serves some data
    '''

    def __init__(self, stop):
        super().__init__(stop, name="SimpleApi", daemon=False)
    
    def run(self):
        print("Start 3")
        try:
            while not self.stop.is_set():
                print("API: Serving some data...")
                sleep(2)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("End 3")