
def main():
    while True:
        turn_left(0.2)
        sleep(4)
        turn_right(0.2)
        sleep(4)
        forward(0.2)
        sleep(4)
        backward(0.2)
        sleep(4)


if __name__ == "__main__":
    # execute only if run as a script
    main()
