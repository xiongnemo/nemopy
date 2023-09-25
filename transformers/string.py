def ascii2octalstring(source: str) -> str:
    octal = ""
    for c in source:
            octal += "\\"
            octrep = oct(ord(c))[2:]  # octal numbers are prepended by a zero,
                                    # but since this will be a string not a
                                    # number we don't want that.
            octrep = octrep.zfill(3)  # pad with preceeding 0s
            octal += octrep
    return octal