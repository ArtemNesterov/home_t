#сумма списка при помощи for and while

#a = {23: "Goo", 43: "Beak", 54: "Jump", 33: "Back"}
#for i in enumerate(a):
 #   print(i)



#summ = 0
#for i in range(1, 30):
 #   summ += 1
  #  print(summ)



#sum1 = 0
#sup = 0
#while sum1 < 22:
 #   sup += sum1
  #  sum1 += 1
   # print(sum1)


#вывести программу выводит сама себя
#import sys
#filename = sys.argv[0]
#f = open(filename, "r")
#for line in f:
    #print(line)
#f.close()


#программу, которая выводит саму себя задом наперед
#import sys
#filename = sys.argv[0]
#f = open(filename, "r")
#l = list(f)#обвернуть в лист
#for line in reversed(l):
 #   print(line)
#f.close()



#Банкомат выдает сумму максимально возможными купюрами
a = int(input("Enter your number"))
lis = [1000, 500, 200, 100, 50, 20, 10, 5]
count = 0 #cheker
