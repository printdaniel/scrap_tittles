import requests
from bs4 import BeautifulSoup
from tkinter import*
from PIL import Image, ImageChops, ImageEnhance, ImageOps





class mem_app:
    def __init__(self,window):
        self.root=window
        self.root.title("Scraper titulos LA NACION")
        self.root.config(bg="#B22222")


        self.imagen=PhotoImage(file="images.png")
        self.nacionimg=Label(self.root,image=self.imagen)
        self.nacionimg.grid(row=0,column=0)

        
        self.frame1=LabelFrame(self.root,text="Texto a memorizar")
        self.frame1.grid(row=1,column=0)

        label_titulo1 = Label(self.root, text='Nombre:',font=('arial', 12, 'bold'),bg="#7C3E48")
        label_titulo1.grid(row=1, column = 0, sticky='W')
    
    def scrap_n(self):
        url = 'https://www.lanacion.com.ar/'
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content,'html.parsers')
        
        titulos = soup.find_all('h2',"com-title")
        
        for i in titulos:
            sub = i.find_all('a')
            print(sub[0].attrs.get('title'))
        


    














if __name__=='__main__':
    window=Tk()
    app=mem_app(window)
    window.mainloop()


