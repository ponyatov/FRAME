## @file
## @brief Minsky FRAME system implementation in Python

import os, sys, pickle, re

## @defgroup world The WORLD where all objects lives
## @{

## image file name is this .py file + ``.image'`
ImageFile = sys.argv[0] + '.image'

try:
    ## The WORLD where all objects lives
    World = pickle.load(open(ImageFile))
except IOError:
    World = []

## @}

## @defgroup sym Symbolic class system
## @{

## base class
class Frame:
    ## construct object in <T:V> 
    def __init__(self,V):
        ## object type
        self.type  = self.__class__.__name__.lower()
        ## object single value (name or literate value for primitives)
        self.value = self._setvalue(V)
    ## selected method for value setup: see @ref Number why is it used
    def _setvalue(self,V): return V
        
    ## `print` operator
    def __repr__(self):
        return self.dump()
    ## dump object in tree form
    def dump(self,prefix=''):
        return self.head(prefix=prefix)
    ## dump only object header
    ## @param[in] prefix before head
    def head(self,prefix=''):
        return '%s<%s:%s> @%X' % (prefix, self.type, self.value, id(self))
    
    ## print object in source code form
    def src(self): return self.value

## @test dump head format
def test_Frame_head():
    assert re.match(r'pfx:<frame:test> @[0-9A-F]+',Frame('test').head(prefix='pfx:'))
## @test source code format == value    
def test_Frame_src():
    assert Frame('test').src() == 'test'

## primititive elements
class Atom(Frame): pass

## symbol
class Symbol(Atom): pass

## number
class Number(Atom): pass

## string
class String(Atom): pass

## @}
