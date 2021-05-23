from queue import Queue
import gpiozero
import threading

to_a = gpiozero.InputDevice(pin=15, pull_up=True)

q = Queue()
counter = 0


def load_data():
    while(True):
        print(to_a.value)
        q.put(to_a.value)


def consume_data():
    print(q.qsize())
    while (True):
        # 如果队列不为空
        if not q.empty:
            # 0就不用看
            if q.get == 0:
                q.get(block=False)
            else:
                if q.get(block=False) == 1 and q.get(block=False) == 1:
                    op1 = q.get(block=False)
                    op2 = q.get(block=False)
                    print(f"<{op1},{op2}>")


threading.Thread(target=load_data).start()
threading.Thread(target=consume_data).start()
