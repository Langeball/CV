def format_duration(secs: int) -> str:
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
    def __init__(self, shift: int = 23):
        self.shift = min(max(shift, 1), 25)  # Prevents edge cases, ie: 0 and below or 26 and above

    def encode(self, st: str) -> str:
        """Time complexity: O(n). Space complexity: O(n)"""
        st = st.upper()  # For simplicity. Upper and lowercase don't share same values in Unicode
        shift = self.shift
        return "".join([c if not c.isalpha() else chr(ord(c)+shift) if ord(c)+shift in range(65, 91)
                        else chr(ord(c)-26+shift) for c in st])

    def decode(self, st: str) -> str:
        """Time complexity: O(n). Space complexity: O(n)"""
        st = st.upper()
        shift = self.shift
        return "".join([c if not c.isalpha() else chr(ord(c)-shift) if ord(c)-shift in range(65, 91)
                        else chr(ord(c)+26-shift) for c in st])


def rgb(r: int, g: int, b: int) -> str:
    """Converts RGB to hex values. Time complexity: O(1). Space complexity: O(1)"""
    take_closest = lambda num, collection: min(collection, key=lambda x: abs(x - num))
    rgb_range = [0, 255]
    r = take_closest(r, rgb_range) if r not in range(255) else r  # O(log n) for lookup in range
    g = take_closest(g, rgb_range) if g not in range(255) else g
    b = take_closest(b, rgb_range) if b not in range(255) else b
    r, g, b = hex(r)[2:], hex(g)[2:], hex(b)[2:]
    return f"{r.zfill(2)}{g.zfill(2)}{b.zfill(2)}".upper()


def quicksort(sequence: List[int]) -> List[int]:
    """t: O(n log n) // s: O(log n) // Unstable version"""
    len_seq = len(sequence)
    if len_seq <= 1:
        return sequence
    pivot_index = randint(1, len_seq-1)  # Random pivot
    pivot = [sequence[pivot_index]]
    higher = []
    lower = []
    for n in sequence[:pivot_index]+sequence[pivot_index+1:]:
        if n > pivot[0]:
            higher.append(n)
        else:
            lower.append(n)
    return quicksort(lower) + pivot + quicksort(higher)


if __name__ == "__main__":
    a = CaesarCipher()
    to_print = [format_duration(3754), a.encode("Hello world!"), a.decode(a.encode("Hello world!")),
                rgb(145, 233, 999), quicksort([7, 6, 5, 4, 3, 2, 1]), ]
    for f in to_print:
        print(f)
