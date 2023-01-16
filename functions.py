def format_duration(secs):
    """Formats seconds to minutes, days, hours, etc"""
    if secs == 0:
        return "now"
    yy = secs//(365*(24*3600))
    dd = secs//(3600*24) % 365
    hh = secs//3600 % 24
    mm = secs//60 % 60
    ss = secs % 60
    yyf = "year" if yy == 1 else "years"
    ddf = "day" if dd == 1 else "days"
    hhf = "hour" if hh == 1 else "hours"
    mmf = "minute" if mm == 1 else "minutes"
    ssf = "second" if ss == 1 else "seconds"
    construct = [f"{x[0]} {x[1]}" for x in list(zip([yy, dd, hh, mm, ss], [yyf, ddf, hhf, mmf, ssf])) if x[0] != 0]
    if len(construct) == 1:
        return construct[0]
    correct = ""
    for i, e in enumerate(construct, 1):
        if i == 1:
            correct += e
        elif i != len(construct):
            correct += ", "+e
        else:
            correct += " and "+e
    return correct


class CaesarCipher:
    """Encodes to and from a caesar cipher"""
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        st = st.upper()
        shift = self.shift
        return "".join([c if not c.isalpha() else chr(ord(c)+shift) if ord(c)+shift in range(65, 91)
                        else chr(ord(c)-26+shift) for c in st])

    def decode(self, st):
        st = st.upper()
        shift = self.shift
        return "".join([c if not c.isalpha() else chr(ord(c)-shift) if ord(c)-shift in range(65, 91)
                        else chr(ord(c)+26-shift) for c in st])