CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def split_korean_jaso(text : str, remove_space : bool = False) -> list[str]:
    """Splits Korean text into individual Jaso (initial, medial, and final consonants).

    Args:
        text (str): The input string containing Korean characters to be split into Jaso.
        remove_space (bool, optional): If True, spaces will be removed from the output. Defaults to False.

    Returns:
        list[str]: A list of strings, where each Korean character is split into its constituent Jaso.
    """
    split_text = []
    for char in text:
        if remove_space and char == ' ':
            continue
        if '가' <= char <= '힣':
            char_code = ord(char) - 44032
            jong = char_code % 28
            jung = ((char_code - jong) // 28) % 21
            cho = ((char_code - jong) // 28) // 21
            split_text.append(CHO[cho])
            split_text.append(JUNG[jung])
            if jong != 0:
                split_text.append(JONG[jong])
        else:
            split_text.append(char)
    return split_text
