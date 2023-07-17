from shared.utils import UUIDGenerator


def generateInstanceId(
    instance, length: int, is_upper: bool = False, has_dashes: bool = False
) -> None:
    """Generates a string based instance `id`"""
    instance.id = UUIDGenerator.generate_string_token(length, is_upper, has_dashes)
