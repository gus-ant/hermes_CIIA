import re

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Reveal.js width to 1400
content = content.replace('width: 1100,', 'width: 1400,')

# 2. Update flex containers max-width from 1050px to 1320px
content = content.replace('max-width: 1050px;', 'max-width: 1320px;')

# 3. Give text side flex: 1.4 instead of flex: 1
content = content.replace('flex: 1; text-align: left;', 'flex: 1.4; text-align: left;')

# 4. Make glass boxes slightly more compact in padding
content = content.replace('padding: 25px;', 'padding: 18px 24px;')

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Part 3 slide canvas width and text column proportions.")
