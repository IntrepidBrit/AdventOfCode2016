import collections


def jamming_error_correction(received_data, r=8):
    counts = [collections.Counter() for _ in range(r)]
    for line in received_data.split("\n"):
        for i in range(len(line)):
            counts[i][line[i]] += 1

    return "".join(map(lambda l: str(l.most_common()[-1][0]), counts))
