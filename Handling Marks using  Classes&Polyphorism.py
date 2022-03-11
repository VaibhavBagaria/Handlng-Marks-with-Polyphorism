from tkinter import*
root=Tk()
root.geometry('400x400')
root.configure(bg="aqua")

G3_l=Label(root)
G3_l.place(relx=0.5,rely=0.25,anchor=CENTER)
G5_l=Label(root)
G5_l.place(relx=0.5,rely=0.5,anchor=CENTER)
G10_l=Label(root)
G10_l.place(relx=0.5,rely=0.75,anchor=CENTER)

class grade3():
    def __init__(self,math,english):
        self.math=math
        self.english=english
        
    def percentage(self):
        total_mark=self.math+self.english
        total_mark_percentage=total_mark/2
        G3_l['text']="Your Average Marks For Grade 3 Are: "+str(total_mark_percentage)+"%"
        
class grade5():
    def __init__(self,math,english,science):
        self.math=math
        self.english=english
        self.science=science
        
    def percentage(self):
        total_mark=self.math+self.english+self.science
        total_mark_percentage=total_mark/3
        G5_l['text']="Your Average Marks For Grade 5 Are: "+str(total_mark_percentage)+"%"
        
class grade10():
    def __init__(self,math,english,science,history):
        self.math=math
        self.english=english
        self.science=science
        self.history=history
    
    def percentage(self):
        total_mark=self.math+self.english+self.science+self.history
        total_mark_percentage=total_mark/4
        G10_l['text']="Your Average Marks For Grade 10 Are: "+str(total_mark_percentage)+"%"
        
obj_G3=grade3(100,80)
obj_G5=grade5(95,85,70)
obj_G10=grade10(100,80,80,70)

btn_G3=Button(root,text="Grade 3 Results",bg="aqua",fg="blue",command=obj_G3.percentage).place(relx=0.5,rely=0.35,anchor=CENTER)
btn_G5=Button(root,text="Grade 5 Results",bg="aqua",fg="blue",command=obj_G5.percentage).place(relx=0.5,rely=0.6,anchor=CENTER)
btn_G10=Button(root,text="Grade 10 Results",bg="aqua",fg="blue",command=obj_G10.percentage).place(relx=0.5,rely=0.85,anchor=CENTER)

root.mainloop()