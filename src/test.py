from src.entity.Point import Point

if __name__ == '__main__':
    s="beijingshijian "
    res="'"
    for n in s:
        res+=n
        res+="','"
    print(res)
