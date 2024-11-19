n=input('enter the number')
n=int(n)
def sum_of_digits(n):

    while n >= 10:
      sum = 0
      while  n > 0:
        sum += n % 10
        n //= 10


      n = sum
    return sum
print(sum_of_digits(n))



str1=input('enter string')

def str_compress(str1):
  compress = " "
  length = len(str1)


  i = 0
  while i < length:
    count =1
    char = str1[i]


    while i +1 < length and str1[i] == str1[i+1]:
      count += 1
      i += 1
    compress += char + str(count)
    i += 1
  return compress
print(str_compress(str1))