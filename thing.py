print("Enter 5 numbers to order from least to greatest: ")
one = input("1: ")
two = input("2: ")
three = input("3: ")
four = input("4: ")
five = input("5: ")
def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]       
        if not swapped:
            return
 
elements = [one, two, three, four, five]
 
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)