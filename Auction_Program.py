def registration(age,name):
   uid = (age ** len(name)) * 2
   temp = uid
   sum = 0
   for i in range(len(str(uid))):
       sum = sum + temp % 10
       temp //= 10
   uid = ((uid % 1000) * 10) + (sum % 10)
   return uid

registeredParticipantsUID = []
registeredParticipantsAge = []
registeredParticipantsName = []
runs = [0,0,0,0,0]

for q in range(5):
   age = int(input("Age "))
   if age > 4 and age < 14:
      name = input("Name ")
      registeredParticipantsAge.append(age)
      registeredParticipantsName.append(name)
      registeredParticipantsUID.append(registration(age,name))

print(registeredParticipantsUID)

timing = []
for week in range(3):
   timingWeek = []
   for race in range(5):
       UserUid = int(input("Identification Number "))
       bool = False
       for checker in registeredParticipantsUID:
           if checker == UserUid:
               bool = True
       if bool:
           timingUser = int(input("Timings "))
           runs[registeredParticipantsUID.index(UserUid)] += 1
           timingWeek.append(timingUser)
       else:
           timingWeek.append(10000)
   timing.append(timingWeek)

PB = []
BandStatus = []
for w in range(5):
   x = 10000
   for c in range(3):
       if timing[c][w] < x:
           x = timing[c][w]
   PB.append(x)

for num in runs:
   if num > 1:
       BandStatus.append("Full Marathon")
   elif num > 0:
       BandStatus.append("Half Marathon")
   else:
       BandStatus.append("No band Go home!")

for final in range(5):
   print(registeredParticipantsName[final] + "has PB: {} ".format(PB[final]) + " and Band: " + BandStatus[final])

print()

bestLow = []
bestMid = []
bestHigh = []
for q in PB:
   lastStep = registeredParticipantsAge[PB.index(q)]
   if lastStep <= 6:
       bestLow.append(q)
   elif lastStep <= 10:
       bestMid.append(q)
   else:
       bestHigh.append(q)

WinnerJunior = registeredParticipantsName[PB.index(min(bestLow))]
WinnerMid = registeredParticipantsName[PB.index(min(bestMid))]
WinnerSenior = registeredParticipantsName[PB.index(min(bestHigh))]

print("Winner Kids " + WinnerJunior)
print("Winner Mids " + WinnerMid)
print("Winner Seniors" + WinnerSenior)
