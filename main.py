from queues import Queues


q = Queues("testing queue")

q.add_to_queue("greeting","hello")
q.add_to_queue("info","next in line")
q.de_queue()


q2 = Queues()
q2.add_to_queue("new topic", "very good")
q2.de_queue()