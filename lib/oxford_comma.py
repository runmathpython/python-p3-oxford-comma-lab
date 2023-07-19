def oxford_comma(items):

    # if the number of items is 2, connect the two with and without a comma,
    # and if the number is 3 or more, the last item will be commected with and anyway
    if len(items) > 1:
        items[-1] = "and " + items[-1]
    
    # if the number is 3 or more, connect each item with a comma and a space,
    # since the last item has been connected with and already
    if len(items) > 2:
        return ", ".join(items)
    else:
        # if the number is 0 or 1, connect the item with nothing
        return " ".join(items)
