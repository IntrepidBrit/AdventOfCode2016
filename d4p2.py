def room_validator(ciphertext, sector_id, checksum):
    count_dict = {}
    for character in ciphertext:
        if character.isalnum():
            try:
                count_dict[character] += 1
            except KeyError:
                count_dict[character] = 1

    calculated_checksum = "".join(v[0] for v in sorted(count_dict.items(), key=lambda c: (-c[1], ord(c[0]))))[0:5]

    if calculated_checksum == checksum:
        return int(sector_id)
    else:
        return 0


def parse_room_entry(room_entry):
    cipher_sector, checksum = room_entry.split("[")
    ciphertext, sector_id = cipher_sector.rsplit("-", maxsplit=1)
    return ciphertext, int(sector_id), checksum[:-1]


def shift_character(c, shift_amount):
    return chr(((ord(c) + shift_amount - 97) % 26) + 97) if c != "-" else " "


def decrypt_caeser_cipher(cipher_text, shift_amount):
    return "".join([shift_character(c, shift_amount) for c in cipher_text])

def print_all_room_names(room_entries):
    for re in room_entries.split("\n"):
        ct, si, chk = parse_room_entry(re)
        print(decrypt_caeser_cipher(ct,si))

def find_north_pole_object_storage(room_entries):
    for re in room_entries.split("\n"):
        ct, si, chk = parse_room_entry(re)
        if room_validator(ct, si, chk) > 0 and decrypt_caeser_cipher(ct, si) == "northpole object storage":
            return si