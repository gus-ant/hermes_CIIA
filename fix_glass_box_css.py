with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('max-width: 900px;', 'max-width: 1250px;')

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated .glass-box max-width to 1250px in Part 3.")
