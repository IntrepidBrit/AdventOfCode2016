def room_validator(room_name):
    count_dict = {}
    cipher_sector, checksum = room_name.split("[")
    ciphertext, sector_id = cipher_sector.rsplit("-", maxsplit=1)
    for character in ciphertext:
        if character.isalnum():
            try:
                count_dict[character] += 1
            except KeyError:
                count_dict[character] = 1

    calculated_checksum = "".join(v[0] for v in sorted(count_dict.items(), key=lambda c: (-c[1], ord(c[0]))))[0:5]

    if calculated_checksum == checksum[:-1]:
        return int(sector_id)
    else:
        return 0


def sum_sector_ids(room_entries):
    return sum(map(room_validator, room_entries.split("\n")))
