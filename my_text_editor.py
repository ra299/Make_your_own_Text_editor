import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("My_Text Editor")
#main_application.wm_iconbitmap("icon.ico")

#_____mian menu_______________________________________________________

#.............................End main menu...........................
main_manu = tk.Menu()

#_______file icons
#new_icon = tk.PhotoImage(file = "icons/new.png")
open_icon = tk.PhotoImage(file = "icons/open.png")
save_icon = tk.PhotoImage(file = "icons/save.png")
save_as_icon = tk.PhotoImage(file = "icons/save_as.png")
exit_icon = tk.PhotoImage(file = "icons/exit.png")


file = tk.Menu(main_manu, tearoff = False)


#__________________________Edit
#_____________________Icons
cpoy_icon = tk.PhotoImage(file = "icons/copy.png")
paste_icon = tk.PhotoImage(file = "icons/paste.png")
cut_icon = tk.PhotoImage(file = "icons/cut.png")
clear_all_icon = tk.PhotoImage(file = "icons/clear_all.png")
find_icon = tk.PhotoImage(file = "icons/find.png")

edit = tk.Menu(main_manu, tearoff = False)



#______________________________View
#____________________icons

tool_bar_icon = tk.PhotoImage(file = "icons/tool_bar.png")
status_bar_icon = tk.PhotoImage(file = "icons/status_bar.png")

view = tk.Menu(main_manu, tearoff = False)


#________________________________________color_theme
#____________________icons

light_default_icon = tk.PhotoImage(file = "icons/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icons/light_plus.png")
dark_icon = tk.PhotoImage(file = "icons/dark.png")
red_icon = tk.PhotoImage(file = "icons/red.png")
monokai_icon = tk.PhotoImage(file = "icons/monokai.png")
night_blue_icon = tk.PhotoImage(file = "icons/night_blue.png")

color_theme = tk.Menu(main_manu, tearoff = False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Defaul' : ("#000000","#ffffff"),
    "Light Plus" : ("#474747","#e0e0e0"),
    "Dark" : ("#c4c4c4", "#2d2d2d"),
    "Red" : ("#2d2d2d","#ffe8e8"),
    "Monokai" : ("#d3b774", "#474747"),
    "Night Blue" : ("#ededed","#6b9dc2")
}


# cascade
main_manu.add_cascade(label = "File", menu = file)
main_manu.add_cascade(label = "Edit", menu = edit)
main_manu.add_cascade(label = "View", menu = view)
main_manu.add_cascade(label = "Color Them", menu = color_theme)


#_____tool bar_______________________________________________________


tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP, fill = tk.X)

###################### Font Box #####################
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = "readonly")
font_box["values"] = font_tuples
font_box.current(font_tuples.index("Arial")) 
font_box.grid(row = 0, column = 0, padx = 5)

######################## Size Box ##################

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = size_var, state = "readonly")
font_size["values"] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row = 0, column = 1, padx = 5 )

## Bold Button

bold_icon = tk.PhotoImage(file = "icons/bold.png")
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0, column = 2, padx = 5)

## Italic Button

italic_icon = tk.PhotoImage(file = "icons/italic.png")
italic_btn = ttk.Button(tool_bar, image = italic_icon)
italic_btn.grid(row = 0, column = 3, padx = 5)

## Underline Button

underline_icon = tk.PhotoImage(file = "icons/underline.png")
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column = 4, padx = 5)

## font color buton 

font_color_icon = tk.PhotoImage(file = "icons/font_color.png")
font_color_btn = ttk.Button(tool_bar, image = font_color_icon)
font_color_btn.grid(row = 0, column = 5, padx = 5)

## Alige Button

alige_left_icon = tk.PhotoImage(file = "icons/align_left.png")
alige_left_btn = ttk.Button(tool_bar, image = alige_left_icon)
alige_left_btn.grid(row = 0, column = 6, padx = 5)

alige_center_icon = tk.PhotoImage(file = "icons/align_center.png")
alige_center_btn = ttk.Button(tool_bar, image = alige_center_icon)
alige_center_btn.grid(row = 0, column = 7, padx = 5)

alige_right_icon = tk.PhotoImage(file = "icons/align_right.png")
alige_right_btn = ttk.Button(tool_bar, image = alige_right_icon)
alige_right_btn.grid(row = 0 , column = 8, padx = 5)

#.............................End tool bar...........................

#_____text editor_______________________________________________________

text_editor = tk.Text(main_application)
text_editor.config(wrap = "word", relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.config(command = text_editor.yview)
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)

text_editor.focus_set()
text_editor.pack(fill = tk.BOTH, expand = True)
text_editor.config(yscrollcommand = scroll_bar.set)

# font family and Font size Functinality

current_font_family = "Arial"
current_font_size = 12

def change_font(event = None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family, current_font_size))

def change_fontsize(event = None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family, current_font_size))


font_box.bind("<<comboboxselected>>", change_font)
font_size.bind("<<comboboxselected>>", change_fontsize)

############################################ Buttons Functionality ##########################

### bold Button 
def change_bold():
    text_property = tk.font.Font(font = text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font = (current_font_family, current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.configure(font = (current_font_family, current_font_size, "normal"))

bold_btn.configure(command=change_bold)

####  For Italic Button Function

def change_italic():
    text_property = tk.font.Font(font = text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.configure(font = (current_font_family, current_font_size, "italic"))
    if text_property.actual()["slant"] == "italic":
        text_editor.configure(font = (current_font_family, current_font_size, "normal"))

italic_btn.configure(command=change_italic)

######## For underline

def change_underline():
    text_property = tk.font.Font(font = text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.configure(font = (current_font_family, current_font_size, "underline"))
    if text_property.actual()["underline"] == 1:
        text_editor.configure(font = (current_font_family, current_font_size, "normal"))

underline_btn.configure(command=change_underline)

####### Change font color functions

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

    # print(color_var)

font_color_btn.configure(command = change_font_color)

###### For Alige Left function

def alige_left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left",justify = tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_editor,"left")

alige_left_btn.configure(command = alige_left)

def alige_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center",justify = tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_editor,"center")

alige_center_btn.configure(command = alige_center)

def alige_right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right",justify = tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_editor,"right")

alige_right_btn.configure(command = alige_right)

text_editor.configure(font = ("Arial",12))
#.............................text editor...........................

#_____main status bar_______________________________________________________

status_bar = ttk.Label(main_application, text = "Status bar")
status_bar.pack(side = tk.BOTTOM)

text_changed = False

def changed(event = None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        word = len(text_editor.get(1.0, "end-1c").split())
        characters = len(text_editor.get(1.0, "end-1c").replace(" ",""))
        status_bar.config(text = f"characters : {characters} word : {word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", changed)        

#.............................end main status bar...........................

#_____mian menu functinality_______________________________________________________

#### Veriable new functions #######3
url = ''
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)



#______________________________main menu functinality end______________________________

#################### File commands #######################

#file.add_command(label = "New", image = new_icon, compound = tk.LEFT, accelerator = "Ctrl+N", command = new_file)

##### Open functionality

def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = "select File", filetypes = (("Text File", "*.txt"),("All files","*.*")))
    try:
        with open(url, "r") as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except: 
        return

    main_application.title(os.path.basename(url))

file.add_command(label = "Open", image = open_icon, compound = tk.LEFT, accelerator = "Ctrl+O", command = open_file)

####### Save Functionaliy

def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url,"w", encoding = "utf-8") as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = "w", defaultextenstion = ".txt", filetypes = (("Text File","*.txt"),("All files","*.*")))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label = "Save", image = save_icon, compound = tk.LEFT, accelerator = "Ctrl+S", command = save_file)

######## save _ as Functionality

def save_as(event = None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = "w", defaultextenstion = ".txt", filetypes = (("Text File","*.txt"),("All files","*.*")))
        url.write(content)
        url.close()

    except:
        return
file.add_command(label = "Save As", image = save_as_icon, compound = tk.LEFT, accelerator = "Ctrl+Alt+S", command = save_as)

######################### Exit

def exit_func(event = None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("Warnning", "Do You Want save This File.?")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END) 
                    with open(url,"w", encoding= "utf-8") as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = "w", defaultextenstion = ".txt", filetypes = (("Text File","*.txt"),("All files","*.*")))                    
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label = "Exit", image = exit_icon, compound = tk.LEFT, accelerator = "Ctrl+Q", command = exit_func)

################ Find Functionality ####################

def find_func(event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex = tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match", foreground = "red", background = "yellow")
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word , replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_Dialogue = tk.Toplevel()
    find_Dialogue.geometry("450x250+500+200")
    find_Dialogue.title("Find")
    find_Dialogue.resizable(0,0)

    ##### Freame

    find_frame = tk.LabelFrame(find_Dialogue, text = "Fin / Replace")
    find_frame.pack(pady = 20,)

    ##### Labels
    text_find_label = ttk.Label(find_frame, text = "Find :")
    text_replace_label = ttk.Label(find_frame, text = "Replace")

    ##### Entry
    find_input = ttk.Entry(find_frame, width = 30)
    replace_input = ttk.Entry(find_frame, width = 30)

    #### Button

    find_button = ttk.Button(find_frame, text = "Find", command = find)
    replace_button = ttk.Button(find_frame, text = "Replace", command = replace)

    #### Label grid

    text_find_label.grid(row = 0, column = 0, padx = 4, pady = 4)
    text_replace_label.grid(row = 1, column = 0, pady = 4)

    #### entry Box Grid

    find_input.grid(row = 0, column = 1, padx = 4, pady =4)
    replace_input.grid(row = 1, column = 1, padx = 4, pady = 4)

    ###### Bottton grid

    find_button.grid(row = 2, column=0, padx = 8, pady = 4)
    replace_button.grid(row = 2, column = 1, padx = 8, pady = 4)

    find_Dialogue.mainloop()

##################### Edit commands ######################

edit.add_command(label = "Copy", image = cpoy_icon, compound = tk.LEFT, accelerator = "Ctrl+C", command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = "Paste", image = paste_icon, compound = tk.LEFT, accelerator = "Ctrl+V", command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label = "Cut", image = cut_icon, compound = tk.LEFT, accelerator = "Ctrl+X", command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = "Clear All", image = clear_all_icon, compound = tk.LEFT, accelerator = "Ctrl+Alt+X", command = lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label = "Find", image = find_icon, compound = tk.LEFT, accelerator = "Ctrl+F", command = find_func)

##################### View Check button #############

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True



view.add_checkbutton(label = "Tool Bar",onvalue = True, offvalue = False, variable = show_toolbar, image = tool_bar_icon, compound = tk.LEFT, command = hide_toolbar)
view.add_checkbutton(label = "Status Bar",onvalue = True, offvalue = False, variable = show_statusbar, image = status_bar_icon, compound = tk.LEFT, command = hide_statusbar )

#################### Colous Theme #############################

def change_theme():
    chose_theme = theme_choice .get()
    color_tuple = color_dict.get(chose_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config( background = bg_color, fg = fg_color)

count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image = color_icons[count], variable = theme_choice, compound = tk.LEFT, command = change_theme)
    count = count+1


#.............................End main menu functinality...........................
main_application.config(menu = main_manu)

####### Bind shorcut keys

main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)


main_application.mainloop()

# importent line of code --print( tk.font.Font(font = text_editor["font"]).actual())