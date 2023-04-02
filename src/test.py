import random
from bubble_sort import  bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from shell_sort import shell_sort

any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]

if __name__ == "__main__":
    test_cases = {
                    'Números aleatórios': any_numbers, 
                    'Já ordenados': already_sorted, 
                    'Ordem inversa': inversed, 
                    'Elementos repetidos': repeated,
                }

    print("*******************************")
    for name, list in test_cases.items():
        print("\nCaso de teste: {}".format(name))
        print(list)
        shell_sort(list)
        print("\n Ordenado:")
        print(list)
    print("*******************************")