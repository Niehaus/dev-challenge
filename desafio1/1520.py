"""
author: Barbara Boechat
date: 03/04/2021

URI PROBLEM 1520 - 'Parafusos e Porcas' -
"""

MAX_NUM_CAIXAS = 100
RANGE_MAX = 100
P_LOTES = 10000

while True:
  try:
    n_caixas = int(input())
    if n_caixas > MAX_NUM_CAIXAS: break 
    range_error = False
    lotes = []
    for i in range(0, n_caixas):
        lote_range = input().split() # x, y
        lote_parafuso, lote_porca = int(lote_range[0]), int(lote_range[1])  
        if lote_parafuso > lote_porca or lote_porca > RANGE_MAX:
            range_error = True
            break
        elif (len(lotes) < P_LOTES):
            for j in range(lote_parafuso, lote_porca + 1):
                lotes.append(j)
    if range_error: break
    lotes = sorted(lotes)    
    pesquisa = int(input())
    found = False
    range_start, range_end = None, None
    for i, lote in enumerate(lotes):
        if lote == pesquisa:
            if found == False:
                range_start = i
                found = True
            else:
                range_end = i
    if found:
        if range_end == None:
            range_end = range_start
        print(f"{pesquisa} found from {range_start} to {range_end}")
    else:
        print(f"{pesquisa} not found")
  except (EOFError, ValueError) as e:
    break
