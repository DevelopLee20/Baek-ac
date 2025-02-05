string = input()

cut_count = 0
first_cut = 0
count = 0
before_char = ""
for char in string:
    if char == "(" and before_char == "(":
        cut_count += 1
        first_cut += 1
    elif char == ")" and before_char == "(":
        count += cut_count + first_cut
        first_cut = 0
    elif char == ")" and before_char == ")":
        cut_count -= 1
    before_char = char

print(count)
