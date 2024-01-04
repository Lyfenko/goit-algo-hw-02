import queue
import time
from faker import Faker

fake = Faker()


class RequestProcessor:
    def __init__(self):
        self.request_queue = queue.Queue()

    def generate_request(self):
        request_data = {
            "number": int(time.time()),
            "type": fake.word(),
            "description": fake.sentence(),
        }
        self.request_queue.put(request_data)
        print(f"Створено новий запит: {request_data}")

    def process_request(self):
        """Обробляє заявку, якщо черга не порожня."""
        if not self.request_queue.empty():
            processed_request = self.request_queue.get()
            self._handle_request(processed_request)
        else:
            print("Черга порожня. Заявок для обробки немає.")

    @staticmethod
    def _handle_request(request):
        print(f"Обробка запиту #{request['number']} - {request['type']}: {request['description']}")
        time.sleep(1)
        print(f"Запит #{request['number']} оброблено.")

    def main_loop(self, interval=1):
        while True:
            self.generate_request()
            self.process_request()
            time.sleep(interval)


if __name__ == "__main__":
    request_processor = RequestProcessor()
    request_processor.main_loop()
