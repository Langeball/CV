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