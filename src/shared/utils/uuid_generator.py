import uuid


class UUIDGenerator:
    """Generates UUID Tokens"""

    @classmethod
    def generate_string_token(
        cls, length: int = 16, is_upper: bool = False, has_dashes: bool = False
    ) -> str:
        """Generates a string based token with no spaces default to \'16 chars\' long
        and \'lowercase\'
        """
        if has_dashes:
            token = str(uuid.uuid1())[:length]
        else:
            token = str(uuid.uuid4()).replace("-", "")[:length]

        if is_upper:
            return token.upper()
        return token
