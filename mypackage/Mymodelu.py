def fibonacci(n):
    """ 
    calculate the nth term in the fibonacci sequence
    Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >>> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
        """
    if n<=1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def top_n(items, n):
    
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """
    # add the body of the function just below the docstring
    for i in range(n):
        for j in (len(items)-1-i):
            if items[j] > items[j+1]: # If this item is bigger than next the item
                items[j], items[j+1] = items[j+1], items[j] # Swap the locations of the elements
    top_n = items[-n:] # Get the last 2 items
    return top_n[::-1]
# Check whether the function works
top_n([8, 3, 2, 7, 4], 3)

    
    

    
    


