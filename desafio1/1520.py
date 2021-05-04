while True:
  try:
    n_caixas = int(input())
    range_error = False
    if n_caixas > 100:
        break
    lotes = []
    for i in range(0, n_caixas):
        lote_range = input()   
        lote_parafuso, lote_porca = lote_range.split(' ') # x, y
        lote_parafuso, lote_porca = int(lote_parafuso), int(lote_porca)
        print("x:", lote_parafuso, "y", lote_porca)
        if lote_parafuso > lote_porca or lote_porca > 100:
            range_error = True
            break
        if range_error: break
        for j in range(lote_parafuso, lote_porca + 1):
            lotes.append(j)
    lotes = sorted(lotes)            
    pesquisa = int(input())
    found = False
    range_start, range_end = "", ""
    for i, lote in enumerate(lotes):
        if lote == pesquisa:
            if found == False:
                range_start = i
                found = True
            else:
                range_end = i
    if found:
        print(f"{pesquisa} found from {range_start} to {range_end}")
    else:
        print(f"{pesquisa} not found")
  except EOFError:
    break