from tkinter import *
import tkinter.messagebox as mb


class Node():
    def __init__(self, value, left_child = None,right_child = None, parent = None,x=None,y=None,h = None,fig = None,text = None,line = None,zn = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.x = x
        self.y = y
        self.h = h
        self.fig = fig
        self.text = text
        self.line = line
        self.zn = zn
    
        
class BinarySearchTree():
    flag = True
    last = 0

    def __init__(self,canvas=None,win=None):
        self.root = None
        self.ar = []
        self.canvas = canvas
        self.win = win
        
    def dop_insert(self):
        self.ar.append(int(self.entry1.get()))
        self.insert(int(self.entry1.get()))
        
    def insert(self,value):
        self.clear_entry()
        if self.root == None:
            self.root = Node(value,x = 750,y = 100,h = 700)
            bst.create_root(self.root)
        else:
            self._insert(value, self.root)

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value,parent = cur_node,x = cur_node.x-(cur_node.h/2),y = cur_node.y+60,h = cur_node.h/2)
                cur_node.left_child.zn = 'left'
                cur_node.left_child.parent = cur_node
                bst.create_node(cur_node.left_child)
                
            else:
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value, parent = cur_node,x = cur_node.x+(cur_node.h/2),y = cur_node.y+60,h = cur_node.h/2)
                cur_node.right_child.zn = 'right'
                cur_node.right_child.parent = cur_node
                bst.create_node(cur_node.right_child)
                
            else:
                self._insert(value,cur_node.right_child)
        else:
            pass
            #print('Node is exist')
            #mb.showinfo("", 'Node is exist')
            
            
    def print_tree(self):
        if self.root != None:
            self._print_tree_inOrder(self.root)
        else:
            print('Binary Search Tree is empty')

    def _print_tree_inOrder(self, cur_node):
        if cur_node != None:
            self._print_tree_inOrder(cur_node.left_child)
            print(cur_node.value)
            self._print_tree_inOrder(cur_node.right_child)

    def clear2(self):
        self.canvas.delete("all")
        self.root = None

    def clear(self):
        self.canvas.delete("all")
        self.root = None
        self.ar = []
    

    def create_field(self):
        self.win = Tk()
        self.win.title('Бинарное дерево')
        self.win.resizable(0, 0)
        self.canvas = Canvas(self.win, width =1500 , height = 1000)
        self.canvas.pack()

        self.entry1 = Entry()
        self.entry1.place(x = 5,y = 10)

        self.entry2 = Entry()
        self.entry2.place(x = 200,y = 10)

        self.entry3 = Entry()
        self.entry3.place(x = 395,y = 10)
                
        self.btn1 = Button(text = 'Insert',command = bst.check_in)
        self.btn1.place(x = 135,y = 10)

        self.btn2 = Button(text = 'Find',command = bst.check_f)
        self.btn2.place(x = 330,y = 10)
        
        self.btn3 = Button(text = 'Clear the screen',command = bst.clear)
        self.btn3.place(x = 630,y = 10)

        self.btn4 = Button(text = 'Delete',command = bst.check_d)
        self.btn4.place(x = 530,y = 10)

        self.bst = BinarySearchTree()        
        self.canvas.mainloop()

    def create_node(self,cur_node):
        
        cur_node.line = self.canvas.create_line(cur_node.parent.x+7,cur_node.parent.y+7,cur_node.x+7,cur_node.y+7)   
        cur_node.fig = self.canvas.create_oval(cur_node.x,cur_node.y,cur_node.x+15,cur_node.y+15,outline = 'blue',fill = 'white')
        cur_node.text = self.canvas.create_text(cur_node.x+7,cur_node.y+7,text = str(cur_node.value))
        self.canvas.lower(cur_node.line)

    def create_root(self,cur_node):
        cur_node.fig = self.canvas.create_oval(cur_node.x,cur_node.y,cur_node.x+15,cur_node.y+15,outline = 'blue',fill = 'white')
        cur_node.text =  self.canvas.create_text(cur_node.x+7,cur_node.y+7,text = str(cur_node.value))

    def dop_find(self):
        self.find(int(self.entry2.get()))
        
    def find(self,x):
        
        if self.root.value == x:
            self.find_config(self.root)
            self.clear_entry()
            
        else:
            self._find(x,self.root)
                
                
            
    def _find(self,x,cur_node):
        if cur_node == None:
            self.canvas.itemconfig(bst.last,fill = 'white')
            mb.showinfo("", 'There is no such node in the tree')
            self.clear_entry()
        elif x<cur_node.value:
            self._find(x,cur_node.left_child)
        elif x>cur_node.value:
            self._find(x,cur_node.right_child)
        elif x == cur_node.value:
            
            self.find_config(cur_node)
            self.clear_entry()
            return cur_node

    def find_config(self,cur_node):
        self.canvas.itemconfig(cur_node.fig,fill = 'yellow')
        bst.flag = False
        bst.last = cur_node.fig

    def check_f(self):
        if self.is_int(self.entry2.get())==True:
            if self.ar.count(int(self.entry2.get()))!=0:
                if bst.flag:
                    self.dop_find()
                else:
                    self.canvas.itemconfig(bst.last,fill = 'white')
                    bst.flag = True
                    self.dop_find()
            else:
                self.canvas.itemconfig(bst.last,fill = 'white')
                mb.showinfo("", 'There is no such node in the tree')
                self.clear_entry()
                
        elif self.is_int(self.entry2.get())==False:                
            self.is_string()
            self.canvas.itemconfig(bst.last,fill = 'white')
        else:
            self.clear_entry()
            self.canvas.itemconfig(bst.last,fill = 'white')
            
    def check_in(self):
        if self.is_int(self.entry1.get())==True:
            if bst.flag and self.ar.count(int(self.entry1.get()))==0:
                self.dop_insert()
            elif bst.flag == False and self.ar.count(int(self.entry1.get()))==0:
                self.canvas.itemconfig(bst.last,fill = 'white')
                bst.flag = True
                self.dop_insert()
            else:
                self.canvas.itemconfig(bst.last,fill = 'white')
                bst.flag = True
                mb.showinfo("", 'Node is exist')
                self.clear_entry()
        elif self.is_int(self.entry1.get())==False:
            self.is_string()
        else:
            self.clear_entry()
            self.canvas.itemconfig(bst.last,fill = 'white')

    def check_d(self):
        if self.is_int(self.entry3.get())==True:
            if bst.flag: 
                self.delete_node(int(self.entry3.get()))            
            else:
                self.canvas.itemconfig(bst.last,fill = 'white')
                bst.flag = True
                self.delete_node(int(self.entry3.get()))
        elif self.is_int(self.entry3.get())==False:
            self.is_string()
        else:
            self.clear_entry()

    def is_int(self,x):
        al = 'qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_=`~ёйцукенгшщзхъфывапролджэ\ячсмитьбю."№;:?,'
        if x!='' and x.count(' ')==0 :
            for i in range(len(x)):
                if al.count(x[i])!=0:
                    return False
            return True
        else:
            return 7
    def clear_entry(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
    
    def is_string(self):
        self.canvas.itemconfig(bst.last,fill = 'white')
        mb.showinfo('','Enter only integers')
        self.clear_entry()
        
    def delete_node(self,x):
        if self.ar.count(int(self.entry3.get()))!=0:
            
            self.ar.remove(int(self.entry3.get()))
            self.clear_entry()
            self.clear2()
            
            self.root = None
            for i in self.ar:
                self.insert(i)
            
        else:
            mb.showinfo("", 'There is no such node in the tree')
            self.clear_entry()


bst = BinarySearchTree()
bst.create_field()

