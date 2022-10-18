import random

def gen_team():
    return [round(random.uniform(5, 10), 2) for _ in range(20)]

team_a = gen_team()
team_b = gen_team()

match = [max(team_a[i], team_b[i]) for i in range(len(team_a))]
print(team_a)
print(team_b)
print(match)
