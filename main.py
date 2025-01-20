from queues import Queues


q = Queues("testing queue")

q.add_to_queue("greeting","hello")
q.add_to_queue("info","next in line")
q.de_queue_all()


q2 = Queues()
q2.add_to_queue("new topic", "very good")
q2.de_queue_all()

q3 = Queues("Third queue")
q3.add_to_queue("testagain", "third times a charm")
q3.add_to_queue("testagain", "four times a charm")
print(q3.de_queue_one())
print(q3.de_queue_one())
