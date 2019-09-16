import csv
from numpy.random import randint

with open('user-account.csv', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    nicknames = []
    for row in reader:
        nicknames.append(row[0])

friends={}
followers={}
for nick in nicknames:
    friends[nick] = []
    followers[nick] = []

for nick in nicknames:
    candidate_friends = [f for f in nicknames if f not in friends[nick] and f != nick]
    nb_friends = randint(0, len(candidate_friends))
    missing_friends = nb_friends - len(friends[nick])
    if missing_friends > 0:
        for i in range(0, missing_friends):
            pick_friend = randint(0, len(candidate_friends))
            if candidate_friends[pick_friend] not in friends[nick]:
                friends[nick].append(candidate_friends[pick_friend])
                friends[candidate_friends[pick_friend]].append(nick)

for nick in nicknames:
    candidate_followers = [f for f in nicknames if f not in friends[nick] and f!=nick]
    nb_followers = randint(0, len(candidate_followers))
    for i in range(0, nb_followers):
        pick_follower = randint(0, len(candidate_followers))
        if candidate_followers[pick_follower] not in followers[nick]:
            followers[nick].append(candidate_followers[pick_follower])

with open('relationship.csv', encoding='utf8', mode='w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['nickname_src', 'nickname_dst', 'type', 'date'])
    for nick in nicknames:
        for friend in friends[nick]:
            writer.writerow([nick, friend, 'friendship', '2009/04/03'])
        for follower in followers[nick]:
            writer.writerow([follower, nick, 'follower', '2009/04/03'])
