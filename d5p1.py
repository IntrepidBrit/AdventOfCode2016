import hashlib


def is_interesting(door_id, index):
    digest = hashlib.md5("".join([door_id, index]).encode()).hexdigest()
    return digest[5] if digest.startswith("00000") else ""


def naive_hashthrash_me_a_password(door_id):
    index = 0
    password = ""
    while len(password) < 8:
        password = "".join([password, is_interesting(door_id, str(index))])
        index += 1
    return password
