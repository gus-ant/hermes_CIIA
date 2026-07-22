import re

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Slide 5: Instalação Facilitada (Antigravity)
s5_old = """            <!-- Slide 5: Instalação com Antigravity -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>O Primeiro Passo: <span class="accent-blue">Instalação Facilitada</span></h2>
                
                <div class="glass-box">
                    <p style="margin-bottom: 20px;">Deixe o <strong>Antigravity 2.0</strong> instalar o Hermes para você com um simples pedido:</p>
                    
                    <div class="code-block" style="border-color: var(--neon-blue); color: #fff;">
                        "Instale o Hermes Agent no meu computador e configure o ambiente para mim."
                    </div>
                    
                    <img src="print_antigravity.png" alt="Antigravity trabalhando" style="border-radius: 10px; max-width: 800px; margin-top: 15px; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">
                    <p style="font-size: 0.9em; margin-top: 10px; color: #a5a5c5;">
                        (O Antigravity cria as pastas, baixa o orquestrador e valida a instalação de forma 100% autônoma, sem você digitar nenhum código complexo)
                    </p>
                </div>

                <aside class="notes">"""

s5_new = """            <!-- Slide 5: Instalação com Antigravity -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>O Primeiro Passo: <span class="accent-blue">Instalação Facilitada</span></h2>
                
                <div style="display: flex; gap: 30px; align-items: center; justify-content: center; width: 100%; max-width: 1050px; margin: 20px auto 0 auto;">
                    <div style="flex: 1; text-align: left;">
                        <div class="glass-box" style="padding: 25px; text-align: left;">
                            <p style="margin-bottom: 15px; color: #fff; font-size: 1.05em;">Deixe o <strong>Antigravity 2.0</strong> instalar o Hermes para você com um simples pedido:</p>
                            
                            <div class="code-block" style="border-color: var(--neon-blue); color: #fff; font-size: 0.85em; padding: 12px 15px; margin: 15px 0;">
                                "Instale o Hermes Agent no meu computador e configure o ambiente para mim."
                            </div>
                            
                            <p style="font-size: 0.85em; margin-top: 15px; color: #a5a5c5; line-height: 1.5;">
                                (O Antigravity cria as pastas, baixa o orquestrador e valida a instalação de forma 100% autônoma, sem você digitar nenhum código complexo)
                            </p>
                        </div>
                    </div>
                    <div style="flex: 1.2; text-align: center;">
                        <img src="print_antigravity.png" alt="Antigravity trabalhando" style="border-radius: 10px; max-height: 440px; max-width: 100%; object-fit: contain; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3); display: block; margin: 0 auto;">
                    </div>
                </div>

                <aside class="notes">"""

content = content.replace(s5_old, s5_new)

# Slide 7: API Key Parte 1 (OpenRouter)
s7_old = """            <!-- Slide 7: API Key Parte 1 (Site) -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>Passo 1: A Chave no <span class="accent-pink">OpenRouter</span></h2>
                
                <div class="glass-box" style="border-top: 5px solid var(--neon-pink);">
                    <p style="font-size: 1.2em; font-weight: 600; margin-bottom: 20px;">A Alma do Seu Agente</p>
                    <p style="margin-bottom: 30px;">A chave de API é o "passaporte" que conecta o seu Hermes aos super cérebros como ChatGPT, Llama 3 ou Claude.</p>
                    
                    <ol style="text-align: left; display: inline-block; font-size: 1.1em; color: #ddd; line-height: 1.8;">
                        <li>Acesse o site <strong class="accent-pink">openrouter.ai</strong></li>
                        <li>Crie uma conta gratuita</li>
                        <li>Vá em <strong>"Keys"</strong> e clique em <em>Create Key</em></li>
                        <li>Copie o código gigante (ex: <code>sk-or-v1-xxxx...</code>)</li>
                    </ol>
                    <img src="print_openrouter.png" alt="OpenRouter API Key" style="border-radius: 12px; max-width: 650px; display: block; margin: 15px auto 0 auto; box-shadow: 0 10px 30px rgba(255, 0, 127, 0.3);">
                </div>

                <aside class="notes">"""

s7_new = """            <!-- Slide 7: API Key Parte 1 (Site) -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>Passo 1: A Chave no <span class="accent-pink">OpenRouter</span></h2>
                
                <div style="display: flex; gap: 30px; align-items: center; justify-content: center; width: 100%; max-width: 1050px; margin: 20px auto 0 auto;">
                    <div style="flex: 1; text-align: left;">
                        <div class="glass-box" style="border-top: 5px solid var(--neon-pink); padding: 25px; text-align: left;">
                            <p style="font-size: 1.1em; font-weight: 600; margin-bottom: 12px; color: #fff;">A Alma do Seu Agente</p>
                            <p style="margin-bottom: 20px; font-size: 0.95em;">A chave de API é o "passaporte" que conecta o Hermes aos super cérebros como ChatGPT, Llama 3 ou Claude.</p>
                            
                            <ol style="font-size: 0.95em; color: #ddd; line-height: 1.7; padding-left: 20px; margin: 0;">
                                <li style="margin-bottom: 8px;">Acesse o site <strong class="accent-pink">openrouter.ai</strong></li>
                                <li style="margin-bottom: 8px;">Crie uma conta gratuita</li>
                                <li style="margin-bottom: 8px;">Vá em <strong>"Keys"</strong> e clique em <em>Create Key</em></li>
                                <li style="margin-bottom: 0;">Copie o código gerado (ex: <code>sk-or-v1-xxxx...</code>)</li>
                            </ol>
                        </div>
                    </div>
                    <div style="flex: 1.1; text-align: center;">
                        <img src="print_openrouter.png" alt="OpenRouter API Key" style="border-radius: 12px; max-height: 440px; max-width: 100%; object-fit: contain; display: block; margin: 0 auto; box-shadow: 0 10px 30px rgba(255, 0, 127, 0.3);">
                    </div>
                </div>

                <aside class="notes">"""

content = content.replace(s7_old, s7_new)

# Slide 8: Terminal Config
s8_old = """            <!-- Slide 8: O Terminal em Ação (Print 1) -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Passo 2: Configurando no <span class="accent-yellow">Terminal</span></h2>
                <p>Nesta etapa, rodamos <code style="color:var(--neon-yellow);">hermes configure</code> e respondemos o passo a passo.</p>
                
                <img src="print_terminal_config.png" alt="Hermes Configure Terminal" style="border-radius: 10px; max-width: 800px; margin-top: 20px; box-shadow: 0 10px 30px rgba(249, 212, 35, 0.3);">

                <aside class="notes">"""

s8_new = """            <!-- Slide 8: O Terminal em Ação (Print 1) -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Passo 2: Configurando no <span class="accent-yellow">Terminal</span></h2>
                
                <div style="display: flex; gap: 30px; align-items: center; justify-content: center; width: 100%; max-width: 1050px; margin: 20px auto 0 auto;">
                    <div style="flex: 1; text-align: left;">
                        <div class="glass-box" style="border-left: 5px solid var(--neon-yellow); padding: 25px; text-align: left;">
                            <p style="font-size: 1.1em; font-weight: 600; color: #fff; margin-bottom: 15px;">Assistente de Configuração</p>
                            <p style="margin-bottom: 15px; font-size: 0.95em;">No terminal, digite o comando de setup guiado:</p>
                            <div class="code-block" style="border-color: var(--neon-yellow); color: var(--neon-yellow); font-size: 0.9em; padding: 10px 15px; margin: 10px 0;">
                                hermes configure
                            </div>
                            <ul style="font-size: 0.9em; color: #ccc; line-height: 1.6; padding-left: 20px; margin-top: 15px;">
                                <li style="margin-bottom: 8px;"><strong>Provider:</strong> Escolha <em>OpenRouter</em></li>
                                <li style="margin-bottom: 8px;"><strong>Model:</strong> Escolha <em>claude-3.5-sonnet</em></li>
                                <li style="margin-bottom: 0;"><strong>API Key:</strong> Cole sua chave copiada</li>
                            </ul>
                        </div>
                    </div>
                    <div style="flex: 1.2; text-align: center;">
                        <img src="print_terminal_config.png" alt="Hermes Configure Terminal" style="border-radius: 10px; max-height: 440px; max-width: 100%; object-fit: contain; display: block; margin: 0 auto; box-shadow: 0 10px 30px rgba(249, 212, 35, 0.3);">
                    </div>
                </div>

                <aside class="notes">"""

content = content.replace(s8_old, s8_new)

# Slide 9: VS Code Env
s9_old = """            <!-- Slide 9: Editando o Arquivo (Print 2) -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>Passo 3: Colando a Chave no <span class="accent-purple">VS Code</span></h2>
                <p>Abra o arquivo secreto <code>.env</code> no VS Code para validar a configuração.</p>
                
                <img src="print_vscode_env.png" alt="VS Code Env" style="border-radius: 10px; max-width: 850px; margin-top: 20px; box-shadow: 0 10px 30px rgba(157, 78, 221, 0.3);">

                <aside class="notes">"""

s9_new = """            <!-- Slide 9: Editando o Arquivo (Print 2) -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>Passo 3: Colando a Chave no <span class="accent-purple">VS Code</span></h2>
                
                <div style="display: flex; gap: 30px; align-items: center; justify-content: center; width: 100%; max-width: 1050px; margin: 20px auto 0 auto;">
                    <div style="flex: 1; text-align: left;">
                        <div class="glass-box" style="border-left: 5px solid var(--neon-purple); padding: 25px; text-align: left;">
                            <p style="font-size: 1.1em; font-weight: 600; color: #fff; margin-bottom: 12px;">Validando no VS Code</p>
                            <p style="margin-bottom: 15px; font-size: 0.95em;">Caso prefira conferir manualmente, abra a pasta do projeto no VS Code e acesse o arquivo <code>.env</code>.</p>
                            <ul style="font-size: 0.9em; color: #ccc; line-height: 1.6; padding-left: 20px; margin: 0;">
                                <li style="margin-bottom: 8px;">Confera se a chave está em <code>OPENROUTER_API_KEY</code>.</li>
                                <li style="margin-bottom: 8px;">Este arquivo é 100% local e seguro no seu computador.</li>
                                <li style="margin-bottom: 0;">O cérebro da IA estará fisicamente conectado!</li>
                            </ul>
                        </div>
                    </div>
                    <div style="flex: 1.2; text-align: center;">
                        <img src="print_vscode_env.png" alt="VS Code Env" style="border-radius: 10px; max-height: 440px; max-width: 100%; object-fit: contain; display: block; margin: 0 auto; box-shadow: 0 10px 30px rgba(157, 78, 221, 0.3);">
                    </div>
                </div>

                <aside class="notes">"""

content = content.replace(s9_old, s9_new)

# Slide 10: Hermes Start
s10_old = """            <!-- Slide 10: O Despertar (Print 3) -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Passo 4: O Despertar do <span class="accent-green">Hermes</span></h2>
                <p>Rodando o <code style="color:var(--neon-green);">hermes start</code> e dando vida ao Agente.</p>
                
                <img src="print_terminal_start.png" alt="Hermes Start" style="border-radius: 10px; max-width: 800px; margin-bottom: 20px; margin-top: 20px; box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);">
                
                <h3 class="accent-gradient" style="font-size: 2em; margin-top: 20px;">
                    "Vamos fazer uma pergunta para o nosso Hermes?"
                </h3>

                <aside class="notes">"""

s10_new = """            <!-- Slide 10: O Despertar (Print 3) -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Passo 4: O Despertar do <span class="accent-green">Hermes</span></h2>
                
                <div style="display: flex; gap: 30px; align-items: center; justify-content: center; width: 100%; max-width: 1050px; margin: 15px auto 0 auto;">
                    <div style="flex: 1; text-align: left;">
                        <div class="glass-box" style="border-left: 5px solid var(--neon-green); padding: 25px; text-align: left;">
                            <p style="font-size: 1.1em; font-weight: 600; color: #fff; margin-bottom: 12px;">Ligando o Agente</p>
                            <p style="margin-bottom: 15px; font-size: 0.95em;">No terminal, digite o comando para iniciar a execução:</p>
                            <div class="code-block" style="border-color: var(--neon-green); color: var(--neon-green); font-size: 0.9em; padding: 10px 15px; margin: 10px 0;">
                                hermes start
                            </div>
                            <p style="font-size: 0.88em; color: #a5a5c5; line-height: 1.5; margin-top: 15px;">
                                O Gateway conectará à API e carregará o banco de memória SQLite local.
                            </p>
                        </div>
                    </div>
                    <div style="flex: 1.2; text-align: center;">
                        <img src="print_terminal_start.png" alt="Hermes Start" style="border-radius: 10px; max-height: 400px; max-width: 100%; object-fit: contain; display: block; margin: 0 auto; box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);">
                    </div>
                </div>
                
                <h3 class="accent-gradient" style="font-size: 1.6em; margin-top: 20px;">
                    "Vamos fazer uma pergunta para o nosso Hermes?"
                </h3>

                <aside class="notes">"""

content = content.replace(s10_old, s10_new)

# Slide 11: Hermes Chat (Bonus)
s11_old = """            <!-- Slide 11: Bônus - Interação Real -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>O Hermes na <span class="accent-gradient">Prática</span></h2>
                <p>Interagindo diretamente com o agente no terminal:</p>
                
                <img src="print_terminal_chat.png" alt="Hermes Chat" style="border-radius: 10px; max-width: 850px; margin-top: 20px; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">
                
                <aside class="notes">"""

s11_new = """            <!-- Slide 11: Bônus - Interação Real -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>O Hermes na <span class="accent-gradient">Prática</span></h2>
                
                <div style="display: flex; gap: 30px; align-items: center; justify-content: center; width: 100%; max-width: 1050px; margin: 20px auto 0 auto;">
                    <div style="flex: 1; text-align: left;">
                        <div class="glass-box" style="border-left: 5px solid var(--neon-blue); padding: 25px; text-align: left;">
                            <p style="font-size: 1.1em; font-weight: 600; color: #fff; margin-bottom: 12px;">Interação Direta</p>
                            <p style="margin-bottom: 15px; font-size: 0.95em;">Envie um prompt direto pelo terminal para ver o raciocínio em tempo real:</p>
                            <div class="code-block" style="border-color: var(--neon-blue); color: #fff; font-size: 0.8em; padding: 10px 12px; margin: 10px 0;">
                                hermes chat "Olá Hermes! Quem é você?"
                            </div>
                            <p style="font-size: 0.88em; color: #a5a5c5; line-height: 1.5; margin-top: 15px;">
                                O agente responde assumindo seu papel e pronto para executar ordens no computador.
                            </p>
                        </div>
                    </div>
                    <div style="flex: 1.2; text-align: center;">
                        <img src="print_terminal_chat.png" alt="Hermes Chat" style="border-radius: 10px; max-height: 440px; max-width: 100%; object-fit: contain; display: block; margin: 0 auto; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">
                    </div>
                </div>
                
                <aside class="notes">"""

content = content.replace(s11_old, s11_new)

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Part 3 side-by-side formatting complete.")
