import time 
# Code : 

raw_books = ["Harry Potter","Rich Dad Poor Dad","Atomic Habits","The Alchemist","To Kill a Mockingbird","The Subtle Art of Not Giving a F*ck","Death Note","The Psychology of Money"]
books = [i.title() for i in raw_books]

emojis = ["📘","📕","📗" ]

class Users :
  
  
  def __init__(self, username) :
    self.username = username.title()
  
  def get_user(self) :
    return self.username

  def display_books (self) :
    print(f"\n🟢 Available Books : {len(books)} \n")
    time.sleep(0.15)
    print("\n-------------------------------\n")
    for i,book in enumerate(books) :
       time.sleep(0.15)
       print(f"# - {emojis[i % len(emojis)]} {book}")
    print("\n-------------------------------\n")
       

  def  borrow_book(self) :

    while True :

      try :
          self.book_name_to_borrow  = input("\n 🟢 Enter the Name of the book to Borrow :  ")
          self.cleaned_name_to_borrow = ' '.join(self.book_name_to_borrow.strip().split()).title()

      except ValueError:
        time.sleep(0.15)
        print("\n❌Invalid Book Name ! Please Try Again \n ")

      if self.cleaned_name_to_borrow in books : 
        break
      else : 
        time.sleep(0.15)
        print("\n❌Invalid Book Name ! Please Try Again \n ")
            
     
        

    while True : 
      try :
          if self.cleaned_name_to_borrow in books :
            time.sleep(0.21)
            self.borrow_time = int(input("\nEnter the number of Days you would like to borrow the Book for 📅 :  "))
      
            if self.borrow_time > 7 :
              
             print("\n ⚠️ we can't issue a book for more than 7 Days 📅 !")

            elif self.borrow_time < 1 :
             print("\n❌ Invalid Input ! please Try Again ...")

            else : 
             time.sleep(0.21)
             print(f"\nTotal Amount You need To pay is  ₹  : {self.borrow_time*10} ")
             books.remove(self.cleaned_name_to_borrow)
             break 

          else :
            print(f"⚠️ No Book found with Name : {self.cleaned_name_to_borrow}")
            
      except ValueError:
          print("\n ❌ Invalid Input ! please Try Again ...")

  def return_book(self):

        self.book_name_to_return = input("📥 Enter the name of the book you'd like to return : ")
        self.cleaned_name_of_book = ' '.join(self.book_name_to_return.strip().split()).title()

        if self.cleaned_name_of_book not in books :
         books.append(self.book_name_to_return)
         time.sleep(0.15)
         print(f"The Book {self.book_name_to_return} has been Returned Successfully ! ✅ \n")
         print("---------------------------------------------")

        elif self.cleaned_name_of_book  in books :

          print(f"\n ⚠️ {self.book_name_to_return} Already Exists ")
          time.sleep(0.21)

          print(" 🔁 If you don't have any book then Enter \"exit\" ")
          time.sleep(0.21)

          print("\n 👉:  ")

          exit_confirmation = input().strip().split()

          if exit_confirmation == "exit" :
            time.sleep(0.21)
            print("----------Exit Successfull------------")
            exit()

        

  def anything_else(self) :

     while True :

      try :
        print(f"\n 🔁 AnyThing else ?\n ")
        
        time.sleep(0.25) 
        print("Enter : \n")

        time.sleep(0.25)
        print("🔸 1️⃣  To View the Options \n")

        time.sleep(0.25)
        print("🔸 2️⃣  To Exit \n ")

        time.sleep(0.21)

        self.final_confirmation = int(input("👉  :  "))

        if self.final_confirmation == 1 :
          self.menu_flow(),
          break

        elif self.final_confirmation == 2  :
          time.sleep(0.15)
          print("Exited Successfully !✅ ")
          break

        else : 
          print("Enter Either 1 or 2 ! ")

      except ValueError: 
        print("❌ Invalid Input ! Please Try Again ")

                 
  def menu_flow(self) :
    time.sleep(0.15)
    print("\n===== 📚 Welcome to the Library =====\n")
    time.sleep(0.15)
    print("1️⃣  Display Books 📚")
    time.sleep(0.15)
    print("2️⃣  Borrow a Book 📚")
    time.sleep(0.15)
    print("3️⃣  Return a Book 📚")
    time.sleep(0.15)
    print("4️⃣  Exit 👋")  
    
    while True : 
      try : 
        time.sleep(0.55)
        self.option = int(input("\n Enter your choice : "))
        break
      except ValueError:
        print("❌ Invalid Input !  Choose any of the Option from below : \n  ")


    match(self.option) :

      case 1 : self.display_books(), self.anything_else()

      case 2 : self.display_books(), self.borrow_book(), self.anything_else()

      case 3 : self.return_book(),self.anything_else()
      
      case 4 : time.sleep(0.23), print(f"Thanks for visiting the Library. Goodbye! {self.username}👋 "),exit()


# Object creation :
time.sleep(0.15)

print("\n------- Library Management System v1.0 ----------\n")
time.sleep(0.15)


print("------- Developed by: Junaid Syed -------")
time.sleep(0.15)

print("\n🟢 Please Enter Your UserName  To Access the Library :")
time.sleep(0.15)

name = input("\n Enter Your UserName : ")
time.sleep(0.15)

print(f"\n===== 👋 Hello , {name.title()} ! ====")

obj1 = Users(name)
obj1.menu_flow()



