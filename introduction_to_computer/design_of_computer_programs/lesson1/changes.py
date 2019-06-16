#问题：poker game中的特殊情况 A 2 3 4 5
#ace low straight

#修改card_ranks
'''
def card_ranks(hand):
    #!!!数组相关下标的应用
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks
'''

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

#!!!问题：ties，如何区别
#修改poker
'''
def poker(hands):
    return max(hands, key=hand_rank)
'''

def poker(hands):
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None)

#!!!问题：解决deal
#my answer
import random
mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']
def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    if (n * numhands > mydeck.len()):
        return None
    else:
    # 分隔数组每5个
    # 指定给各个人员
        return poker()

#standard answer
'''
import random
mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']
def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
'''






