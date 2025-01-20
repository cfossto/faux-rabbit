from queue import Queue
import uuid

class Queues:

    def __init__(self, queue_id=None):
        self.our_queue = Queue()
        if queue_id is None:
            self.queue_id = uuid.uuid4()
        else:
            self.queue_id = queue_id

    def add_to_queue(self, topic: str, message):
        item = {
            "topic": topic,
            "message": message
        }
        self.our_queue.put(item)

    def de_queue(self):
        try:
            for i in range(0, self.our_queue.qsize()):
                q = self.our_queue.get()
                print(self.queue_id, q)
        except Exception as e:
            print(e)
