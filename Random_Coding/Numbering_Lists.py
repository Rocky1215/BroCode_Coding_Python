userlist = list()
finallist = list()
listnumber = 0
appendnumber = 1
def main():
    while True:
        asklist = input("Enter a word to add to the list. When done, type in 'Finished' - ")
        if asklist == "Finished":
            numbering()
            print(finallist)
            quit()
        else:
            userlist.append(asklist)
def numbering():
    for lists in userlist:
        global listnumber
        global appendnumber
        lists = userlist[listnumber]
        listnumber = str(listnumber)
        appendnumber = str(appendnumber)
        finished_single = lists+"_"+appendnumber
        finallist.append(finished_single)
        listnumber = int(listnumber)
        appendnumber = int(appendnumber)
        listnumber = listnumber + 1
        appendnumber = appendnumber + 1

main()