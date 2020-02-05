str = "Hello!.. how are you? we'll couldn't"
special_char = {}
output = ""
count = 0
for char in str:
    if char.isalpha() or char == " ":
        output += char
    else:
        special_char[count] = char
    count += 1
output = " ".join([a[::-1] for a in output.split(" ")])

for key, value in special_char.items():
    output = output[:key] + value + output[key:]
            
print(output)
