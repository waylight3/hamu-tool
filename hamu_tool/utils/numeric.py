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

def mean(data : list) -> float:
    """Calculate the mean of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    return sum(data) / len(data)

def variance(data : list) -> float:
    """Calculate the variance of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The variance of the numbers.
    """
    m = mean(data)
    return mean([(x - m) ** 2 for x in data])

def std_dev(data : list) -> float:
    """Calculate the standard deviation of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The standard deviation of the numbers.
    """
    return variance(data) ** 0.5

def median(data : list) -> float:
    """Calculate the median of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The median of the numbers.
    """
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2

