import ipywidgets as widgets

def first_char(string, bol=[1, 4, 5]):
    return (len(string), string[-1], bol)

widgets.interact(first_char, string='a',bo=[2,3])
