for t in range(int(input())):
    n = input()
    a = []
    b = []
    c = []
    for i in range(len(n)):
        if i == 0:
            a.append('..#..')
        else:
            a.append('.#..')
    for i in range(len(n)):
        if i == 0:
            b.append('.#.#.')
        else:
            b.append('#.#.')
    for i in range(len(n)):
        if i == 0:
            c.append(f'#.{n[i]}.#')
        else:
            c.append(f'.{n[i]}.#')
    print(''.join(a),''.join(b),''.join(c),''.join(b),''.join(a),sep='\n')