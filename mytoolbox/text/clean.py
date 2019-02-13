import re


def clean_text(s):
    """
    Return the text with only character belong to A-Za-z0-9,;.!?\sàâêéèäëïöüùûîœ’'
    
    Parameters
    ----------
    s : str
        input string
    
    Returns
    -------
    str
        output
    """

    s=re.sub("\n[\s]*"," ",s)
    s=re.sub("[^A-Za-z0-9,;.!?\sàâêéèäëïöüùûîœ’\']", '',s)
    s=s.replace("( ","(").replace(" )",")")
    s=s.replace(" ,",",").replace(" ;",",")
    s=s.replace(" .",".")
    s=re.sub("[ ]+"," ",s)
    s = s.replace(u'\xa0', u' ')
    return s