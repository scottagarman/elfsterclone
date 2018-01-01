import random
 
def generateNewDraw(buyers, noOneGetsSamePersonAsLastYear, lastYearsDraw):
   global shuffleCount
   receivers = []
   for i in range(len(buyers)):
      receivers.append(buyers[i])
   random.shuffle(receivers)
   shuffleCount += 1
   newDraw = []
   for i in range(len(buyers)):
      if buyers[i] == receivers[i] or (noOneGetsSamePersonAsLastYear and buyers[i] in lastYearsDraw and receivers[i] == lastYearsDraw[buyers[i]]):
         if (i < len(buyers) - 1):
            if buyers[i] == receivers[i + 1]:
               return generateNewDraw(buyers, noOneGetsSamePersonAsLastYear, lastYearsDraw)
            if noOneGetsSamePersonAsLastYear and buyers[i] in lastYearsDraw and receivers[i+1] == lastYearsDraw[buyers[i]]:
               return generateNewDraw(buyers, noOneGetsSamePersonAsLastYear, lastYearsDraw)
            temp = receivers[i]
            receivers[i] = receivers[i + 1]
            receivers[i + 1] = temp
         else:
            return generateNewDraw(buyers, noOneGetsSamePersonAsLastYear, lastYearsDraw)   
      newDraw.append({buyers[i]: receivers[i]})
   return newDraw


lastYearsDraw = {"Rachel": "Jeri",
                "Glenn": "Dave",
                "Jeri": "Lauren",
                "Dave": "Rachel",
                "Lauren": "Glenn"}
noOneGetsSamePersonAsLastYear = True
shuffleCount = 0
buyers = ["Rachel", "Glenn", "Jeri", "Dave", "Lauren"]
random.shuffle(buyers)
newDraw = generateNewDraw(buyers, noOneGetsSamePersonAsLastYear, lastYearsDraw)
results = { "count": shuffleCount, "draw": newDraw }
print results
