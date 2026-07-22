with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove duplicate conclusion section if present
duplicate_marker = """            <!-- Slide: Conclusão da Parte 3 / Ponte para a Parte 4 -->"""
first_idx = content.find(duplicate_marker)
if first_idx != -1:
    second_idx = content.find(duplicate_marker, first_idx + len(duplicate_marker))
    if second_idx != -1:
        # cut out from second_idx to </div> before script tag
        end_idx = content.find("    </div>\n\n    <!-- Reveal.js JS -->", second_idx)
        if end_idx != -1:
            content = content[:second_idx] + content[end_idx:]

# Update the conclusion slide styling
old_glass = """                <div class="glass-box"
                    style="padding: 25px 35px; text-align: left; max-width: 900px; margin: 0 auto; border-left: 5px solid var(--neon-green);">"""

new_glass = """                <div class="glass-box"
                    style="padding: 20px 30px; text-align: left; max-width: 1250px; width: 100%; margin: 0 auto; border-left: 5px solid var(--neon-green);">"""

content = content.replace(old_glass, new_glass)

# Make heading line-height/margins slightly tighter
content = content.replace('margin-bottom: 15px;">\n                    O Cérebro do Hermes', 'margin-bottom: 10px; font-size: 2.5em;">\n                    O Cérebro do Hermes')

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed last slide width and removed duplicate slide.")
