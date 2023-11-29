from hashlib import sha256, sha512, sha1, md5, sha224, sha384, sha3_224, sha3_256, sha3_384, sha3_512, blake2b, \
                     blake2s, shake_128, shake_256


HASH_ALGORITHMS = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256,
    'sha512': sha512,
    'sha224': sha224,
    'sha384': sha384,
    'sha3_224': sha3_224,
    'sha3_256': sha3_256,
    'sha3_384': sha3_384,
    'sha3_512': sha3_512,
    'blake2b': blake2b,
    'blake2s': blake2s,
    'shake_128': shake_128,
    'shake_256': shake_256
}


def hashing_algos() -> list[str]:
    return list(HASH_ALGORITHMS.keys())


def has_hashing_algo(algo: str) -> bool:
    return algo.lower().strip() in HASH_ALGORITHMS


def hash_file(file_path: str, algo: str) -> str:
    """
    Hash a file using the given hash type.
    """
    with open(file_path, 'rb') as file:
        return HASH_ALGORITHMS[algo](file.read()).hexdigest()


def hash_string(text: str, algo: str) -> str:
    """
    Hash a string using the given hash type.
    """
    if isinstance(text, str):
        text = text.encode('utf-8')
    return HASH_ALGORITHMS[algo](text).hexdigest()

