import re

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Slide 5: Add print_antigravity.png
s5_target = """                    <p style="font-size: 0.9em; margin-top: 20px; color: #a5a5c5;">
                        (O Antigravity cria as pastas, baixa o orquestrador e valida a instalação de forma 100% autônoma, sem você digitar nenhum código complexo)
                    </p>"""
s5_replace = """                    <img src="print_antigravity.png" alt="Antigravity trabalhando" style="border-radius: 10px; max-width: 800px; margin-top: 15px; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">
                    <p style="font-size: 0.9em; margin-top: 10px; color: #a5a5c5;">
                        (O Antigravity cria as pastas, baixa o orquestrador e valida a instalação de forma 100% autônoma, sem você digitar nenhum código complexo)
                    </p>"""
content = content.replace(s5_target, s5_replace)

# Slide 7: Add print_openrouter.png
s7_target = """                        <li>Vá em <strong>"Keys"</strong> e clique em <em>Create Key</em></li>
                        <li>Copie o código gigante (ex: <code>sk-or-v1-xxxx...</code>)</li>
                    </ol>
                </div>"""
s7_replace = """                        <li>Vá em <strong>"Keys"</strong> e clique em <em>Create Key</em></li>
                        <li>Copie o código gigante (ex: <code>sk-or-v1-xxxx...</code>)</li>
                    </ol>
                    <img src="print_openrouter.png" alt="OpenRouter API Key" style="border-radius: 12px; max-width: 650px; display: block; margin: 15px auto 0 auto; box-shadow: 0 10px 30px rgba(255, 0, 127, 0.3);">
                </div>"""
content = content.replace(s7_target, s7_replace)

# Slide 8: print_terminal_config.png
s8_target = """                <div class="print-placeholder">
                    <!-- ADICIONAR PRINT DO TERMINAL AQUI -->
                    <svg class="icon-med" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M6.827 6.175A2.31 2.31 0 015.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 00-1.134-.175 2.31 2.31 0 01-1.64-1.055l-.822-1.316a2.192 2.192 0 00-1.736-1.039 48.774 48.774 0 00-5.232 0 2.192 2.192 0 00-1.736 1.039l-.821 1.316z" /><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 12.75a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z" /></svg>
                    <p>[ COLAR O PRINT DO SEU TERMINAL AQUI ]</p>
                    <p style="font-size: 0.7em; font-weight: normal; margin-top: 10px;">Mostrar o assistente de configuração perguntando Provedor, Modelo e API Key.</p>
                </div>"""
s8_replace = """                <img src="print_terminal_config.png" alt="Hermes Configure Terminal" style="border-radius: 10px; max-width: 800px; margin-top: 20px; box-shadow: 0 10px 30px rgba(249, 212, 35, 0.3);">"""
content = content.replace(s8_target, s8_replace)

# Slide 9: print_vscode_env.png
s9_target = """                <div class="print-placeholder">
                    <!-- ADICIONAR PRINT DO VS CODE AQUI -->
                    <svg class="icon-med" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M14.25 9.75L16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0020.25 18V6A2.25 2.25 0 0018 3.75H6A2.25 2.25 0 003.75 6v12A2.25 2.25 0 006 20.25z" /></svg>
                    <p>[ COLAR O PRINT DO VS CODE AQUI ]</p>
                    <p style="font-size: 0.7em; font-weight: normal; margin-top: 10px;">Mostrar a tela do VS Code com o arquivo .env aberto contendo a linha: OPENROUTER_API_KEY=sk-or-...</p>
                </div>"""
s9_replace = """                <img src="print_vscode_env.png" alt="VS Code Env" style="border-radius: 10px; max-width: 850px; margin-top: 20px; box-shadow: 0 10px 30px rgba(157, 78, 221, 0.3);">"""
content = content.replace(s9_target, s9_replace)

# Slide 10: print_terminal_start.png
s10_target = """                <div class="print-placeholder" style="margin-bottom: 20px; min-height: 200px; padding: 40px 20px;">
                    <!-- ADICIONAR PRINT DO TERMINAL RODANDO AQUI -->
                    <svg class="icon-med" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15.91 11.672a.375.375 0 010 .656l-5.603 3.113a.375.375 0 01-.557-.328V8.887c0-.286.307-.466.557-.327l5.603 3.112z" /></svg>
                    <p>[ COLAR O PRINT DO HERMES START AQUI ]</p>
                    <p style="font-size: 0.7em; font-weight: normal; margin-top: 10px;">Mostrar os logs de "Gateway Online" e "Conexão com OpenRouter OK".</p>
                </div>"""
s10_replace = """                <img src="print_terminal_start.png" alt="Hermes Start" style="border-radius: 10px; max-width: 800px; margin-bottom: 20px; margin-top: 20px; box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);">"""
content = content.replace(s10_target, s10_replace)

# Slide 11: Bonus (print_terminal_chat.png)
bonus_slide = """
            <!-- Slide 11: Bônus - Interação Real -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>O Hermes na <span class="accent-gradient">Prática</span></h2>
                <p>Interagindo diretamente com o agente no terminal:</p>
                
                <img src="print_terminal_chat.png" alt="Hermes Chat" style="border-radius: 10px; max-width: 850px; margin-top: 20px; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">
                
                <aside class="notes">
                    Para fechar com chave de ouro: aqui está o nosso agente rodando e respondendo ativamente. Quando eu pergunto 'Quem é você e qual a sua função?', ele responde perfeitamente, assumindo o papel que configuramos no System Prompt dele.
                </aside>
            </section>
"""

content = content.replace('                <div class="slide-source">Fonte: Documentação Oficial do Hermes</div>\n            </section>', '                <div class="slide-source">Fonte: Documentação Oficial do Hermes</div>\n            </section>\n' + bonus_slide)

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)
