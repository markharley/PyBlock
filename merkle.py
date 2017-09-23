import hashlib


def hash_sha256(obj):
    sha = hashlib.sha256()
    sha.update(obj)
    return sha.hexdigest()


def merkle_double_hash(h1, h2):
    first = hash_sha256(str(h1) + str(h2))
    return hash_sha256(first)


def compute_merkle(transactions):
    hashed_transactions = map(lambda x: hash_sha256(str(x)), transactions)
    return recurse_step(hashed_transactions)


def recurse_step(hashes):
    if len(hashes) == 0:
        return 0
    elif len(hashes) == 1:
        return hashes[0]

    intermediate = []
    for i in range(0, len(hashes), 2):
        a = hashes[i]
        if i + 1 >= len(hashes):
            b = ''
        else:
            b = hashes[i+1]
        intermediate.append(merkle_double_hash(a, b))
    return recurse_step(intermediate)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 5]
    b = [1, 2, 3, 4, 5]
    print compute_merkle(a)
    print compute_merkle(b)

