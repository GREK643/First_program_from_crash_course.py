V = [1,2,3]
s = [0,0,0]

for j in range(V):
    imax = 0
    for i in range(len(V)):
      if (V[i]/(2 * s[i] + 1)) > (V[imax]/(2 * s[imax] + 1)):
        imax = i

    s[imax] = s[imax] + 1

print (s)
