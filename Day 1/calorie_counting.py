def count_calories():
    file = open("input", "r")
    calories_per_elf = [calories.split("\n") for calories in file.read().split("\n\n")]
    sum_calories_per_elf = [sum(map(int, calories)) for calories in calories_per_elf]
    sum_calories_per_elf.sort()

    print(sum_calories_per_elf[-1])
    print(sum(sum_calories_per_elf[-3:]))

if __name__ == '__main__':
    count_calories()

