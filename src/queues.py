from queue import Queue, Full
from abc import ABC, abstractmethod
from typing import Any
from enum import Enum
import uuid


class QueueBase(ABC):
    @abstractmethod
    def add_to_queue(self, topic: str, message):
        pass

    @abstractmethod
    def list_queue(self):
        pass

    @abstractmethod
    def de_queue_all(self):
        pass

    @abstractmethod
    def de_queue_one(self):
        pass


class QueueOverflowPolicy(Enum):
    BLOCK = "block"
    REJECT = "reject"
    DROP_OLDEST = "drop_oldest"


class Queues(QueueBase):
    """Object to create queues."""

    def list_queue(self):
        pass

    # Initialize a queue. If there is no name given, give it a random UUID id.
    def __init__(self, queue_id=None, max_size: int = 0):
        self.queue = Queue(maxsize=max_size)
        if queue_id is None:
            self.queue_id = uuid.uuid4()
        else:
            self.queue_id = queue_id

    # Add a topic and a message to the Queue.
    # Open ended to allow different type of messages
    def add_to_queue(self, topic: str, message: Any):
        try:
            post = {
                "topic": topic,
                "message": message
            }
            self.queue.put_nowait(post)
        except Full:
            raise ValueError(f"Queue is full. Maxsize was: {self.queue.maxsize}")

    # Dequeues all elements at ones. FIFO.
    def de_queue_all(self):
        try:
            for i in range(0, self.queue.qsize()):
                q = self.queue.get()
                print(self.queue_id, q)
        except Exception as e:
            print(e)

    # Dequeues one at a time. FIFO.
    def de_queue_one(self):
        try:
            q = self.queue.get()
            return q
        except Exception as e:
            print(e)
