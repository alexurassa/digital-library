import uuid


class UUIDGenerator:
    """Generates UUID Tokens"""

    @classmethod
    def generate_string_token(cls, length: int = 16, is_upper: bool = False) -> str:
        """Generates a string based token with no spaces default to \'16 chars\' long
        and \'lowercase\'
        """

        token = str(uuid.uuid1()).replace("-", "")[:length]
        if is_upper:
            return token.upper()
        return token
