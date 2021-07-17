result = True
another_result = result

print(id(result))   #4558666448
print(id(another_result))   #4558666448

result = False
print(id(result))   #4553833136

# because booleans are immutable, we can not change the value of true
# what python does is it rebound result to a new value, False

result = "Correct"
another_result = result
print(id(result))   #140259094790064
print(id(another_result))   #140259094790064

result += "ish"
print(id(result))   #140517064721712
print(another_result)   # Correct
print(id(another_result))   #140259094790064