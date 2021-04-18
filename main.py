import requests
from bs4 import BeautifulSoup
from tkinter import*


class mem_app:
    def __init__(self,window):
        self.root=window
        self.root.title("Scraper titulos LA NACION")
        self.root.config(bg="#FFFFFF")


        self.imagen=PhotoImage(file="images.png")
        self.nacionimg=Label(self.root,image=self.imagen)
        self.nacionimg.grid(row=0,column=0)

        
        self.frame1=LabelFrame(self.root,text="Scrap")
        self.frame1.grid(row=1,column=0)
        
        btn_scrap = Button(self.root,text='Scrapear Titulos',padx=5,pady=5,bg='#836F41',command=self.scrap_n)
        btn_scrap.grid(row=2,column=0)

    
    
    def scrap_n(self):
        url = 'https://www.lanacion.com.ar/'
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content,'html.parser')
        
        titulos = soup.find_all('h2',"com-title")
        
        lst_title = []
        for i in (titulos):
            sub = i.find_all('a')
            #print(sub[0].attrs.get('title'))
            
            
            lst_title.append(sub[0].attrs.get('title'))
        
        print (lst_title)    
            
        lbl1 =  Label(self.root, text= lst_title[0],font=('arial', 12, 'bold'),bg="#FFFFFF")
        lbl1.grid(row=3,column=0)
        lbl2 =  Label(self.root, text=lst_title[1],font=('arial', 12, 'bold'),bg="#FFFFFF")
        lbl2.grid(row=4,column=0)
        lbl3 =  Label(self.root, text=lst_title[2],font=('arial', 12, 'bold'),bg="#FFFFFF")
        lbl3.grid(row=5,column=0)
        lbl4 =  Label(self.root, text=lst_title[3],font=('arial', 12, 'bold'),bg="#FFFFFF")
        lbl4.grid(row=6,column=0)
        lbl5 =  Label(self.root, text=lst_title[4],font=('arial', 12, 'bold'),bg="#FFFFFF")
        lbl5.grid(row=7,column=0)
            
     

if __name__=='__main__':
    window=Tk()
    app=mem_app(window)
    window.mainloop()