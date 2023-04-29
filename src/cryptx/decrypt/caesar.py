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
    "Z"
]


def caesar(text: str,shift: int):
    """Used to decrypt text encrypted with the caesar encryption method.
    .. |language| replace:: Python
    
    Parameters
    ----------
    text : str
        The text to decrypt

    shift : int
        The shift of the letters in the alphabet
   
    Return Values
    -------------
    Returns the decrypted text

    Raises
    ------
    * NotImplementedError: If text or shift is None
    * ValueError: If shift is higher than 25
    """
    if text == "" or None:
        raise NotImplementedError("Text can't be none or empty!")
    if shift == "" or None:
        raise NotImplementedError("Shift can't be none or empty!")
    if int(shift) > 25:
        raise ValueError("Shift can't be higher than 25!")
    
    text = text.strip().upper()
    __output = ""
    
    __shifted_alphabet = __alphabet[int(shift):] + __alphabet[:int(shift)]

    for __letter in range(len(text)):
        if str(text[int(__letter)]) == " ":
            pass
        else:
            __pos = __shifted_alphabet.index(str(text[int(__letter)]))
            __output = __output + str(__alphabet[__pos])
    
    return(__output)
