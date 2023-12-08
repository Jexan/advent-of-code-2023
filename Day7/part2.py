import functools


order = (
    "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"
)


@functools.total_ordering
class Hand():
    position = 0
    
    def __init__(self, flush: str, wager: int):
        self.flush = flush
        self.wager = wager
        
        if 'J' in flush:
            replaced_jokers = (flush.replace("J", i) for i in order)
            self.rank = min(map(self.get_rank, replaced_jokers))
        else:
            self.rank = self.get_rank(flush)
    
    def get_rank(self, flush):
        unique_set = frozenset(flush)
        len_unique_set = len(unique_set)
        
        if len_unique_set == 1:
            return 1
        elif len_unique_set == 2:    
            for i in unique_set:
                how_many = flush.count(i)
                if how_many in (1, 4):
                    return 2
                elif how_many in (2, 3):
                    return 3
        elif len_unique_set == 3:
            for i in unique_set:
                how_many = flush.count(i)
                if how_many == 3:
                    return 4
                if how_many == 2:
                    return 5 
        elif len_unique_set == 4:
            return 6

        return 7
    
    def __lt__(self, other):
        if self.rank == other.rank:
            for s_1, o_1 in zip(self.flush, other.flush):
                order_s_1 = order.index(s_1)
                order_o_1 = order.index(o_1)
                
                if order_o_1 != order_s_1:
                    return order_s_1 > order_o_1
        else:
            return self.rank > other.rank
        
    def __eq__(self, other):
        return False
    
    def __repr__(self):
        return f"{self.flush} - {self.rank} - {self.position}"
    
def decode_lines(l: str):
    flush, wager = l.split()
    
    return Hand(flush, wager)
            

def decode_message():
    with open("input1.txt") as f:
        hands = [decode_lines(l) for l in f.readlines()]
        
    hands.sort()
    
    total = 0
    
    for i, hand in enumerate(hands, 1):
        hand.position = i
        total += int(hand.wager)*i
        
    print(hands)
    return total
            
            
result = decode_message()
print(result)