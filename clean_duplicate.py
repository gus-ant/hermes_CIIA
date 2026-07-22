with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Delete everything between line 681's comment and </div> before Reveal JS script
idx1 = content.find('        <!-- Slide: Conclusão da Parte 3 / Ponte para a Parte 4 -->')
if idx1 != -1:
    idx2 = content.find('    <!-- Reveal.js JS -->')
    if idx2 != -1:
        content = content[:idx1] + '\n' + content[idx2:]

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Duplicate section cleaned successfully.")
