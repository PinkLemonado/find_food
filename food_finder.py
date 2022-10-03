import wx
import gui
import sqlite3
conn=sqlite3.connect(r"C:\Users\feath\Desktop\table.db")
cur=conn.cursor();

class CalcFrame(gui.MyFrame3):
    def __init__(self,parent):
        gui.MyFrame3.__init__(self,parent)
    def on_choice(self,event):
        tmp=self.ch_box.GetString(self.ch_box.GetSelection())
        #print(tmp)
        return tmp

    def generate(self,event):
        option = CalcFrame.on_choice(self,event)
        if option == "離我最近":
            cur.execute("SELECT name from food_table ORDER BY distance ASC")
            c=cur.fetchmany(3)
            str1=" ".join('%s'%id for id in c)
            self.ans.SetLabel(str1)
        elif option=="評價最高":
            cur.execute("SELECT name from food_table ORDER BY rating DESC")
            c=cur.fetchmany(3)
            str1=" ".join('%s'%id for id in c)
            self.ans.SetLabel(str1)
        elif option=="便宜的":
            cur.execute("SELECT name from food_table ORDER BY cheap DESC")
            c=cur.fetchmany(3)
            str1=" ".join('%s'%id for id in c)
            self.ans.SetLabel(str1)
        elif option=="出餐最快":
            cur.execute("SELECT name from food_table ORDER BY speed DESC")
            c=cur.fetchmany(3)
            str1=" ".join('%s'%id for id in c)
            self.ans.SetLabel(str1)
        else:
            cur.execute("SELECT name from food_table ORDER BY RANDOM()")
            c=cur.fetchmany(3)
            str1=" ".join('%s'%id for id in c)
            self.ans.SetLabel(str1)


def midterm_app():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()

#if __name__=='__midterm_app__':
midterm_app()
