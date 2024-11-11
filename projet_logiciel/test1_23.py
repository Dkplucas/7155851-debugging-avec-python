def less_confusing_division(top, bottom):
    """Divise "top" par "bottom"."""
    if bottom == 0 or top == 0:
        return None
 
    if top % bottom != 0:
        return None
 
    return top / bottom