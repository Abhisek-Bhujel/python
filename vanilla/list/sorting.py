even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)

even.sort(reverse=True)
print(even)

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)   #No sort method for strings only list
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

another_sorted_numbers = numbers.sort()
print(another_sorted_numbers)
print(numbers)