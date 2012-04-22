# encoding: UTF-8
from PyQt4 import QtCore,QtGui
import re


def connect(sender, signal, receiver, slot):
    print "Connect::", sender, signal, receiver, slot
    m = re.search("^(\w+).(\w+)(\(.*\))?", slot)
    if m:
        remote_obj = getattr(receiver, m.group(1))
        if remote_obj is None: raise AttribueError, "Object %s not found on %s" % (remote_obj, str(receiver))
        remote_fn = getattr(remote_obj, m.group(2))
        if remote_fn is None: raise AttribueError, "Object %s not found on %s" % (remote_fn, remote_obj)
        sender.connect(sender, QtCore.SIGNAL(signal), remote_fn)
    else:
        sender.connect(sender, QtCore.SIGNAL(signal), receiver, QtCore.SLOT(slot))
    return True

QMessageBox = QtGui.QMessageBox

class MessageBox(QMessageBox):
    @classmethod
    def msgbox(cls, typename, text, button0, button1 = None, button2 = None):
        icon = QMessageBox.NoIcon
        title = "Message"
        if typename == "question":
            icon = QMessageBox.Question
            title = "Question"
        elif typename == "information":
            icon = QMessageBox.Information
            title = "Information"
        elif typename == "warning":
            icon = QMessageBox.Warning	
            title = "Warning"
        elif typename == "critical":
            icon = QMessageBox.Critical
            title = "Critical"
        title = unicode(title,"UTF-8")
        text = unicode(text,"UTF-8")
        msg = QMessageBox(icon, title, text)
        msg.addButton(button0)
        if button1: msg.addButton(button1)
        if button2: msg.addButton(button2)
        return msg.exec_()

    @classmethod
    def question(cls, *args): return cls.msgbox("question",*args)

    @classmethod
    def information(cls, *args): return cls.msgbox("question",*args)

    @classmethod
    def warning(cls, *args): return cls.msgbox("warning",*args)

    @classmethod
    def critical(cls, *args): return cls.msgbox("critical",*args)