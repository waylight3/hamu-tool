def is_int(x : str) -> bool:
    """Check if a string is an integer.

    Args:
        x (str): The string to check.

    Returns:
        bool: True if the string is an integer, False otherwise.
    """
    try:
        int(x)
        return True
    except ValueError:
        return False

def is_float(x : str) -> bool:
    """Check if a string is a float.

    Args:
        x (str): The string to check.

    Returns:
        bool: True if the string is a float, False otherwise.
    """
    try:
        float(x)
        return True
    except ValueError:
        return False

def is_number(x : str) -> bool:
    """Check if a string is a number.

    Args:
        x (str): The string to check.

    Returns:
        bool: True if the string is a number, False otherwise.
    """
    return is_int(x) or is_float(x)
