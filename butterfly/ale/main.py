def main():
    n = 3
    if n < 3:
        return

    cols = 2 * n - 1
    rows = 2 * (n - 2) + 1

    half_width = (cols - 1) // 2
    half_height = (rows - 1) // 2

    center = '\\ /'
    stripes = '*-'

    for row in range(rows):
        if row == half_height:
            print(' ' * half_width + '@')
            center = '/ \\'
            continue
        wing = stripes[row % len(stripes)] * (half_width - 1)
        print(wing + center + wing)

if __name__ == '__main__':
    main()
