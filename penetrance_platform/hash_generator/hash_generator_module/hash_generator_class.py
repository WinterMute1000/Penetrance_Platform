import hashlib


class HashGeneratorClass:
    @staticmethod
    def md5_encrypt(target_str):
        return hashlib.md5(target_str.encode()).hexdigest()

    @staticmethod
    def sha1_encrypt(target_str):
        return hashlib.sha1(target_str.encode()).hexdigest()

    @staticmethod
    def sha256_encrypt(target_str):
        return hashlib.sha256(target_str.encode()).hexdigest()

    @staticmethod
    def sha512_encrypt(target_str):
        return hashlib.sha512(target_str.encode()).hexdigest()
