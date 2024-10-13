id: str = "Ido Hamrany Rosh-Ha'ayin"
#exc a
print (len(id))

#exc b
print (id.upper())

#exc c
print (id.lower())

#exc d
print (id.startswith(("Ido")))
#exc e
print (id.endswith("Rosh-Ha'ayin"))

#exc f
print (id.split(" "))

#exc g
id2: str = id.replace(" ","*")
print (id2.split("*"))

#exc h
print (id.center(50,"="))

#exc i
print(id[3:-1])

#exc j
print (id[0:4])

#exc k
print (id[2:-1:2])

#exc l
print(id.title())