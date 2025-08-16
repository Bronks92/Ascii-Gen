import os
import pyfiglet

def create_ascii_text():
    fontlist = pyfiglet.FigletFont.getFonts()


    while True:
        os.system("cls")
       
        print("""
                                                                                                                                                   
 ▄████████    ▄████████    ▄████████    ▄████████     ███    
███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄
███    █▀    ███    ███   ███    █▀    ███    ███    ▀███▀▀██
███         ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███     ███   ▀
███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████     ███    
███    █▄  ▀███████████   ███    █▄    ███    ███     ███    
███    ███   ███    ███   ███    ███   ███    ███     ███    
████████▀    ███    ███   ██████████   ███    █▀     ▄████▀  
             ███    ███                                      
   ▄████████    ▄████████  ▄████████  ▄█   ▄█                
  ███    ███   ███    ███ ███    ███ ███  ███                
  ███    ███   ███    █▀  ███    █▀  ███▌ ███▌               
  ███    ███   ███        ███        ███▌ ███▌               
▀███████████ ▀███████████ ███        ███▌ ███▌               
  ███    ███          ███ ███    █▄  ███  ███                
  ███    ███    ▄█    ███ ███    ███ ███  ███                
  ███    █▀   ▄████████▀  ████████▀  █▀   █▀  
            _____________________              
                By BROONKS        
              
                """)
        

        text = input(f" >>> Enter the texte you want convert : ")
        if text == "q":
            exit()
    
        while True:
            fontchoix = input(""" >>> Enter a font  ("?" for the liste): """)
            if fontchoix == "q":
               break


            elif fontchoix == "?":
                for font in fontlist:
                    print(f"   {font}   ")

            elif fontchoix == "":
                for font in fontlist:
                    ASCII_art_1 = pyfiglet.figlet_format(text,font)
                    print(f" {text}")
                    print(f"font: {font}")
                    print(ASCII_art_1)

            else:
                try:
                    ASCII_art_1 = pyfiglet.figlet_format(text,font=fontchoix)
                      
                    print(f"text: {text} ")
                    print(f"font: {fontchoix}")
                    print(ASCII_art_1)
                    
                except:
                    print("  error! {font} probably doesn't exist!")

            print(" --------------------------------------------------------------------------------- ")
           


while True:
    create_ascii_text()

# By BROONKSs
