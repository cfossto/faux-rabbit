from queue import Queue
import uuid


class Queues:
    """Object to create queues."""

    # Initialize a queue. If there is no name given, give it a random UUID id.
    def __init__(self, queue_id=None):
        self.our_queue = Queue()
        if queue_id is None:
            self.queue_id = uuid.uuid4()
        else:
            self.queue_id = queue_id

    # Add a topic and a message to the Queue.
    # Open ended to allow different type of messages
    def add_to_queue(self, topic: str, message):
        item = {
            "topic": topic,
            "message": message
        }
        self.our_queue.put(item)

    # Dequeues all elements at ones. FIFO.
    def de_queue_all(self):
        try:
            for i in range(0, self.our_queue.qsize()):
                q = self.our_queue.get()
                print(self.queue_id, q)
        except Exception as e:
            print(e)

    # Dequeues one at a time. FIFO.
    def de_queue_one(self):
        try:
            q = self.our_queue.get()
            return q
        except Exception as e:
            print(e)
