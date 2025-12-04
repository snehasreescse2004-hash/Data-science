a={"sneha","priya","raga","srindhini"}
a.add("kavi")
print(a)

a.update(["anni","pooja"])
print(a)

a.remove("anni")
print(a)

a.discard("meena") #not in list
print(a)

a.pop()
print(a)

a.clear()
print(a)

a={"sneha","priya","raga"}
b={"divya","ramya","raga"}
c=a.union(b)
print(c)

c=a.intersection(b)
print(c)

c=a.symmetric_difference(b)
print(c)

c=a.symmetric_difference_update(b)
print(c)

a={"sneha","priya","raga"}
b={"divya","ramya","raga"}
c=a.isdisjoint(b)
print(c)

a={"sneha","priya","raga"}
b={"divya","ramya","raga"}
c=a.difference(b)
print(c)