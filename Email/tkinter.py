from tkinter import *
 
 #Initialize Tk
 
root = Tk()
 
 root.title ("ملصق تعليمي لـ tkinter")
 
 root.geometry ('300x200') # حجم النافذة 300x200
 
 # fg: لون المقدمة أحمر bg: لون الخلفية أصفر ذهبي
 
 label = Label (root، fg = "red"، bg = "gold"، text = 'I am text display')
 
 # تسمية العرض ، يجب أن تحتوي على هذا البيان
 
label.pack()
 
 # أدخل حلقة الرسالة
 
root.mainloop()