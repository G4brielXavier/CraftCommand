import re, os, json

# importing Merger
from .Merger import Merger

# instanciating Merger
merger = Merger()



class CLIket:
    def __init__(self, filePath, configPath):
        self.patternCommandMerge = r'([A-Za-z]{1,}) \+ ([A-Za-z]{1,})'
        self.patternCommand = r'\!+.'
        
        self.filePath = filePath
        self.configPath = configPath
        
        self.base = ">"
        self.on = True
        
    # get all elements in the JSON FILE
    def GetElements(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data 
        
        
           
        
        
        
    def Home(self):
        os.system('title CraftCommand')
        os.system('cls')
        print('<>' + ('-'*30) + '< Craft Command V2 >' + (30*'-') + '<>')
        print()
        print('!help: to view all comands that you can use.')
        print()
        
        
    # view all elements for name
    def view_name(self):
        elements = self.GetElements(self.filePath)
        
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
         
    
    def view_all(self):
        elements = self.GetElements(self.filePath)
        
        print()
        
        for k, v in elements.items():
            print(f'{v['icon']}  {k}')      
            
        print()
        
    
    def help(self):
        configInfo = self.GetElements(self.configPath)
        commands = configInfo['commands']
        
        print()
        for k, v in commands.items():
            print(f'{k}: {v}')
        print()

     
         
    def asker(self) -> str:
        try:
            return input(f'{self.base} ')
        except Exception as err:
            print(f'Ops! Ocurred an error, try again')

                    
    def listener(self, ask: str):
        if re.match(self.patternCommand, ask) is not None:
            match(ask):     
                case '!help':
                    self.help()    
                case '!view_all':
                    self.view_all()       
                case '!view_name':
                    self.view_name()
                case '!l':
                    self.on = False
                case '!rs':
                    os.system('cls')
                    self.Home()
                case '!creator':
                    print("Hi, I'm Gabriel Xavier(Dotket). I created Craft Command inspired by Neal Fun's Infinity Craft. So, all rights reserved to https://neal.fun")
                    
            
                       
        if re.match(self.patternCommandMerge, ask) is not None:
            stringMatched = re.match(self.patternCommandMerge, ask)
            
            merger.elements = self.GetElements(self.filePath)
            merger.filePath = self.filePath
            
            merger.makeMerger(stringMatched.group(1), stringMatched.group(2))
            
        
        
        
                

        
 