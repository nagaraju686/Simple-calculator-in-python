# small example of class and object   
# class A:
#     def skills(s):
#         print("class a")
# class B:
#     def disp(s):
#         print("class b")

# obj=A()
# obj.skills()


# while using a constructor

# class student:
#     def __init__(self,sid,sname,smarks,snum):
#         self.sid=sid
#         self.sname=sname
#         self.smarks=smarks
#         self.snum=snum
#     def disp(self):
#         print(self.sid,self.sname,self.smarks,self.snum)

# s1=student(101,"nagalakshmi",950,80)
# s2=student(102,"nagaraju",750,76)
# s1.disp()
# s2.disp()

# create a book list 
class book:
    def __init__(self,price,title,rt):
        self.price=price
        self.title=title
        self.rt=rt
    def disp(self):
        print(self.price,self.title,self.rt)
    

b1=book(101,"python",200)
b2=book(102,"html",300)
b3=book(103,"css",400)
b4=book(104,"javascript",500)
b1.disp()
b2.disp()
b3.disp()
b4.disp()



        



