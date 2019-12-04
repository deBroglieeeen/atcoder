n = int(input())
r = input()
a,b,c,d,f = r.count("A"),r.count("B"),r.count("C"),r.count("D"),r.count("F")
print((4 * a + 3 * b + 2 * c + 1 * d + 0 * f) / n)