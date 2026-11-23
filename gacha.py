"""抽卡逻辑 v2：加入货币与大小保底。"""

COST = 160          # 单抽价格
PITY_MAX = 90       # 硬保底


def new_state():
    return {
        "currency": 1600,    # 初始资源
        "pity": 0,           # 距上次五星抽了多少次
        "guaranteed": False, # 下次五星是否大保底
        "total": 0,          # 总抽数
    }


def draw(state, is_five_star, is_up=True):
    """抽一次。

    返回 {"ok": 是否成功抽卡, "hit": 是否出五星}
    """
    if state["currency"] < COST:
        return {"ok": False, "hit": False}      # 资源不足：不扣不抽

    state["currency"] -= COST
    state["pity"] += 1
    state["total"] += 1

    hit = is_five_star or state["pity"] >= PITY_MAX
    if hit:
        state["pity"] = 0
        state["guaranteed"] = not is_up          # 歪了 -> 下次大保底
    return {"ok": True, "hit": hit}