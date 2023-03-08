from tkinter import *
from tkinter import ttk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

def find_price(*args):
    try:
        price = int(sell_price.get())
        buy_price.set(price * .9)
        if mode == 0: # diamonds
            buy_price.set(buy_price - 500)
        elif mode == 1: # golds
            buy_price.set(buy_price - 200)
        elif mode == 2: # silvers
            buy_price.set(buy_price - 100)
        else: # bronzes
            buy_price.set(buy_price - 50)
    except:
        pass

def update_mode(selected_mode):
    if selected_mode == 0:
        mode.set('The current mode is Diamond.')
    elif selected_mode == 1:
        mode.set('The current mode is Gold.')
    elif selected_mode == 2:
        mode.set('The current mode is Silver.')
    elif selected_mode == 3:
        mode.set('The current mode is Bronze.')

root = Tk()
root.title('MLB Sniping Tool')
root.geometry('1280x720')

mainframe = ttk.Frame(root, padding = '0 0 1280 720')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sell_price = StringVar()
sell_entry = ttk.Entry(mainframe, width=15, textvariable=sell_price)
sell_entry.grid(column=2, row=13, sticky=(W, E))

buy_price = StringVar()
ttk.Label(mainframe, textvariable=buy_price).grid(column=2, row=14, sticky=(W, E))

ttk.Button(mainframe, text='Enter Price', command=find_price()).grid(column=3, row=15, sticky=W)

mode = StringVar()
mode_label = ttk.Label(mainframe, textvariable=mode)
mode_label.grid(column=0, row=0, sticky=W)

ttk.Button(mainframe, width=10, text='Diamonds', command=lambda: update_mode(0)).grid(column=0, row=2, sticky=(E, W))
ttk.Button(mainframe, text='Golds', command=lambda: update_mode(1)).grid(column=1, row=2, sticky=(E, W))
ttk.Button(mainframe, text='Silvers', command=lambda: update_mode(2)).grid(column=2, row=2, sticky=(E, W))
ttk.Button(mainframe, text='Bronzes', command=lambda: update_mode(3)).grid(column=3, row=2, sticky=(E, W))

ttk.Label(mainframe, text='stubs').grid(column=3, row=13, sticky=W)
ttk.Label(mainframe, text='stubs').grid(column=3, row=14, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

sell_entry.focus()
root.bind('<Return>', find_price)
root.mainloop()

while False:
    # Required information for program
    test_price = input('What can you find the card for? ') # Here would be a prompt to quit, not displayed to reduce clutter
    if test_price == '-1': break
    elif test_price == '-2': # Prompt for player info would be here, not present for less clutter
        player_info = input('Enter player information: ')
        card_list.append(player_info)
    elif test_price == '-3':
        print(card_list)
    else:
        buy_price = (int(test_price) * .90)
        print(f'Silver Card: {buy_price - 100}.')
        print(f'Gold Card: {buy_price - 250}.')
        print(f'Diamond Card: {buy_price - 500}.')