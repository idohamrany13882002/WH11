import random

# exc a
l1: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(f"l1: {l1}")  # -- to check

# exc b
print ("all True:", all (l1))

# exc c
print ("any True:", any(l1))

# exc d
print ("all False:", not any (l1))

# exc e
print ("any False:", not all (l1) )

# exc f
l2: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(f"l2: {l2}")  # -- to check

# exc g
print ("all different than 0:", all (l2))

# exc h
print ("any different than 0:", any (l2))

# exc i
print ("all is 0:", not any (l2))

# exc j
print ("any is 0:", not all (l2))
