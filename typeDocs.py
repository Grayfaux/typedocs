with open("functions.py", "r") as code:
    read_code = code.readlines()


# for i in read_code:
#     if "# >" in i or "#>" in i or "# h>" in i or "#h>" in i\
#             or "# t>" in i or "#t>" in i:
#
#         print(f"{read_code.index(i)}: {i}")



for i in read_code:
    if "import" in i and read_code.index(i) < 10:
        print(f'{read_code.index(i)}: {i}')

functions = 0
for i in read_code:
    if "def" in i:
        print(f'{read_code.index(i)}: {i.replace("def", "")}')
        functions += 1
print(f"functions: {functions}")


returns = 0
for i in read_code:
    if "return" in i and "#" not in i:
        print(f'{read_code.index(i)}: {i}')
        returns += 1
print(f"returns: {returns}")
