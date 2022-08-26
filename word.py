from abc import abstractmethod


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
    def __init__(self, Text="",PoS="",LineSeq=0,WordSeq=0) -> None:
        Word.__init__(self,Text)
        POS.__init__(self,PoS)
        self.seq = [LineSeq,WordSeq]
    
    @property
    def key(self):
        return (self.Text,self.POS)
        
    @property
    def position(self):
        return self.seq


class Dict:
    def __init__(self) -> None:
        self.Dict = dict()

    @abstractmethod
    def __add__(self,obj):
        pass

class PositionsDict(Dict):
    def __init__(self,other=None) -> None:
        super().__init__()
        if other:
            self.Dict = other

    def __add__(self, ObjPosition):
        key,position = ObjPosition
        if key not in self.Dict:
            self.Dict[key] = [position]
        else: 
            self.Dict[key].append(position)
        return self

    @property
    def itmes(self):
        return self.Dict.items()
    
    
    
        
