# role panel bot Utilities
from typing import Iterable

import random


unicode_a = 0x1f1e6


colors = {
    "default": 0x000000,
    "white": 0xffffff,
    "aqua": 0x1abc9c,
    "green": 0x57f287,
    "blue": 0x3498db,
    "yellow": 0xfee75c,
    "purple": 0x9b59b6,
    "luminousvividpink": 0xe91e63,
    "fuchsia": 0xeb459e,
    "gold": 0xf1c40f,
    "orange": 0xe67e22,
    "red": 0xed4245,
    "grey": 0x95a5a6,
    "navy": 0x34495e,
    "darkaqua": 0x11806a,
    "darkgreen": 0x1f8b4c,
    "darkblue": 0x206694,
    "darkpurple": 0x71368a,
    "darkVividpink": 0xad1457,
    "darkgold": 0xc27c0e,
    "darkorange": 0xa84300,
    "darkred": 0x992d22,
    "darkgrey": 0x979c9f,
    "darkergrey": 0x7f8c8d,
    "lightgrey": 0xbcc0c0,
    "darknavy": 0x2c3e50,
    "blurple": 0x5865f2,
    "greyple": 0x99aab5,
    "darkbutnotblack": 0x2c2f33,
    "notquiteblack": 0x23272a
}


def get_color(cl: str) -> int:
    """文字列から色を表す数字に変換します。

    対応する書き方
    - 上の一覧にある色指定コード
    - random(適当に色を決めます)
    - カンマ区切りでかかれたRGBのコード(10進)
    - 16進で書かれたRGBコード(`0x`はあってもなくてもok)
    - 10進のただの数字
    """
    x = colors.get(cl.lower().replace("_", ""), cl.lower())
    if isinstance(x, int):
        return x
    if x == "random":
        return random.randint(0, 0xffffff)
    if "," in x:
        x = x.replace(" ", "").split(",")
        try:
            return int(x[0])*0x10000 + int(x[1])*0x100 + int(x[2])
        except:
            return -1
    if x.startswith("0x"):
        try:
            return int(x, 0)
        except:
            return -1
    if x.isdigit():
        return int(x)
    try:
        return int(x, 16)
    except:
        return -1


def get_next_alphabet_int(emojis: Iterable[str]) -> str:
    used = [False]*26
    for emoji in emojis:
        if len(emoji) == 1 and (ord(emoji)-unicode_a) < 26:
            used[ord(emoji)-unicode_a] = True
    for i in range(25):
        if used[i]:
            return chr(unicode_a+i)
    return chr(unicode_a+26)

def get_panel_data_from_content(content: str) -> dict[str, int] | str:
    raw_data = content.splitlines()
    panel_data = {}
    for item in raw_data:
        if len(item.split(":")) != 2:
            return "正しいパネル形式ではありません。"
        emoji, role_mention = item.split(":")
        role_id = role_mention.split("&")[1].replace(">", "")
        if not role_id.isdigit():
            return "正しいパネル形式ではありません。"
        panel_data[emoji] = int(role_id)
    return panel_data or "正しいパネル形式ではありません。"
