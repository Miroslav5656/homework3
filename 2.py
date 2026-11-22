def ticket_total(count,price=12):
    return count*price
def final_price(count, is_school_group=False):
    total=ticket_total(count) 
    if is_school_group:
        return total*0.75
    return total
print(f"3 обычных билета: {ticket_total(3)} руб.")
print(f"4 билета для школьной группы: {final_price(4,is_school_group=True)} руб.")
print(f"2 билета по 15 рублей: {ticket_total(2,price=15)} руб.")