from queues import Queues


q = Queues("testing queue")
q.addToQueue("greeting","hello")
q.addToQueue("info","next in line")
q.deQueue()