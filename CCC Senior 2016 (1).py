word1 = input()
word2 = input()
list1 = [0] * len(word1)
list2 = [0] * len(word2)
counter = 0
counterPrime = 0
counter3 = 0
size = len(list2)
checker = [0] * size
for n in range(0, len(word1)):
   list1[n] = word1[n]
for w in range(0, len(word2)):
   list2[w] = word2[w]
   if word2[w] == "*":
       counterPrime += 1

if len(list1) == len(list2):
   for i in range(0, len(list1)):
       for j in range(0, len(list1)):
           if list2[i] == list1[j]:
               checker[counter] = list2[i]
               counter += 1
               list1[j] = 4
               break

checker.reverse()
for i in range (0, counterPrime):
   checker[i] = "a"
for i in range(0, len(list1)):
   if checker[i] == 0:
      counter3 += 1

if counter3 >= 1:
   print("N")
else:
   print("A")
      
