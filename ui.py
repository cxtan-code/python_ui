# -*- coding: utf-8 -*-
import wx
import os
class NewFrame(wx.Frame):
    def __init__(self, parent, title):
        # super(A, self).__init__(self, title=title, size=(300,100))#不知道为什么用super会出错，以后在查把
        wx.Frame.__init__(self, parent, title=title, size=(800,800))
        self.TextContrl = wx.TextCtrl(self, style = wx.TE_MULTILINE)

        self.CreateStatusBar()      #创建窗口底部的状态栏

        self.filemenu = wx.Menu()   #添加菜单
        MenuExit = self.filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        self.filemenu.AppendSeparator() #添加一个分隔符

        MenuAbount = self.filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")  # 设置菜单的内容
        MenuOpenFile = self.filemenu.Append(wx.ID_OPEN, "file", "open file")    #打开文件
        MenuSaveFIle = self.filemenu.Append(wx.ID_SAVE, "save", "save file")
        self.menuBar = wx.MenuBar() #添加菜单条

        self.menuBar.Append(self.filemenu, u"关于")
        self.SetMenuBar(self.menuBar)  # 创建菜单条
        self.Show(True)

        self.Bind(wx.EVT_MENU, self.onMenuExit, MenuExit)
        self.Bind(wx.EVT_MENU, self.onMenuAbount, MenuAbount)
        self.Bind(wx.EVT_MENU, self.onOpenFile, MenuOpenFile)
        self.Bind(wx.EVT_MENU, self.onSaveFile, MenuSaveFIle)

    def onMenuExit(self, event):
        dlg = wx.MessageDialog(self,"A samll text editor", "About sample Editor",wx.YES_NO|wx.ICON_QUESTION)#创建一个对话框，有一个ok的按钮
        if wx.ID_YES == dlg.ShowModal():#显示对话框
            self.Close(True)
        dlg.Destroy()#完成后，销毁它。

    def onMenuAbount(self, event):
        dlg = wx.MessageDialog(self, u"这是一个对话框", u"关于", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        pass
    def onOpenFile(self, event):
        self.dirname = " "
        self.filename = ""
        dlg = wx.FileDialog(self, u"选择文件", self.dirname, self.filename , "*.*", wx.ID_OPEN)#文件对话框
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            with open(os.path.join(self.dirname, self.filename), "rb") as f:
                data = f.read().decode(encoding='utf-8')
                self.TextContrl.Clear()
                self.TextContrl.AppendText(data)
        dlg.Destroy()

    def onSaveFile(self, event):
        data = self.TextContrl.GetValue()
        with open(os.path.join(self.dirname, self.filename), "wb") as f:
            f.write(data.encode(encoding='utf-8'))
        dlg = wx.MessageDialog(self, u'文件已经保存', u'保存', wx.OK)
        if dlg.ShowModal() == wx.ID_OK:
            self.TextContrl.Clear()
            self.TextContrl.AppendText(u'欢迎使用文档编辑器，作者cxtan')
            dlg.Destroy()
if __name__ == "__main__":
    app = wx.App(False)#创建一个APP的实例
    TextContrl = NewFrame(None, "hello,Gui python")
    app.MainLoop()
    pass
