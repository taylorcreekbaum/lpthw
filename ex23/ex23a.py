import sys
script, input_encoding, error = sys.argv


def main(language_file, byte_file, encoding, errors):
    line = language_file.readline()

    if line:
        export_line(line, byte_file, encoding, errors)
        return main(language_file, byte_file, encoding, errors)


def export_line(line, byte_file, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    byte_file.write(str(raw_bytes)[2:-1] + '\n')
    print(raw_bytes, "<===>", cooked_string)


languages = open("ex23/languages.txt", encoding="utf-8")
lang_bytes = open("ex23/bytes.txt", 'wb', encoding="utf-8")

main(languages, lang_bytes, input_encoding, error)