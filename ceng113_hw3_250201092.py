# 250201092

import operator

users = []
friends = []


def add_user(user):

    if user == "":  # check the user name valid or invalid
        print("Wrong input")
        return False
    if user in users: # Check the user name if in the users list
        print("This name already exist.")
        return False
    else:
        users.append(user)  # Append the user name in the user list
        friends.append([])
        print("New user " + user + " is created.")

        return True


def add_friend(user, friend):

    if friend not in users: # Check the friend name in the user list
        print("This name is not exist!!")
        return False
    else:
        if user not in users: # Check the user name in the user list
            print("This name is not exist!")
            return False
        counter = 0
        for i in range(len(users)): # Take an index the user
            if user == users[i]:
                counter = i
        if friend in friends[counter]:
            print("This person has already friend!")
            return False
        if user == friend:
            print("You cannot add yourself as a friend!!")
        else:
            index = 0
            for i in range(len(users)):  # friend name is added to user name as a friend
                if user == users[i]:
                    index = i
            friends[index].append(friend)
            for i in range(len(users)):
                if friend == users[i]:
                    index = i
            friends[index].append(user)
            print(friend + " is added to " + user + " friend list")


def delete_user(del_user):

    if del_user in users:  # Deleted user is removed other users as a friend
        for i in range(len(friends)):
            if del_user in friends[i]:
                friends[i].remove(del_user)
        index = 0
        for i in range(len(users)):
            if del_user == users[i]:
                index = i
        friends.pop(index)
        users.remove(del_user)
        print(del_user + " is now deleted from this network.")
        return True
    else:
        print("This name is not in the users")


def remove_friend(user_friend, rem_friend):

    if rem_friend not in users:
        print("There is no such a person ")
        return False
    if user_friend not in users:
        print("There is no such a person ")
        return False
    index_friend = 0
    index_user = 0
    for i in range(len(users)):
        if user_friend == users[i]:
            index_user = i
        if rem_friend == users[i]:
            index_friend = i
    friends[index_user].remove(rem_friend)
    friends[index_friend].remove(user_friend)
    print(rem_friend + " is now deleted from " + user_friend + " account.")

    return True


def offer_friend(user):

    list_of_mutual_friends = []
# --------  For all users, determined how many common friends  --------------------
    for i in users:
        i_friend_list = []
        for a in range(len(users)):
            if i == users[a]:
                i_friend_list = friends[a]
        for j in users:
            counter = 0
            if i == j:
                continue
            else:
                j_friend_list = []
                for k in range(len(users)):

                    if j == users[k]:
                        j_friend_list = friends[k]
                for person1 in i_friend_list:
                    for person2 in j_friend_list:
                        if person1 == person2:
                            counter += 1
            list_of_mutual_friends.append(counter)
# ------------- end of how many common friends ----------------------------

    if user not in users:
        print("There is no such a user.")
        return False
# --------- Determine friends of the entered user ---------------------
    user_friend_list = []
    for i in range(len(users)):
        if user == users[i]:
            user_friend_list = friends[i]
            break
# ---------end of Determine friends of the entered user --------------
# ---------Determine non friends of the entered user ------------------
    not_friend_list = []
    for i in range(len(users)):
        if user == users[i]:
            continue
        elif users[i] not in user_friend_list:
            not_friend_list.append(users[i])
# ---------end ofDetermine non friends of the entered user ------------------

    x_scaled_list1 = {}

    for i in range(len(not_friend_list)):

        f_list_of_not_friend_user = []
        for a in range(len(users)):
            if not_friend_list[i] == users[a]:
                f_list_of_not_friend_user = friends[a]
                break

        mutual_friend_counter = 0
        for person1 in user_friend_list:

            for person2 in f_list_of_not_friend_user:

                if person1 == person2:
                    mutual_friend_counter += 1
        total_friend_number = mutual_friend_counter / (len(f_list_of_not_friend_user)
                                                       + len(user_friend_list) - mutual_friend_counter)
        x_scaled = ((total_friend_number - min(list_of_mutual_friends)) /
                    (max(list_of_mutual_friends) - min(list_of_mutual_friends)))
        x_scaled_list1[not_friend_list[i]] = x_scaled
    print("Potential friends ")
    dict_list = sorted(x_scaled_list1.items(), key=operator.itemgetter(0))
    for key, values in dict_list:
        print("{} = {} ".format(key, values))

    return True
