# Library Management
class library:
  def __init__(self):
    self.noofbooks = 0
    self.books=[]
        
  def addbooks(self, add ):
    self.books.append(add)
    self.noofbooks = len(self.books)
    # for i in self.books:
    #   print(i)
    # print(f"{self.noofbooks} books are added")
  
  def Showbooks(self):
    
    print(" Recently added book is:",self.books[-1],"\n")
    print(f"The total no books in library are {self.noofbooks}")
    
    # if self.books:
    i=0
    r = ""
    while i < len(self.books):
      if i == len(self.books) - 1:
        r=r+ "and " + self.books[i]
      else:
        r+= self.books[i] + ", "
      i += 1
    return r
        
      # while (self.noofbooks == [self.noofbooks][-1]):

      #   for i in self.books:
      #     print(i,",")
      # else:
      # for i in self.books:
      #     print(i,"and") 
    # print("\n Recently added book is:",self.books[-1])

a1 = library()
a1.addbooks("HARRY potter")
# a1.Showbooks()
a1.addbooks("Rich dad and poor dad")
# a1.Showbooks()
a1.addbooks("Hands on ML")
# a1.Showbooks()
a1.addbooks("Data Science from Scratch")
a1.Showbooks()

  
