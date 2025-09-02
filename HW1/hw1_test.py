from hw1_strings import *
def test_constantsAndVariables():
    assert constantsAndVariables() == 23

def test_NumTimesQuoteIn23():
    assert numTimesQuoteIn23() == 15

def test_StartAndEndIndeciesOfSubstring():
    assert startAndEndIndicesOfSubString()[0] == 262

def test_StartAndEndIndeciesOfSubstring2():
    assert startAndEndIndicesOfSubString()[1] == 308   

def test_IntegerSeqToString():
    assert integerSeqToString() == "J Robert Oppenhiemer"