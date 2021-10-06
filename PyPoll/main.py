import csv



header = True
#Voter ID,County,Candidate
#12864552,Marsh,Khan

votes = 0
myCandidate = []
myVotes = []
with open("resources/election_data.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if header == True:
            header = False
            pass
        else:
            found = False
            myList = row[0].split(",")
            for x in range(len(myVotes)):
                    if myList[2] == myCandidate[x]:
                        myVotes[x]+=1
                        votes+=1
                        found = True
                    else:
                        pass
                        
            if found == False:
                myVotes.append(1)
                myCandidate.append(myList[2])
                votes+=1

winner = myCandidate[myVotes.index(max(myVotes))]

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")


for x in range(len(myCandidate)):
    print(myCandidate[x] + ": " + str(round(((myVotes[x]/votes)*100))) + "%" + " (" + str(myVotes[x]) + ")") 

    
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")


############################

fl = open("analysis/myfile.txt", "w")

fl.write("Election Results")
fl.write("-------------------------")
fl.write("Total Votes: " + str(votes))
fl.write("-------------------------")


for x in range(len(myCandidate)):
    fl.write(myCandidate[x] + ": " + str(round(((myVotes[x]/votes)*100))) + "%" + " (" + str(myVotes[x]) + ")") 

    
fl.write("-------------------------")
fl.write("Winner: " + str(winner))
fl.write("-------------------------")

