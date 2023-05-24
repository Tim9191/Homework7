#Task 34


def check_rhythm(poem):
    lines = poem.split() 

    for line in lines:
        words = line.split('-') 

        syllables = []
        for word in words:
            count = sum(1 for char in word if char.lower() in 'aeiouаеёиоуыэюя')  
            syllables.append(count)

        if syllables.count(syllables[0]) != len(syllables):  
            return "Пам парам"

    return "Парам пам-пам"


poem_input = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem_input)
print(result)




#Task 36


def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            result = operation(row, column)
            print(result, end='\t')
        print()

def multiplication(x, y):
    return x * y

print_operation_table(multiplication, num_rows=4, num_columns=5)


