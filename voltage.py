
def calculation(voltage:float, energy:float, charge:float) -> float:
    if voltage == 0:
        return energy / charge
    elif energy == 0:
        return voltage * charge
    elif charge == 0:
        return energy / voltage
    else:
        return 0.0


def main():
    while True:
        start()     


def start():
    print("Write 0 if unknown")
    v = float(input("Voltage (V): "))
    j = float(input("Energy (J): "))
    c = float(input("Charge (c): "))
    print("This is the result: ", calculation(v, j, c))



if __name__ == "__main__":
    main()