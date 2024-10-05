from services import ServiceManager
from services.fake_worker import FakeWorker
from services.new_api import SimpleApi
from services.simple_server import SimpleServer


def main():
    try:
        sm = ServiceManager()
        stop_signal = sm.stop_flag

        sm.add_service(FakeWorker(stop_signal))
        sm.add_service(SimpleServer(stop_signal))
        sm.add_service(SimpleApi(stop_signal))

        sm.start()
        sm.wait_for_stop()

    except KeyboardInterrupt:
        sm.stop()


if __name__ == "__main__":
    main()