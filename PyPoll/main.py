import csv

with open ('Resources/election_data.csv') as file:
    reader = csv.DictReader(file)

    totVote = 0
    electionResults = {}
    
    # I want to creat an empty dict, creat keys of candidate names, values of the occurances..
    # If the candidiate is already in as a key, I incremint the frequency..
    # If not, creat a new key, with frequency set = 1
    # wile looping, count the rows

    # define how I'm counting frequencies (or occurances)
    for row in reader:
        candidate = row['Candidate']
        
        if candidate in electionResults:
            electionResults[candidate] += 1
        else:
            electionResults[candidate] = 1

        totVote += 1
    print("Election Results")
    print("Total number of voters was",totVote)
    # print each candidate frequency divided by the total in %
    for candidate in electionResults.keys():
        voteCount = electionResults[candidate]
        percentage = 100 * voteCount/ int(totVote)
        #electionResults[candidate].append(percentage)
# print frequency for each candidate
        print("Candidate",candidate,"got", percentage, "% of the votes, which is equl to", voteCount,"votes")  
#compare these frequencies to each other, and declare the largest a winner
    highestVotes = 0
    winner = None
    for candidate in electionResults.keys():
        if  voteCount > highestVotes:
            highestVotes = voteCount
            winner = candidate
    print("The election winner is",winner)

#export a text file!

with open("MyPyPollOutput.txt", "a") as f:
    print("Election Results", file=f)
    print("Total number of voters was",totVote, file=f)
    for candidate in electionResults.keys():
        voteCount = electionResults[candidate]
        percentage = 100 * voteCount/ int(totVote)
        print("Candidate",candidate,"got", percentage, "% of the votes, which is equl to", voteCount,"votes", file=f)  

    print("The election winner is",winner, file=f)