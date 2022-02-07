with open("input4.txt") as input1:
    input_list=[]
    for line in input1.readlines():
        line = line.rstrip()
        line = line.split(" ")
        input_list.append(line)

total=[]
row_and_column=[]
new_list=[]
total_score=0
neighbor = []

def dublication(list1,list2): # to avoid list dublication
    for item in list2:
        if item in list1:
            pass
        else:
            list1.append(item)


def neighbor_search(x,y,list1): # finding related ball and put its index into list
    dublication(total,[(x,y)])
    search_neighbor=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    actual=[]
    for (a,b) in search_neighbor:
        if a <= len(list1)-1 and b <= len(list1[0])-1 and a>=0 and b>=0:
            actual.append((a,b))
    actual.sort()
    for (a,b) in actual:
        if list1[a][b] == list1[x][y] and total.count((a,b)) == 0:
            neighbor.append((a,b))
            dublication(total,neighbor)
    if len(total) == 1 :
        total.clear()
        return total
    elif len(neighbor) == 0:
        return total
    else:
       try:
        neighbor.sort()
        for i in range(len(neighbor)):
            a= neighbor[0][0]
            b = neighbor[0][1]
            neighbor.pop(0)
            neighbor_search(a, b, list1)
        return total
       except IndexError:
           return total


def bomb(x, y, list1,list2,list3):  # it finds chain bomb range while doing that calculate total score
    total_score = 0
    row = [(x, y) for y in range(len(list1[x]))]
    column = [(x, y) for x in range(len(list1))]
    list1[x][y] = "A"
    dublication(list3,row+column)
    list3.sort()
    new_list2=[]
    for (a,b) in list3:
        if list1[a][b]=="X":
            new_list2.append((a,b))
            dublication(list2,new_list2)
            list1[a][b]="A"
    if len(list2)==0:
        set(list3)
        for (a, b) in list3:
            ball = list1[a][b]
            total_score += score_calculate_x(ball)
        return total_score
    else:
        try:
            list2.sort()
            for i in range(len(list2)):
                a = list2[0][0]
                b = list2[0][1]
                list2.pop(0)
                del new_list2
                bomb(a, b, list1,list2,list3)
            set(list3)
            for (a, b) in list3:
                ball = list1[a][b]
                total_score += score_calculate_x(ball)
            return total_score
        except IndexError:
            set(list3)
            for (a, b) in list3:
                ball = list1[a][b]
                total_score += score_calculate_x(ball)
            return total_score


def delete(set1,list1):  # turn elemnts to A which its index stored in row_and_colum(chain bomb range)
    try:                   # and delete all A in input_list
        set1.sort()
        for (a, b) in set1:
            list1[a][b] = "A"
        n=0
        while n<= len(list1):
            if list1[n][0]=="A" and list1[n][-1]=="A":
                list1.pop(n)
            n+=1
        for i in range(len(list1)):
            while "A" in list1[i]:
                list1[i].remove("A")
    except IndexError:
        for i in range(len(list1)):
            while "A" in list1[i]:
                list1[i].remove("A")


def score_calculate_x(ball_type): # to calculate chain bomb score
    if ball_type == "B":
        current_score = 9
        return current_score
    elif ball_type == "G":
        current_score = 8
        return current_score
    elif ball_type == "W":
        current_score = 7
        return current_score
    elif ball_type == "Y":
        current_score = 6
        return current_score
    elif ball_type == "R":
        current_score = 5
        return current_score
    elif ball_type == "P":
        current_score = 4
        return current_score
    elif ball_type == "O":
        current_score = 3
        return current_score
    elif ball_type == "D":
        current_score = 2
        return current_score
    elif ball_type == "F":
        current_score = 1
        return current_score
    elif ball_type == "X" or ball_type == "A" or ball_type==" ":
        current_score = 0
        return current_score


def score_calculate(ball_type,list1): # to calculate other ball
    if ball_type == "B":
        current_score = 9 * len(list1)
        return current_score
    elif ball_type == "G":
        current_score = 8 * len(list1)
        return current_score
    elif ball_type == "W":
        current_score = 7 * len(list1)
        return current_score
    elif ball_type == "Y":
        current_score = 6 * len(list1)
        return current_score
    elif ball_type == "R":
        current_score = 5 * len(list1)
        return current_score
    elif ball_type == "P":
        current_score = 4 * len(list1)
        return current_score
    elif ball_type == "O":
        current_score = 3 * len(list1)
        return current_score
    elif ball_type == "D":
        current_score = 2 * len(list1)
        return current_score
    elif ball_type == "F":
        current_score = 1 * len(list1)
        return current_score
    elif ball_type == "X" :
        current_score = 0
        return current_score


def falling(list1,list2):  # input_list,total,to falling ball which is not used for chain bomb
    if len(list2)==0:
        return list1
    else:
        list2.sort()
        for (a,b) in list2:
            if a >0:
                if list1[a][b]==" " and list1[a-1][b] !=" ":
                    list1[a][b] = list1[a-1][b]
                    list1[a - 1][b] = " "
            list2.sort()
        if list2[-1][0] == 0:
            return list1
        else:
            list2[:]=[(a-1,b) for (a,b) in list2]
            falling(list1,list2)
            return list1


def del_blank_column(list1):  # input_list, to delete empty column
    try:
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                if (list1[0][y]== " ") and (list1[-1][y]== " ") :
                    n=0
                    while n<= len(list1):
                        list1[n][y]="A"
                        n+=1
    except IndexError:
        for i in range(len(list1)):
            while "A" in list1[i]:
                list1[i].remove("A")


for line in input_list:   # opening screen
    print(" ".join(map(str, line)))
print()
print("Your score is: 0")
print()

t=0
while t==0:
    input_list_index = set() #realising game over
    is_neighbor_exit = []
    blank=set()
    x_list=set()
    for x in range(len(input_list)):
        for y in range(len(input_list[0])):
            input_list_index.add((x, y))
    for (x, y) in input_list_index:
        if input_list[x][y] == " " :
            blank.add((x, y))
    for (x, y) in input_list_index:
        if input_list[x][y] == "X" :
            x_list.add((x, y))
    input_list_index.difference_update(blank)
    input_list_index.difference_update(x_list)
    list(input_list_index).sort()
    for (x, y) in input_list_index:
        neighbor_search(x, y, input_list)
        if len(total) > 0:
            is_neighbor_exit.append((x, y))
    total.clear()
    new_list.clear()
    if (len(x_list)==0 and len(is_neighbor_exit)==0) or len(input_list)==0:
        print("Game over!")
        t=1
    else:
        rc = input("Please enter a row and column number: ")  # taking input
        print()
        rc_list = rc.split(" ")
        x = int(rc_list[0])
        y = int(rc_list[1])
        if x == int(x) and y == int(y) and x <= len(input_list) - 1 and y <= len(input_list[0]) - 1 and input_list[x][y] != " ":  # handling wrong input
            ball_type = input_list[x][y]
            if ball_type == "X":  # bomb chain
                current_score = bomb(x, y, input_list, new_list, row_and_column)
                delete(row_and_column, input_list)
                if " " in input_list[-1]:
                    del_blank_column(input_list)
                for line in input_list:
                    print(" ".join(map(str, line)))
                print()
                total_score = total_score + current_score
                row_and_column.clear()

            elif ball_type != "X":  # other balls
                neighbor_search(x, y, input_list)
                for (a, b) in total:
                    input_list[a][b] = " "
                falling(input_list, total)
                if " " in input_list[-1]:
                    del_blank_column(input_list)
                try:
                    for x in range(len(input_list)):
                        if input_list[x].count(" ") == len(input_list[x]):
                            input_list.pop(x)
                        else:
                            break
                except IndexError:
                    len(input_list)
                for line in input_list:
                    print(" ".join(map(str, line)))
                print()
                total_score = total_score + score_calculate(ball_type, total)
                total.clear()
                new_list.clear()
            print("Your score is: " + str(total_score))
            print()
        else:
            print("Please enter a valid size")  # warning message
            print()



