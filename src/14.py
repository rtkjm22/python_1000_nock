from enum import Enum

# Lang = Literal["ja", "en"]
# SUPPORTED_LANGS: tuple[Lang, ...] = ("ja", "en")


# def greet_user(name: str, lang: Lang) -> str:
#     if lang not in SUPPORTED_LANGS:
#         raise ValueError("Unsupported language.")
#     match lang:
#         case "ja":
#             return f"こんにちは、{name}さん"
#         case "en":
#             return f"Hello, {name}!"


class Lang(str, Enum):
    JA = "ja"
    EN = "en"


def greet_user(name: str, lang: Lang) -> str:
    if lang not in Lang._value2member_map_:
        raise ValueError("Unsupported language.")
    match lang:
        case Lang.JA:
            return f"こんにちは、{name}さん"
        case Lang.EN:
            return f"Hello, {name}!"


print(greet_user("なお", Lang.JA))
print(greet_user("なお", Lang.EN))
