import threading
import recv

# port initialize
uwb_port0, uwb_port1 = recv.serial_init_port()

# Threads initialize
uwb_thread = threading.Thread(target=recv.__get_uwb_distance, args=(
    uwb_port0, uwb_port1), name="uwb_threading")
uwb_thread.start()

# def main():
#     while True:
#         move.turn_left(0.2)
#         time.sleep(4)
#         move.turn_right(0.2)
#         time.sleep(4)
#         move.forward(0.2)
#         time.sleep(4)
#         move.backward(0.2)
#         time.sleep(4)


if __name__ == "__main__":
    # execute only if run as a script
    print('start running')
    main()
