def main():
    depths = read_file('input.txt')

    print(sol1(depths, 1))
    print(sol1(depths, 3))

def read_file(filename):
    with open(filename, 'r') as f:
        return [int(l) for l in f.readlines()]

def sol1(depths, distance):
    # Checking whether the sum of the moving window of x items increases is equivalent
    # to checking whether the item at index n is greater than the item at index (n - x)
    return len([1 for i in range(len(depths)) if i >= distance and depths[i] > depths[i - distance]])

if __name__ == "__main__":
    main()
