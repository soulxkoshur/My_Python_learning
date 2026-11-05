def main():
    print(write_letter("Aegon", "arya"), end="")
    print(write_letter("stark", "Jhon"), end="")
    print(write_letter("joffery", "sansa"), end="")


def write_letter(sender, reciever):
    return f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    hello, dear {reciever}

    I am pleased to inform you,
    that, I have returned and am well,
    so do not be concerned.

    from {sender}, lots of love <3...

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
main()