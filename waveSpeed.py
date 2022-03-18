
def calculation(waveSpeed:float, frequency:float, waveLength:float) -> float:
    if waveLength == 0:
        return waveSpeed / frequency
    elif waveSpeed == 0:
        return frequency * waveLength
    elif frequency == 0:
        return waveSpeed / waveLength
    else:
        return 0.0


def main():
    while True:
        start()     


def start():
    print("Write 0 if unknown")
    ws = float(input("Wave speed (m/s): "))
    f = float(input("Frequency (Hz): "))
    wl = float(input("Wave length (m): "))
    print("This is the result: ", calculation(ws, f, wl))



if __name__ == "__main__":
    main()