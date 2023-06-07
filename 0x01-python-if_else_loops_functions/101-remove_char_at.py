#!/usr/bin/python3
def remove_char_at(str, n):
    n = int(n)
    if n < 0:
        return f"{str}"
    return f"{str[:n]+str[n + 1:]}"
