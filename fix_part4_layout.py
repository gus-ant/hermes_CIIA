import re

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update global glass-box CSS max-width and centering
content = content.replace('max-width: 1500px;', 'max-width: 950px;')

# Fix Slide 3
s3_old = """            <!-- Slide 3: Criando o Agente CRONOS -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Criando o <span class="accent-pink">Agente CRONOS</span></h2>
                <p>O jeito certo (e fácil): vamos usar o <strong>Antigravity</strong> para programar o nosso agente.</p>
                
                <div class="glass-box">
                    <p style="text-align: left; margin-bottom: 10px; color: var(--neon-pink); font-weight: bold;">Mande esse prompt no chat do Antigravity:</p>
                    <div class="code-block" style="border-color: var(--neon-pink); color: #fff; font-size: 0.9em;">
                        "Crie um agente chamado CRONOS focado em procurar notícias. Configure o ambiente dele para que ele consiga varrer sites de forma autônoma e me enviar os relatórios diários exclusivamente por e-mail."
                    </div>
                    <img src="print_cronos_antigravity.png" alt="Criando Agente Cronos" style="border-radius: 10px; max-width: 750px; margin-top: 15px; box-shadow: 0 10px 30px rgba(255, 0, 127, 0.3);">
                </div>

                <aside class="notes">"""

s3_new = """            <!-- Slide 3: Criando o Agente CRONOS -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Criando o <span class="accent-pink">Agente CRONOS</span></h2>
                <p style="margin-bottom: 10px;">O jeito certo (e fácil): vamos usar o <strong>Antigravity</strong> para programar o nosso agente.</p>
                
                <div class="glass-box" style="padding: 15px 25px;">
                    <p style="text-align: left; margin-bottom: 5px; color: var(--neon-pink); font-weight: bold; font-size: 0.9em;">Mande esse prompt no chat do Antigravity:</p>
                    <div class="code-block" style="border-color: var(--neon-pink); color: #fff; font-size: 0.85em; padding: 10px 15px; margin: 5px 0;">
                        "Crie um agente chamado CRONOS focado em procurar notícias. Configure o ambiente dele para que ele consiga varrer sites de forma autônoma e me enviar os relatórios diários exclusivamente por e-mail."
                    </div>
                    <img src="print_cronos_antigravity.png" alt="Criando Agente Cronos" style="border-radius: 10px; max-height: 250px; max-width: 100%; object-fit: contain; margin-top: 10px; box-shadow: 0 10px 30px rgba(255, 0, 127, 0.3);">
                </div>

                <aside class="notes">"""

content = content.replace(s3_old, s3_new)

# Fix Slide 5, 6, 7, 8 image heights
content = re.sub(
    r'<img src="print_cronos_vscode\.png"[^>]*>',
    '<img src="print_cronos_vscode.png" alt="VS Code Credenciais" style="border-radius: 10px; max-height: 420px; max-width: 100%; object-fit: contain; margin: 10px auto; display: block; box-shadow: 0 10px 30px rgba(157, 78, 221, 0.3);">',
    content
)

content = re.sub(
    r'<img src="print_cronos_trigger\.png"[^>]*>',
    '<img src="print_cronos_trigger.png" alt="Cron Trigger" style="border-radius: 10px; max-height: 420px; max-width: 100%; object-fit: contain; margin: 10px auto; display: block; box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);">',
    content
)

content = re.sub(
    r'<img src="print_cronos_email\.png"[^>]*>',
    '<img src="print_cronos_email.png" alt="E-mail na Caixa de Entrada" style="border-radius: 10px; max-height: 420px; max-width: 100%; object-fit: contain; margin: 10px auto; display: block; box-shadow: 0 15px 40px rgba(255, 0, 127, 0.4);">',
    content
)

content = re.sub(
    r'<img src="print_cronos_cron\.png"[^>]*>',
    '<img src="print_cronos_cron.png" alt="Agendamento Cron" style="border-radius: 10px; max-height: 420px; max-width: 100%; object-fit: contain; margin: 10px auto; display: block; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">',
    content
)

# Fix Slide 9
s9_old = """            <!-- Slide 9: Expandindo Horizontes -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Modificando o <span class="accent-blue">Cronos</span></h2>
                <p>O poder de criar múltiplos agentes especialistas.</p>
                
                <div class="glass-box" style="text-align: left; border-left: 5px solid var(--neon-blue);">
                    <p style="font-size: 1.1em; margin-bottom: 20px;">Você não está restrito a notícias gerais. É só alterar o <strong>prompt do comando</strong>:</p>
                    <ul style="line-height: 1.8;">
                        <li><strong>Política:</strong> <em>"Resuma os projetos de lei focados em impostos votados ontem."</em></li>
                        <li><strong>Mercado:</strong> <em>"Analise as manchetes de finanças e destaque a cotação das empresas X e Y."</em></li>
                        <li><strong>Empregos:</strong> <em>"Visite portais de vagas e me avise se surgiu algo para Analista de Marketing Sênior no Linkedin."</em></li>
                    </ul>
                    <p style="color: var(--neon-green); text-align: center; font-weight: bold; font-size: 1.1em; margin-top: 30px;">
                        Imagine ter 5 agentes diferentes, todos trabalhando em background.
                    </p>
                </div>

                <aside class="notes">"""

s9_new = """            <!-- Slide 9: Expandindo Horizontes -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Modificando o <span class="accent-blue">Cronos</span></h2>
                <p style="margin-bottom: 12px;">O poder de criar múltiplos agentes especialistas.</p>
                
                <div class="glass-box" style="text-align: left; border-left: 5px solid var(--neon-blue); padding: 20px 30px;">
                    <p style="font-size: 1.05em; margin-bottom: 12px; color: #fff;">Você não está restrito a notícias gerais. É só alterar o <strong>prompt do comando</strong>:</p>
                    <ul style="line-height: 1.5; margin-bottom: 15px;">
                        <li style="margin-bottom: 8px;"><strong>Política:</strong> <em>"Resuma os projetos de lei focados em impostos votados ontem."</em></li>
                        <li style="margin-bottom: 8px;"><strong>Mercado:</strong> <em>"Analise as manchetes de finanças e destaque a cotação das empresas X e Y."</em></li>
                        <li style="margin-bottom: 0;"><strong>Empregos:</strong> <em>"Visite portais de vagas e me avise se surgiu algo para Analista de Marketing Sênior no Linkedin."</em></li>
                    </ul>
                    <p style="color: var(--neon-green); text-align: center; font-weight: bold; font-size: 1.05em; margin-top: 15px; margin-bottom: 0;">
                        Imagine ter 5 agentes diferentes, todos trabalhando em background.
                    </p>
                </div>

                <aside class="notes">"""

content = content.replace(s9_old, s9_new)

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte4.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Slide 4 layout updated successfully.")
