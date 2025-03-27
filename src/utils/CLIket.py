import re
from os import system, path
import json

from .Merger import Merger

merger = Merger()



class CLIket:
    def __init__(self, filePath):
        self.patternCommandMerge = r'([A-Za-z]{1,}) \+ ([A-Za-z]{1,})'
        self.patternCommand = r'\!+.'
        
        self.filePath = filePath
        
        self.base = ">"
        self.on = True
        
    
    def GetElements(self):
        with open(self.filePath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data    
        
    def Home(self):
        system('cls')
        print('<>' + ('-'*30) + '< Craft Command V1 >' + (30*'-') + '<>')
        print()
        print(f'!rs: clear all')
        print(f'!l: leave')
        print()
               
    def IfWantToLeave(self):
        try:
            
            option = input('Leave now? [ Y / n ]: ')

            if option == 'Y':
                self.on = False
            elif option == 'n':
                self.on = True
                self.Home()
            else:
                print()
                print('Invalid Value: It just can be "Y" or "n", obeying the uppercase and lowercase.')
                self.IfWantToLeave()    
            
            
        except:
            self.Home()
            pass
        
    def View(self):
        elements = self.GetElements()
        
        try:
            name_element = input('~ element_name: ').lower()            
            element = elements[name_element]
            
            print()
            print(f'= Icon: {element['icon']}')
            print(f'= Discovered: {'Not' if element['discovered'] is False else 'Yes'}')
            print()
        
        except Exception as err:
            self.Home()
            print(f'Ops!, Ocorreu um erro')
         
    def asker(self) -> str:
        try:
            return input(f'{self.base} ')
        except Exception as err:
            print(f'Ops! Ocurred an error, try again')

                    
    def listener(self, ask: str):
        if re.match(self.patternCommand, ask) is not None:
            match(ask):
                case '!view':
                    self.View()
                case '!l':
                    self.IfWantToLeave()
                case '!rs':
                    system('cls')
                    self.Home()
            
                       
        if re.match(self.patternCommandMerge, ask) is not None:
            stringMatched = re.match(self.patternCommandMerge, ask)
            
            merger.elements = self.GetElements()
            merger.filePath = self.filePath
            
            merger.makeMerger(stringMatched.group(1), stringMatched.group(2))
            
            
        
                

        
 