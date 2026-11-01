import tkinter as tk

count = 0
root = tk.Tk()
root.title("CODE-VVOD")
jj = open('codes.txt')
codes = ''.join(jj.readlines()).split('||')
jj.close()

def click(text_box,label):
    global count
    for i in codes:
        if text_box.get() == i:
            codes.remove(i)
            count += 1
            label.config(text=str(count))
            break
    print(str(count))
            
label = tk.Label(root, text='0')
label.pack(pady=1)
text_box = tk.Entry(root, width=30)
text_box.pack(side=tk.LEFT, padx=(10, 5), pady=10)
button = tk.Button(root, text="Go", width=3, height=1, command=lambda: click(text_box,label))
button.pack(side=tk.LEFT, padx=(5, 10), pady=10)
root.mainloop()