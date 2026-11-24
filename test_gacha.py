# 每条 test_ 开头就是一个用例，pytest 会自动找出来跑。
# 先跑通示例，再写下面 5 条。

from gacha import new_state, draw, COST, PITY_MAX


# ===================== 示例（照着这个格式写） =====================
def test_第90抽必出五星():
    s = new_state()
    s["currency"] = 99999              # 排除资源干扰
    for _ in range(PITY_MAX - 1):
        draw(s, False)

    assert s["pity"] == PITY_MAX - 1   # 应该正好 89

    result = draw(s, False)            # 第 90 抽

    assert result["hit"] is True       # 必出
    assert s["pity"] == 0              # 计数归零


# ===================== 你来写这 5 条 =====================

# 1. 资源不足：不扣钱、不抽、返回 ok=False
#    提示：把 currency 改成 COST - 1，然后 draw 一次
# def test_...():
#     ...
def test_资源不足时不扣不抽():
    s= new_state()
    s["currency"]=159

    result= draw(s,False)

    assert result["ok"] is False
    assert s["currency"] == 159
    assert s["total"] ==0

# 2. 边界：第 89 抽不该出五星
#    提示：循环 88 次，第 89 次 draw 后断言 hit is False
# def test_...():
# 
def test_第89抽不该出5星():
    s = new_state()
    s ["currency"]=99999
    for _ in range(PITY_MAX - 2):
        draw(s,False)
    result = draw(s,False)
    assert result["hit"] is False
    assert s["pity"]==89

# 3. 歪了之后，guaranteed 变 True
#    提示：draw(s, True, is_up=False) 之后看 s["guaranteed"]
# def test_...():
#     ...
def test_歪了之后进入大保底():
    s= new_state()
    draw(s,True,is_up=False)

    assert s["guaranteed"] is True

# 4. 大保底出货后，guaranteed 变回 False
#    提示：先歪一次，再 draw(s, True, is_up=True)
# def test_...():
#
def test_大保底出货后归False():
    s = new_state()
    draw(s,True,is_up=False)
    assert s["guaranteed"] is True
    draw(s,True,is_up=True)
    assert s["guaranteed"] is False


# 5. 连点两次：扣 320，总抽数 2
#    提示：连续调两次 draw(s, False)，断言 currency 少了 COST*2
# def test_...():
#     ...