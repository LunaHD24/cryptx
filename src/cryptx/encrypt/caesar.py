__alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def caesar(text: str,shift: int):
    """Used to encrypt text with the caesar encryption method.
    .. |language| replace:: Python
    
    Parameters
    ----------
    text : str
        The text to encrypt

    shift : int
        The shift of the letters in the alphabet
   
    Return Values
    -------------
    Returns the encrypted text

    Raises
    ------
    * NotImplementedError: If text or shift is None
    * ValueError: If shift is higher than 25
    """
    if text == None:
        raise NotImplementedError("Text can't be none!")
    if shift == None:
        raise NotImplementedError("Shift can't be none!")
    text = text.upper()
    __repeats = len(text)
    __output = ""
    __count = 0
    for __letter in range(__repeats):
        if int(shift) > 25:
            raise ValueError("The shift can't be higher than 25!")
        else:
            __position = __alphabet.index(text[__count:__count+1])
            __index = __position
            for __pos in range(int(shift)):
                __index = __index + int(shift)
                __index = __index % 26
                __output = __output + __alphabet[__index]
                __count = __count + 1
    return str(__output)