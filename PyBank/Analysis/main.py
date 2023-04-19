#Import dependencies:
import pandas as pd
import os
#Create ROOT_DIR to overcome relative pathing issues as discussed in ReadMe
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
#Create CSV ingest path
csvpath = os.path.join(ROOT_DIR, "Resources", "budget_data.csv")
#Create TXT output path
outputpath = os.path.join(ROOT_DIR, "Analysis", "output.txt")

#Import csv
df = pd.read_csv(csvpath)

#Calculate number of months:
num_months =  len(df['Date'].unique())

#Calculate profit and loss total
pnl = sum(df['Profit/Losses'])

#Calculate total profit and loss:
avg_pnl = (df['Profit/Losses']).mean()

#Calculate max profit:
max_pnl = df.loc[df['Profit/Losses'] == df['Profit/Losses'].max()]

#Calculate max gain:
#Set initial value
max_gain = 0

#loop through rows 2 to len()
for i in range(1, len(df['Profit/Losses'])):
    #setup for loop to check if current cell difference from last month is greater than max_gain
    if (df['Profit/Losses'][i] - df['Profit/Losses'][i - 1]) > max_gain:

        #update value of max_gain
        max_gain = df['Profit/Losses'][i] - df['Profit/Losses'][i - 1]

        #update value of max_gain_date
        max_gain_date = df['Date'][i]


#Calculate max loss:
#Set initial value
max_loss = 0

#loop through rows 2 to len()
for i in range(1, len(df['Profit/Losses'])): 

    #setup for loop to check if current cell difference from last month is greater than max loss
    if (df['Profit/Losses'][i] - df['Profit/Losses'][i - 1]) < max_loss:

        #update value of max_loss
        max_loss = df['Profit/Losses'][i] - df['Profit/Losses'][i - 1]
               
        #update value of max_loss_date
        max_loss_date = df['Date'][i]


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
profits_losses = df["Profit/Losses"]

# use list comprehension to calculate the changes in profit/losses over the entire period
changes = [profits_losses[i+1] - profits_losses[i] for i in range(len(profits_losses)-1)]

# calculate the average of the changes
average_change = sum(changes) / len(changes)

#Final output

print('Financial Analysis')
print('---------------------------')
print(f"Total Months: {num_months}")
print(f"Total: ${pnl}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase In Profits: {max_gain_date} (${max_gain})")
print(f"Greatest Decrease In Profits: {max_loss_date} (${max_loss})")

#Output to output.csv
with open(outputpath, 'a') as f:
    print('Financial Analysis', file=f)
    print('---------------------------', file=f)
    print(f"Total Months: {num_months}", file=f)
    print(f"Total: ${pnl}", file=f)
    print(f"Average Change: ${round(average_change, 2)}", file=f)
    print(f"Greatest Increase In Profits: {max_gain_date} (${max_gain})", file=f)
    print(f"Greatest Decrease In Profits: {max_loss_date} (${max_loss})", file=f) 