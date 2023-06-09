# Import dependencies
import pandas as pd
import os

#Create ROOT_DIR to overcome relative pathing issues as discussed in ReadMe
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
#Create CSV ingest path
csvpath = os.path.join(ROOT_DIR, "Resources", "election_data.csv")
#Create TXT output path
outputpath = os.path.join(ROOT_DIR, "Analysis", "output.txt")

# Import data and store in dataframe
df = pd.read_csv(csvpath)

# Calculate total number of votes using len() and store in variable
total_votes = len(df['Ballot ID'])

# Get list of all candidates using .unique() and store in variable
candidates = df['Candidate'].unique()

#Group by candidates and count number of votes from each and store in DF
df_votes_candidate = df.groupby(['Candidate'])['Ballot ID'].count().reset_index(name='Votes')

#add column with vote percentage:
df_votes_candidate['VotePercentage'] = df_votes_candidate['Votes']/total_votes

# Calculate the winer using idmax() and store in variable
winner = df_votes_candidate.loc[df_votes_candidate['Votes'].idxmax()]

# Display the output in terminal
print('Election Results')
print('-----------------------')
print(f"Total Votes: {total_votes}")
print('-----------------------')
print(f"{df_votes_candidate.loc[0][0]}: {((df_votes_candidate.loc[0][2]*100).round(3))}% ({df_votes_candidate.loc[0][1]}) ")
print(f"{df_votes_candidate.loc[1][0]}: {((df_votes_candidate.loc[1][2]*100).round(3))}% ({df_votes_candidate.loc[1][1]}) ")
print(f"{df_votes_candidate.loc[2][0]}: {((df_votes_candidate.loc[2][2]*100).round(3))}% ({df_votes_candidate.loc[2][1]}) ")
print('-----------------------')
print(f"Winner: {winner[0]}")
print('-----------------------')

#File output to text file 
with open(outputpath, 'a') as f:
    print('Election Results', file=f)
    print('-----------------------', file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print('-----------------------', file=f)
    print(f"{df_votes_candidate.loc[0][0]}: {((df_votes_candidate.loc[0][2]*100).round(3))}% ({df_votes_candidate.loc[0][1]}) ", file=f)
    print(f"{df_votes_candidate.loc[1][0]}: {((df_votes_candidate.loc[1][2]*100).round(3))}% ({df_votes_candidate.loc[1][1]}) ", file=f)
    print(f"{df_votes_candidate.loc[2][0]}: {((df_votes_candidate.loc[2][2]*100).round(3))}% ({df_votes_candidate.loc[2][1]}) ", file=f)
    print('-----------------------', file=f)
    print(f"Winner: {winner[0]}", file=f)
    print('-----------------------', file=f)