# #Pascal's prob
# import random
#
# def rollDie():
#     return random.choice([1,2,3,4,5,6])
#
# def checkPascal(numTrials):
#     for i in range(numTrials):
#         numWins = 0
#         for j in range(24):
#             d1 = rollDie()
#             d2 = rollDie()
#             if d1 == 6 and d2 == 6:
#                 numWins += 1
#                 break
#         print("Prob of win: {}%".format((numWins/numTrials)*100))
#
# checkPascal(100)

#CrapsGame
# import random
# import statistics
#
# def rollDie():
#     return random.choice([1,2,3,4,5,6])
#
# class CrapsGame(object):
#     def __init__(self):
#         self.passWins, self.passLosses = 0,0
#         self.dpWins, self.dpLosses, self.dpPushes = 0,0,0
#     def playHand(self):
#         throw = rollDie() + rollDie()
#         if throw == 7 or throw == 11:
#             self.passWins += 1
#             self.dpLosses += 1
#         elif throw == 2 or throw == 3 or throw == 12:
#             self.passLosses += 1
#             if throw == 12:
#                 self.dpPushes += 1
#             else:
#                 self.dpWins += 1
#         else:
#             point = throw
#             while True:
#                 throw = rollDie() + rollDie()
#                 if throw == point:
#                     self.passWins +=1
#                     self.dpLosses +=1
#                     break
#                 elif throw == 7:
#                     self.passLosses +=1
#                     self.dpWins +=1
#                     break
#
#     def passResults(self):
#         return(self.passWins, self.passLosses)
#
#     def dpResults(self):
#         return(self.dpWins , self.dpLosses,self.dpPushes)
#
# def crapsSim(handsPerGame, numGames):
#     games = []
#
#     #Play numGames games
#     for t in range(numGames):
#         c = CrapsGame()
#         for i in range(handsPerGame):
#             c.playHand()
#         games.append(c)
#
#     #stats
#     pROIPerGame, dpROIPerGame = [],[]
#     for g in games:
#         wins,  losses = g.passResults()
#         pROIPerGame.append((wins-losses)/float(handsPerGame))
#         wins,losses,pushes = g.dpResults()
#         dpROIPerGame.append((wins-losses)/float(handsPerGame))
#
#     #print results
#     meanROI = 100*sum(pROIPerGame)/numGames
#     sigma = 100*statistics.stdev(pROIPerGame)
#     print("Pass: meanROI:{}% Std.dev:{}%".format(meanROI,sigma))
#     meanROI = 100*sum(dpROIPerGame)/numGames
#     sigma = 100*statistics.stdev(dpROIPerGame)
#     print("NotPass: meanROI:{}%, Std.dev:{}%".format(meanROI,sigma))
#
# crapsSim(20,10)

#TableLookUp:faster CrapsGame...use dictionary!
def playHand(self):
    pass

#ThrowNeedles
# import random
# import statistics
# def throwNeedles(numNeedles):
#     inCircle = 0
#     for Needles in range(1, numNeedles + 1):
#         x = random.random()
#         y = random.random()
#         if(x*x + y*y)**0.5 <= 1:
#             inCircle += 1
#     return 3*(inCircle/numNeedles)
#
# def getEst(numNeedles, numTrials):
#     estimates = []
#     for t in range(numTrials):
#         piGuess = throwNeedles(numNeedles)
#         estimates.append(piGuess)
#     sDev = statistics.stdev(estimates)
#     curEst = sum(estimates)/len(estimates)
#     print("Est = {}".format(str(round(curEst,3))) + ' ',
#         "Std. dev. = {}".format(str(round(sDev,3))) + ' ',
#         "Needles = {}".format(numNeedles)+"\n" + "*****")
#     print("* {} *".format(numTrials))
#     return (curEst,sDev)
#
# def estPi(precision, numTrials):
#     numNeedles = 1000
#     sDev = precision
#     while sDev > precision/1.96:
#         curEst, sDev = getEst(numNeedles,numTrials)
#         numNeedles *= 2
#     return curEst
#
# estPi(0.01,200)
