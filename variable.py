nums = (0, 1, 2, 3, 4, 5)

first, *rest = nums
print(f"{first=}, {rest=}")

first, *middle, last = nums
print(f"{first=}, {middle=}, {last=}")

a, b, *c, d = nums
print(f"{a=}, {b=}, {c=},{d=},{nums=}")

x = {nums,...}
print(x)

