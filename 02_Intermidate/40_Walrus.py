def expensive_calculation():
    return 100**100**100

value = expensive_calculation()
if value > 10:
    print(value)

if (value := expensive_calculation()) > 10:
    print(value)