def main():
    sprites = [
        [
            0b1110,
            0b1010,
            0b1010,
            0b1110,
        ],
        [
            0b0100,
            0b1100,
            0b0100,
            0b1110,
        ],
        [
            0b1100,
            0b0100,
            0b1000,
            0b1110,
        ],
        [
            0b1110,
            0b0010,
            0b1110,
            0b1110,
        ],
        [
            0b1010,
            0b1110,
            0b0010,
            0b0010,
        ],
        [
            0b1110,
            0b1000,
            0b0110,
            0b1110,
        ],
        [
            0b1110,
            0b1000,
            0b1110,
            0b1110,
        ],
        [
            0b1110,
            0b0100,
            0b1000,
            0b1000,
        ],
        [
            0b1110,
            0b1110,
            0b1010,
            0b1110,
        ],
        [
            0b1110,
            0b1110,
            0b0010,
            0b1110,
        ],
    ]

    num_to_word_map = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}

    for i, ten in enumerate(sprites):
        for j, one in enumerate(sprites):
            print("sprite SMALL_" + num_to_word_map[i] + "_" + num_to_word_map[j])
            for ten_byte, one_byte in zip(ten, one):
                byte = (ten_byte << 4) + one_byte
                print("\t" + to_byte_repr(byte))
            print("endsprite")


def to_byte_repr(n):
    out = ""
    for _ in range(8):
        out = out + str(n % 2)
        n = n >> 1
    out = out[::-1]
    out = "0b" + out
    return out


if __name__ == "__main__":
    main()
