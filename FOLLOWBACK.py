from tkinter import *
from tkinter import filedialog
from bs4 import BeautifulSoup

def extract_data_from_html(file):
    with open(file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return [link.text for link in soup.find_all('a')]


def remove_list_from_list(list1, list2):
    for item in list2:
        if item in list1:
            list1.remove(item)
    return list1


def save_to_html(list, file):
    with open(file, 'w') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Followback</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write("<center>\n")
        f.write("<h1>NO FOLLOWING-BACK</h1>\n")
        f.write("</center>\n")
        f.write('<ul>\n')
        for item in list:
            f.write(f'<li><a href="https://www.instagram.com/{item}">{item}</a></li>\n')
        f.write('</ul>\n')
        f.write('</body>\n')
        f.write('</html>\n')


def open_file1():
    file1 = filedialog.askopenfilename()
    listbox1.delete(0, END)
    for item in extract_data_from_html(file1):
        listbox1.insert(END, item)


def open_file2():
    file2 = filedialog.askopenfilename()
    listbox2.delete(0, END)
    for item in extract_data_from_html(file2):
        listbox2.insert(END, item)


def process_files():
    list1 = [listbox1.get(idx) for idx in range(listbox1.size())]
    list2 = [listbox2.get(idx) for idx in range(listbox2.size())]
    result = remove_list_from_list(list1, list2)
    save_to_html(result, 'No_followback.html')
    root.destroy()


root = Tk()
root.title("Followback")
root.geometry("635x300")
root.config(bg="#5851DB")


listbox1 = Listbox(root, width=40)
listbox1.grid(row=0, column=0, padx=10, pady=10)

listbox2 = Listbox(root, width=40)
listbox2.grid(row=0, column=2, padx=10, pady=10)

button1 = Button(root, text="Select following.html", command=open_file1)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = Button(root, text="Select followers.html", command=open_file2)
button2.grid(row=1, column=2, padx=10, pady=10)

process_button = Button(root, text="FOLLOWBACK", command=process_files)
process_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
