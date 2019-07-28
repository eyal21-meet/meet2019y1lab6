result = []
for count in range(1, 100):
    if count % 15 == 0:
        result.append("Fizzbuzz")
    elif count % 3 == 0:
        result.append("Fizz")
    elif count % 5 == 0:
        result.append("buzz")
    else: 
        result.append(count)
print(result)
