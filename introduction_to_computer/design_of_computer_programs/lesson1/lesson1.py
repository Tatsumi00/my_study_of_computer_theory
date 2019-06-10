#自己的解决方法，借鉴标准答案，但获得理解
#1观察学习2尝试应用3学会

#a poker program
# ?->problem->special->codes


#hand.card.rank suit
#poker(hands)->hand
#hand rank


#1.选择数据结构，确保正确性
#如何表示一手牌

#2.poker function
#max函数，key参数

#3. hand_rank function
#普通排序->高阶排序

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

#!!!card_ranks function
def card_ranks(hand):
    #!!!数组相关下标的应用
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

#straight function
#???自己实现
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."

#!!!flush function
def flush(hand):
    "Return True if all the cards have the same suit"
    # !!!数组相关下标的应用
    suits=[s for r,s in hand]
    return len(set(suits))==1

#!!!kind function
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        #出现次数等于n
        #数值较大，因为反向排序
        if ranks.count(r)==n:
            return r
        return None
#two_pair function
#my answer
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    i = 0
    twopair = ()
    for r in ranks:
        if ranks.count(r) == 2:
            twopair[i] = r
            i + 1
    if i == 1:
        twopair.sort(reverse=True)
        return twopair
    else:
        return None

"""
def two_pair(ranks):
    pair=kind(2, ranks)
    lowpair=kind(2,list(reversed(ranks)))
    if pair and lowpair!=pair:
        return (pair, lowpair)
    else:
        return None
"""

#单元测试
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "TD 9H TH 7C 3S".split() # Two Pair
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'












