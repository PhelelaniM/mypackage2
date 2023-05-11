def top_n(items,n):
    """
    Return the top n items in an array in descending order.

    Arguements:
        n (int): Number of top items to returns
        items(list/array): list or array like object containing numerical valuees.

    Returns:
        list: list with the top n items in desc order

    Examples:
    >>> top_n([8,3,2,7,4],3)
    [8,7,4]
    
    """

    for i in range(n):
        for j in range (len(items)-1-i): #minus 1 because it counts starting from 1 so we must align with the index
            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j+1]

    # get last two items
    top_n = items[-n:]

    #return in descorder
    return top_n[::-1]