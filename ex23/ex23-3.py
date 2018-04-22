import sys
script, input_encoding, error = sys.argv


def main(byte_file, encoding, errors):
    line = byte_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(byte_file, encoding, errors)


def print_line(line, encoding, errors):
    next_byte = bytes(line.strip().decode('unicode-escape').encode('latin-1'))
    cooked_string = next_byte.decode(encoding, errors=errors)
    raw_bytes = cooked_string.encode(encoding, errors=errors)
    print(cooked_string, "<===>", raw_bytes)


lang_bytes = open("ex23/bytes.txt", 'rb')

main(lang_bytes, input_encoding, error)