import random

def nim_game():
    heap_size=29
    current_player="Max"
    if heap_size>0:
        print(f"current heap size={heap_size}")

    if current_player=="Max":
        move=max_heap_move(heap_size)

    else:
        move=min_heap_move(heap_size)

    print(f"{current_player} removed {move} matchstics")
    heap_size-=move

    current_player="Min" if current_player=="Max" else "Max"

    print(f"{current_player} wins")


def max_heap_move(heap_size):
    a=int(heap_size/2)
    b=heap_size-a-1
    return b

def min_heap_move(heap_size):
    b=int(heap_size/2)
    if b>0:
        a=random.randint(1,b)
    else:
        a=random.randint(1,heap_size)

    return b

if __name__=="__main__":
    nim_game()
