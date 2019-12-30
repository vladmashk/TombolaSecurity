def test(ar1, ar2=None):
    if ar2 is None:
        ar2 = []
    print(ar1 + ar2)


a1 = [1,2,3]
a2 = [4,5,6]

test(a1)