s = input() # https://www.facebook.com/dscareer

s = str.split(s, '//', 1)
s = s[1]
s = str.split(s, '/', 1)
s = s[0]

print(s) # www.facebook.com
