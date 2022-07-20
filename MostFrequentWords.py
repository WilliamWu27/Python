from collections import Counter
Topnumber = input("Top: ")
StupidThing = input("Paste your goddamn paragraph thing")
Topnumberr = int(Topnumber)
split_it = StupidThing.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(Topnumberr)
  
print(most_occur)