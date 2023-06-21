def fizzBuzz(n):
    answer = []
    i = 1
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i%3 == 0:
            answer.append("Fizz")
        elif i%5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
        i += 1
    return answer

print(fizzBuzz(3))