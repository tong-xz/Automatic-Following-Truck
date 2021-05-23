import threading
import recv
import direct
import move


def __resume_distance() -> (float, float):
    """
    Resume the distance from uwb sensor
    """
    to_a = recv.q_to_a.get()
    to_b = recv.q_to_b.get()
    return (to_a, to_b)


def control():
    while (True):
        to_a, to_b = __resume_distance()
        direction, degree = direct.get_direction_degree()

    # threading.Thread(target=recv.avg_distance, name="avg_distance").start()
