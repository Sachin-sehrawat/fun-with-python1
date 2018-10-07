from tkinter import *
import requests
def click():
    API_END_POINT="https://www.wikidata.org/w/api.php"
    txt=textentry.get()

    params={
        'action':'wbsearchentities',
        'language':'en',
        'search':txt,
        'format':'json'
    }
    r=requests.get(API_END_POINT,params=params)
    ans=(r.json()['search'][0]['description'])
    output.insert(END,ans)

window=Tk()
window.title("The Encyclopedia")
window.configure(background="black")
Label(window,text="ask me about anybody: ",bg="black",fg="white",font="none 12 bold").grid(row=1,column=0,sticky=W)
textentry=Entry(window,width=20,bg="white")
textentry.grid(row=2,column=0,sticky=W)
Button(window,text="ASK",width=6,command=click).grid(row=3,column=0,sticky=W)
output=Text(window,width=20,height=3,wrap=WORD,background="white")
output.grid(row=4,column=0,sticky=W)
window.mainloop()
