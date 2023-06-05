# list comprehension but with () to make it a generator
my_gen = ( x for x in range(10) )
print(my_gen)

# using yeild

def gen():
    for _ in my_gen:
        yield _

gen_two = gen()

print(gen_two)

for _ in gen_two:
    print(_)

# yield test

def yieldOnly():
    yield "A"
    yield "B"
    yield "C"

print(yieldOnly())

def yieldFrom():
    for i in yieldOnly():
        yield i

print(yieldFrom())
# generator comprehension
test = yieldFrom()
for i in test:
    print(i)