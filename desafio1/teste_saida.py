import sys

respostas_corretas = sys.argv[1]
outputs = sys.argv[2]

with open(respostas_corretas) as f:
    content_resp = f.readlines()
    
with open(outputs) as f:
    content_output = f.readlines()
    
for i in range(0, len(content_resp)):
    assert content_resp[i] == content_output[i], f"Linha {i + 1}: Resp. Errada"
print(f"All {len(content_resp)} tests passed!")