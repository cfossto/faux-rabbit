from queue import Queue


class Queues:

    def __init__(self, queue_id):
        self.our_queue = Queue()
        self.queue_id = queue_id

    def addToQueue(self, topic, message):
        item = {
            "topic": topic,
            "message": message
        }
        self.our_queue.put(item)

    def deQueue(self):
        try:
            for i in range(0, self.our_queue.qsize()):
                q = self.our_queue.get()
                print(self.queue_id, q)
        except Exception as e:
            print(e)

