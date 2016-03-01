#!/usr/bin/python
import time, datetime

print("Hei Pi")

cnt = 1
while cnt <= 10:
  print(cnt)
  cnt = cnt + 1

start = datetime.datetime.now()

print(  datetime.datetime.now() )
for i in range(1000):
  print("1234567890qwertyuiop", i)
        
stop = datetime.datetime.now()

print( start )
print( stop )

print( stop - start)




start = datetime.datetime.now()

print(  datetime.datetime.now() )

x = 0.0
y = 9.9

for i in range(10000):
  x = x + (y*y  - y)/y
  y = y + 0.01

print( 'x = ', x ) 
      
stop = datetime.datetime.now()

print( start )
print( stop )

print( stop - start)
