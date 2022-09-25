"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        try:
            frequencies[str(item)] += 1
        except KeyError:
            frequencies[str(item)] = 1
        except:
            print(f"error for item: {item}")
    return frequencies
