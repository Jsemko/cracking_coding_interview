

def convert(num):

    if num < 0 or num > 1:
        print('Nope')
        return

    cur_ans = '0.'
    for _ in range(33):
        if num:
            num *= 2
            cur_ans += '%d' % int(num // 1)
            num %= 1
        else:
            break
    else:
        print('Error')
        return

    print(cur_ans)

convert(1)
convert(.25)
convert(1234/(2**11))

