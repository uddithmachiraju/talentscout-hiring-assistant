
# Returns True if the user/candidate types some unknown words
def is_gibberish(text):
    letters = sum(c.isalpha() for c in text)
    if letters / max(len(text),1) < 0.5:
        return True
    # Add more rules as needed
    return False