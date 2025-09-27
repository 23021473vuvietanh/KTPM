def choose(t, ph, h):
    if t < 20 or t > 30:
        return "Lỗi input"
    
    if ph < 4 or ph > 7:
        return "Lỗi input"
    
    if h < 0 or h > 5.5:
        return "Lỗi input"

    if t >= 27 and ph >= 6.5 and h >= 4.5:
        return "Thả bạch tuộc"

    elif t >= 25 and ph >= 5.5 and h >= 4.5:
        return "Thả cá"

    elif t >= 25 and ph >= 4 and h >= 3:
        return "Thả tôm"

    return "Không thả gì"

def main():
    t, ph, h = map(float, input().split())
    print(choose(t, ph, h))

if __name__ == "__main__":
    main()
