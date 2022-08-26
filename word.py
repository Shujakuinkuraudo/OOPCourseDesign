class Word:
    def __init__(self,Text="") -> None:
        self.Text = Text
    
    @property
    def key(self):
        return (self.Text)

class POS:    #part of speech
    def __init__(self,PoS="") -> None:
        self.POS = PoS

    @property
    def key(self):
        return (self.POS)

class WordPOS(Word,POS):
    def __init__(self, Text="",PoS="") -> None:
        Word.__init__(self,Text)
        POS.__init__(self,PoS)
    
    @property
    def key(self):
        return (self.Text,self.POS)


class Dict:
    def __init__(self) -> None:
        self.Dict = dict()
    def __add__(self,obj):
        pass

class PositionsDict(Dict):
    def __init__(self) -> None:
        super().__init__()
    def __add__(self, obj):
        if 
        

a = WordPOS("aaaa","aaaaaaaa")