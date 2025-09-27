def main():
    t, ph, h = map(float, input().split())

    if t < 20 or t > 30:
        print("Lỗi đầu vào, vui lòng thử lại!")
        return -1

    if ph < 4 or ph > 7:
        print("Lỗi đầu vào, vui lòng thử lại!")
        return -1

    if h < 0 or h > 5.5:
        print("Lỗi đầu vào, vui lòng thử lại!")
        return -1

    if t >= 27 and ph >= 6.5 and h >= 4.5:
        print("Thả bạch tuộc")

    elif t >= 25 and ph >= 5.5 and h >= 4.5:
        print("Thả cá")

    elif t >= 25 and ph >= 4 and h >= 3:
        print("Thả tôm")

    return 0

if __name__ == "__main__":
    main()
