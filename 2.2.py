#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

counter = 0

if a % 2 == 0:
    counter += 1

if b % 2 == 0:
    counter += 1

if c % 2 == 0:
    counter += 1

print counter