def format_duration(secs):
    """Formats seconds to minutes, days, hours, etc. Time complexity: O(1). Space complexity: O(1)"""
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
    def __init__(self, shift=23):
        self.shift = shift

    def encode(self, st):
        """Time complexity: O(n). Space complexity: O(n)"""
        st = st.upper()
        shift = self.shift
        return "".join([c if not c.isalpha() else chr(ord(c)+shift) if ord(c)+shift in range(65, 91)
                        else chr(ord(c)-26+shift) for c in st])

    def decode(self, st):
        """Time complexity: O(n). Space complexity: O(n)"""
        st = st.upper()
        shift = self.shift
        return "".join([c if not c.isalpha() else chr(ord(c)-shift) if ord(c)-shift in range(65, 91)
                        else chr(ord(c)+26-shift) for c in st])


def rgb(r, g, b):
    """Converts RGB to hex values. Time complexity: O(1). Space complexity: O(1)"""
    take_closest = lambda num, collection: min(collection, key=lambda x: abs(x - num))
    rgb_range = [0, 255]
    r = take_closest(r, rgb_range) if r not in range(255) else r  # O(log n) for lookup in range
    g = take_closest(g, rgb_range) if g not in range(255) else g
    b = take_closest(b, rgb_range) if b not in range(255) else b
    r, g, b = hex(r)[2:], hex(g)[2:], hex(b)[2:]
    return f"{r.zfill(2)}{g.zfill(2)}{b.zfill(2)}".upper()


if __name__ == "__main__":
    a = CaesarCipher()
    to_print = [format_duration(3754), a.encode("Hello world!"), a.decode(a.encode("Hello world!")),
                rgb(145, 233, 999), ]
    for f in to_print:
        print(f)
