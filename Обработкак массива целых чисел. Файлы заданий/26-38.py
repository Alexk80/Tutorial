F = open( '26-j9.txt' )

S, N = map( int, F.readline().split() )

a = []
for i in range(N):
  a.append( int(F.readline()) )

a.sort()

last = 0
count = 0
total = 0
iSmall = 0
iLarge = N - 1
while iLarge >= iSmall:
  if total + a[iLarge] <= S:
    total += a[iLarge]
    count += 1
    last = a[iLarge]
    if total + a[iSmall] <= S:
      total += a[iSmall]
      count += 1
      last = a[iSmall]
    else:
      break
  iLarge -= 1
  iSmall += 1

print( count, last )
