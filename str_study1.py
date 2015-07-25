#!/usr/bin/env python
s = '  asd 123fd 1df cdew    adff   qwer '
n = 0
m = 0
list = []
while n < len(s) - 1:
   while s[n] == ' ':
      n = n + 1
   m = s.find(' ', n)
   list.append(s[n:m])
   n = m


print list
