import binascii
import sys
import pysnooper
import time

class SM3:
    MAX = 2 ** 32
    IV = "7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e"

    def __init__(self, string):
        self.input = string
        self.b_input = bytes(self.input, "utf-8")
        self.hex_input = hex(int.from_bytes(self.b_input, "big"))[2:]  # 按照大端计算

    @property
    def hash(self):
        return self.iterationCourse(self.fill(self.hexToBin(self.hex_input)))[-1]

    def getT(self, j):
        if 0 <= j <= 15:
            return int("79cc4519", 16)
        elif 16 <= j <= 63:
            return int("7a879d8a", 16)

    def FF(self, X, Y, Z, j):
        if 0 <= j <= 15:
            return X ^ Y ^ Z
        elif 16 <= j <= 63:
            return (X & Y) | (X & Z) | (Y & Z)
        else:
            return 0

    def GG(self, X, Y, Z, j):
        if 0 <= j <= 15:
            return X ^ Y ^ Z
        elif 16 <= j <= 63:
            return (X & Y) | (self.non(X) & Z)
        else:
            return 0

    def P0(self, X):
        return X ^ self.leftRotate(X, 9) ^ self.leftRotate(X, 17)

    def P1(self, X):
        return X ^ self.leftRotate(X, 15) ^ self.leftRotate(X, 23)

    def leftRotate(self, X, k):
        res = list(self.intToBin(X))
        for i in range(k):
            temp = res.pop(0)
            res.append(temp)
        return int("".join(res), 2)

    def fill(self, bin_string):
        tail = "{:064b}".format(len(bin_string))
        bin_string += "1"
        div, mod = divmod(len(bin_string), 512)
        if mod >= 448:
            bin_string += "0" * (512 - mod + 448)
        else:
            bin_string += "0" * (448 - mod)

        return bin_string + tail

    def iterationCourse(self, msg):
        n = len(msg) >> 9
        m = [msg[i <<9:(i + 1) <<9] for i in range(n)]
        V = [self.IV]
        for i in range(n):
            V.append(hex(int(self.intToBin(self.CF(V[-1], m[i]), 256), 2))[2:])

        return V

    def CF(self, Vi, mi):
        msg = Vi
        A = [int(msg[i * 8: (i + 1) * 8], 16) for i in range(len(msg) >> 3)]
        W1, W2 = self.informationExtend(mi)
        for j in range(64):
            factor1 = self.leftRotate(A[0], 12)
            factor2 = self.leftRotate(self.getT(j), j % 32)
            SS1 = self.leftRotate((factor1 + A[4] + factor2) % self.MAX, 7)
            factor3 = self.leftRotate(A[0], 12)
            SS2 = SS1 ^ factor3
            TT1 = (self.FF(A[0], A[1], A[2], j) + A[3] + SS2 + W2[j]) % self.MAX
            TT2 = (self.GG(A[4], A[5], A[6], j) + A[7] + SS1 + W1[j]) % self.MAX
            A[3] = A[2]
            A[2] = self.leftRotate(A[1], 9)
            A[1] = A[0]
            A[0] = TT1
            A[7] = A[6]
            A[6] = self.leftRotate(A[5], 19)
            A[5] = A[4]
            A[4] = self.P0(TT2)
        temp = self.intToBin(A[0], 32) + self.intToBin(A[1], 32) + self.intToBin(A[2], 32) + \
               self.intToBin(A[3], 32) + self.intToBin(A[4], 32) + self.intToBin(A[5], 32) + \
               self.intToBin(A[6], 32) + self.intToBin(A[7], 32)
        temp = int(temp, 2)
        return temp ^ int(Vi, 16)


    def informationExtend(self, mi):
        mi = self.binToHex(mi)
        W1 = [int(mi[i * 8: (i + 1) * 8], 16) for i in range(len(mi) >> 3)]
        for j in range(16, 68):
            p = self.P1(W1[j - 16] ^ W1[j - 9] ^ self.leftRotate(W1[j - 3], 15))
            W1.append(p ^ self.leftRotate(W1[j - 13], 7) ^ W1[j - 6])
        W2 = [W1[j] ^ W1[j + 4] for j in range(64)]

        return W1, W2

    def bigLittleEndianConvert(self, data, need="big"):
        if sys.byteorder != need:
            return binascii.hexlify(binascii.unhexlify(data)[::-1])
        return data

    def hexToBin(self, hex_string):
        res = ""
        for h in hex_string:
            res += '{:04b}'.format(int(h, 16))
        return res

    def binToHex(self, bin_string):
        res = ""
        for i in range(len(bin_string) >> 2):
            s = bin_string[i * 4: (i + 1) * 4]
            res += '{:x}'.format(int(s, 2))
        return res

    def msgToHex(self, msg):
        return msg.encode("utf-8").hex()

    def msgToBin(self, msg):
        return self.hexToBin(self.msgToHex(msg))

    def intToBin(self, X, bits=32):
        return ('{:0%db}' % bits).format(X)

    def non(self, X):
        X = self.intToBin(X)
        Y = ""
        for i in X:
            if i == "0":
                Y += "1"
            else:
                Y += "0"
        return int(Y, 2)


if __name__ == "__main__":
    s_time = time.time()
    for i in range(1000):
       print(SM3("abcdefghijklmnopqrstuvwxyz").hash)
    c_time = time.time()
    print(c_time - s_time)


