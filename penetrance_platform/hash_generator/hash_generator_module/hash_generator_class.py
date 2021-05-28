import hashlib


class HashGeneratorClass:
    @staticmethod
    def md5_encrypt(target_str):
        return hashlib.md5(target_str.encode()).hexdigest()

    @staticmethod
    def md5_decrypt(target_str):
        result = ""
        for i in range(target_str):
            result = target_str.replace(hashlib.md5(chr(i).encode()).hexdigest(), chr(i))

        return result

    @staticmethod
    def sha1_encrypt(target_str):
        return hashlib.sha1(target_str.encode()).hexdigest()

    @staticmethod
    def sha1_decrypt(target_str):
        result = ""
        for i in range(target_str):
            result = target_str.replace(hashlib.sha1(chr(i).encode()).hexdigest(), chr(i))

        return result

    @staticmethod
    def sha256_encrypt(target_str):
        return hashlib.sha256(target_str.encode()).hexdigest()

    @staticmethod
    def sha256_decrypt(target_str):
        result = ""
        for i in range(target_str):
            result = target_str.replace(hashlib.sha256(chr(i).encode()).hexdigest(), chr(i))

        return result

    @staticmethod
    def sha512_encrypt(target_str):
        return hashlib.sha512(target_str.encode()).hexdigest()

    @staticmethod
    def sha512_decrypt(target_str):
        result = ""
        for i in range(target_str):
            result = target_str.replace(hashlib.sha512(chr(i).encode()).hexdigest(), chr(i))

        return result




