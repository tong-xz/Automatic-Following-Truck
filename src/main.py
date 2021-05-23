import move
import time


def main():
    while True:
        move.turn_left(0.2)
        time.sleep(4)
        move.turn_right(0.2)
        time.sleep(4)
        move.forward(0.2)
        time.sleep(4)
        move.backward(0.2)
        time.sleep(4)


if __name__ == "__main__":
    # execute only if run as a script
    print('start running')
    main()
