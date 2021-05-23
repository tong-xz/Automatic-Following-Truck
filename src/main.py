import threading
import recv
import controller


def main():
    # controller init
    threading.Thread(target=controller.control, name="controller").start()


if __name__ == "__main__":
    # execute only if run as a script
    print('start running')
    main()
