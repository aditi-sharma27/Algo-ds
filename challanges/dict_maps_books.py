
n =3
a = [["sam", 99912222], ["tom", 11122222], ["harry", 12299933]]
# sam
# edward
# harry

print(a)
book = {}
for i in range(n):
    name, no = a[i]
    print(name, no)
    book[name] = no

print(book)

find_out = ["sam", "edward", "harry"]

for name1 in find_out:
    result = book.get(name1, "Not found")

    print("{}={}".format(name1, str(result)))

find_out = ["sam", "edward", "harry"]
print(map(int, find_out.split()))
