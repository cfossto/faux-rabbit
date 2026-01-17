from src.queues import Queues


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

q4 = Queues(max_size=2)

q4.add_to_queue("q4", "first one")
q4.add_to_queue("q4:2", "second one")
print(q4.de_queue_all())
