from mypackage2 import myModule2

def top_n():
    """ 
    to ensure that top_n function works properly
    """

    assert myModule2.top_n([8,3,2,7,4],3) == [8,7,4], "incorrect"
    assert myModule2.top_n([10,1,12,9,2],2) == [12,10],"incorrect"
    assert myModule2.top_n([1,2,3,4,5],5) == [5,4,3,2,1], "incorrect"