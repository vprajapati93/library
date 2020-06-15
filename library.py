

class Library:


    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.dictionary={}


    def viewbook(self):
        print(f"Books available are")
        for book in self.booklist:
            print(book)

    def addbook(self,book):
        self.booklist.append(book)
        print("books are updated")


    def lendbook(self,user,book):
        if book not in self.dictionary.keys():
            self.dictionary.update({book:user})
            print("updated")
        else:
            print(f"book is beinf bt{self.dictionary[book]} ")


    def returnbook(self,book):
        self.dictionary.pop(book)




if __name__ == '__main__':

    vishal = Library(["pyhton", "c++", "hacker one", "jeff bezos", "the fault in our star"], "VISHAL'S LIBRARY")
    while(True):
        print("ENTER TO OUR LIBRARY........ENTER YOUR CHOICE TO PROCCED\n"
            "1.view books\n"
            "2.add books\n"
            "3.lend books\n"
            "4.return books\n ")
        choise=int(input("enter your choice"))

        if choise==1:
            vishal.viewbook()

        elif choise==2:
            book=input("enter the book you want to add")
            vishal.addbook(book)

        elif choise==3:
            book=input("enter the book you want")
            user=input("name")
            vishal.lendbook(user,book)


        elif choise==4:
            book= input("enter")
            vishal.returnbook(book)


        else:
            print("enter valid input")


        print("press q to quit and c continer")

        a=input()

        if a=="q":
            quit()
        if a=="c":
            continue