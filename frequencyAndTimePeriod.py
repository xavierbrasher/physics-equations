
def calculation(frequency:float, time:float) -> float:
    if frequency == 0:
        return 1 / time
    elif time == 0:
        return 1 / frequency
    else:
        return 0.0


def main():
    while True:
        start()     


def start():
    print("Write 0 if unknown")
    t = float(input("Time (s): "))
    f = float(input("Frequency (Hz): "))
    print("This is the result: ", calculation(t, f))



if __name__ == "__main__":
    main()