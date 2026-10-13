def suma(x, y):
    return x + y

def pintPriramede(numBase):
    i = 0
    while i < numBase:
        j = i
        for s in range(i):
            print(" ", end="")
        while j + 1 < i:
            print("+", end="")
            j += 1
        print("\n")
        i += 1


if __name__ == "__main__":
    print("Hello world")
    print("La suma es esta" + suma(3, 5))
    pintPriramede(5)

