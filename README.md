# faux-rabbit
A fake version of a similar queue system for Python. Just for showing an understanding of techniques regarding event based design patterns.

The natural entrypoint to this software is main.py.

# The goal
It is simple: to mimic but not fully recreate software in the likes of RabbitMQ and Kafka.
In this repository I am exploring sockets and socketserver to make endpoints for a digital queue.
You should be able to enqueue and dequeue messages from another client (preferrably Python).

In the best of cases this software will spin up a socket server, handle incoming connections based on paths,
enqueing messages, dequeing the messages (for further processing) and multi-threading support for creating parallell queues.


# Techniques used
Queue, sockets, socketserver, uuid (for randomized queue nameing if no name is given), exception handling and threading.
