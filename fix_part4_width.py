with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte4.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('width: 1100,', 'width: 1400,')
content = content.replace('max-width: 950px;', 'max-width: 1320px;')

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte4.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Part 4 width.")
