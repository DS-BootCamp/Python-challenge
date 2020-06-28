import csv

with open ('Resources/election_data.csv') as file:
    reader = csv.DictReader(file)

    totVote = 0
    electionResults = {}
    
    # I want to creat an empty dict, creat keys of candidate names, values of the occurances..
    # If the candidiate is already in as a key, I incremint the frequency..
    # If not, creat a new key, with frequency set = 1
    # wile looping, count the rows
    
    # define how I'm counting frequencies (or occurances) (or setting start point for them)
    for row in reader:
        candidate = row['Candidate']

        if candidate in electionResults:
            electionResults[candidate] += 1
        else:
            electionResults[candidate] = 1

        totVote += 1
    print(totVote)
# print frequency for each candidate
    print(electionResults)  
# print each candidate frequency divided by the total in %

#compare these frequencies to each other, and declare the largest a winner

#export a text file!


#In addition, your final script should both print the analysis to the terminal 
 (,)
#with open("output.txt", "a") as f:
    #print("Hello StackOverflow!", file=f)
    #print("I have a question.", file=f)