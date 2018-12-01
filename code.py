# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)
f.close()

#print(data)
# Find data type of the file
type_of_data = type(data)
print("type of data is: ",type_of_data)

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print("the city in which the IPL match was played: ", city)

venue = data['info']['venue']
print("the venue of the IPL match was: ", venue)

# which teams played the match
#print(data['info'])
team1 = data['info']['teams'][0]
team2 = data['info']['teams'][1]
print('The match was played between ', team1,'and',team2)

# Which are all the teams that played in the tournament ? How many teams participated in total?

# Which team won the toss and what was the decision of toss winner ?
decision = data['info']['toss']['decision']
toss_winner = data['info']['toss']['winner']
print("the toss was won by ",toss_winner," and the decision was ",decision)

# Find the first bowler and first batsman who played the first ball of the first inning
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print("the first ball was played by ",first_batsman,"and"," bowled by",first_bowler)

# How many deliveries were delivered in first inning ?
deliveries_1st = len(data['innings'][0]['1st innings']['deliveries'])
print("Deliveries bowled in the 1st innings were ",deliveries_1st)

# How many deliveries were delivered in second inning ?
#print(data['innings'][1]['2nd innings']['deliveries'])

deliveries_2nd = len(data['innings'][1]['2nd innings']['deliveries'])
print("Deliveries bowled in the 2nd innings were ",deliveries_2nd)

# Which team won and how ?
how = data['info']['outcome']['by']['runs']
winner = data['info']['outcome']['winner']
print(winner," won by",how,"runs")



