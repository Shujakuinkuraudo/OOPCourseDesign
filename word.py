import pickle
from abc import abstractmethod
from typing import overload

import utils


class WordAndPOS:...


class Word:

    @overload
    def __init__(self, WAP: WordAndPOS):...

    @overload
    def __init__(self, Text: str):...

    def __init__(self, *args) -> None: 
        """ 一个词"""
        self.Word = ""
        if type(args[0]) == WordAndPOS:
            self.Word = args[0].Word
        if type(args[0]) == str:
            self.Word = args[0]

    @property
    def key(self):
        return (self.Word)


class POS:  # part of speech

    @overload
    def __init__(self, WAP: WordAndPOS):...

    @overload
    def __init__(self, POS: str):...

    def __init__(self, *args) -> None:
        self.POS = ""
        """"一个词性"""
        if type(args[0]) == WordAndPOS:
            self.POS = args[0].POS
        if type(args[0]) == str:
            self.POS = args[0]

    @property
    def key(self):
        return (self.POS)


class WordAndPOS(Word, POS):

    def __init__(self, word="", PoS="", LineSeq=0, WordSeq=0) -> None:
        """"一个词和词性对 出现的位置"""
        Word.__init__(self, word)
        POS.__init__(self, PoS)
        self.seq = [LineSeq, WordSeq]

    @property
    def key(self):
        return (self.Word, self.POS)

    @property
    def position(self):
        return self.seq

    @property
    def is_first(self):
        return self.seq[1] == 0


class Bigram(WordAndPOS):

    def __init__(self, prev_WordAndPOS: WordAndPOS, now_WordAndPOS: WordAndPOS):
        """"两个词和词性对 第一个对出现的位置"""
        super().__init__(prev_WordAndPOS.Word, prev_WordAndPOS.POS,
                         prev_WordAndPOS.seq[0], prev_WordAndPOS.seq[1])
        self.AnotherWord = self.AnotherPOS = ""
        self.AnotherWord = now_WordAndPOS.Word
        self.AnotherPOS = now_WordAndPOS.POS

    @property
    def key(self):
        return (self.Word, self.POS, self.AnotherWord, self.AnotherPOS)


class Dict:

    def __init__(self, name="") -> None:
        """一个通用字典"""
        self.Dict = dict()
        self.Name = name

    @abstractmethod
    def __add__(self, obj):...

    @property
    def items(self):
        return self.Dict.items()

    def print(self):
        count = 0
        for k, v in self.items:
            print(k, v)
            count += 1
            if (count > 20):
                break


class PositionsDict(Dict):

    def __init__(self, name="") -> None:
        """"一个字典添加位置或数量"""
        super().__init__(name)

    @overload
    def __add__(self, Obj: Bigram):...

    @overload
    def __add__(self, ObjAndPos: list):...

    def __add__(self, Obj):
        if type(Obj) == list:
            obj, position = Obj
            if obj.key not in self.Dict:
                self.Dict[obj.key] = [position]
            else:
                self.Dict[obj.key].append(position)
        else:
            if Obj.key not in self.Dict:
                self.Dict[Obj.key] = 1
            else:
                self.Dict[Obj.key] += 1
        return self

    def sort(self, mode:str):
        if mode == "Bigram" or mode == "WordAndPOS":
            self.Dict = dict(sorted(self.items), key=lambda kv: kv[0][0])
        else:
            self.Dict = dict(sorted(self.items), key=lambda kv: kv[0])
        return self

    def to_pkl(self, file:str):
        utils.IOtools.dict_to_pkl(self.Dict, file)
