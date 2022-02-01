#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    u = set('abcdefghijklmnopqrstuvwxyz')
    a = {'b', 'k', 'n', 'o', 'q'}
    b = {'a', 'b', 'k', 'u'}
    c = {'o', 'p'}
    d = {'a', 'm', 'n', 'y', 'z'}
    x = d.intersection(a.union(b))
    y = (u.difference(a).intersection(d)).union(c.difference(b))
    print(f'x = {x}')
    print(f'y = {y}')
