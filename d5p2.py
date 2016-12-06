import hashlib


def is_interesting(door_id, index):
    digest = hashlib.md5("".join([door_id, index]).encode()).hexdigest()
    return digest[5], digest[6] if digest.startswith("00000") and 47 < ord(digest[5]) < 56 else None


def naive_hashthrash_me_a_password(door_id):
    index = 0
    password_count = 0
    password = [None] * 8
    while password_count < 8:
        loc, char = is_interesting(door_id, str(index))
        if loc is not None and char is not None and password[int(loc)] is None:
            password[int(loc)] = char
            password_count += 1
        index += 1
    return "".join(password)
