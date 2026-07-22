import re

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Slide 3 (add bonus print)
s3_target = """                    <div class="code-block" style="border-color: var(--neon-pink); color: #fff;">
                        "Crie um agente chamado CRONOS focado em procurar notícias. Configure o ambiente dele para que ele consiga varrer sites de forma autônoma e me enviar os relatórios diários exclusivamente por e-mail."
                    </div>
                </div>"""
s3_replace = """                    <div class="code-block" style="border-color: var(--neon-pink); color: #fff; font-size: 0.9em;">
                        "Crie um agente chamado CRONOS focado em procurar notícias. Configure o ambiente dele para que ele consiga varrer sites de forma autônoma e me enviar os relatórios diários exclusivamente por e-mail."
                    </div>
                    <img src="print_cronos_antigravity.png" alt="Criando Agente Cronos" style="border-radius: 10px; max-width: 750px; margin-top: 15px; box-shadow: 0 10px 30px rgba(255, 0, 127, 0.3);">
                </div>"""
content = content.replace(s3_target, s3_replace)

# Replace Slide 5 (add print 1)
s5_target = """                <div class="print-placeholder">
                    <!-- ADICIONAR PRINT DO VS CODE AQUI -->
                    <svg class="icon-med" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M14.25 9.75L16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0020.25 18V6A2.25 2.25 0 0018 3.75H6A2.25 2.25 0 003.75 6v12A2.25 2.25 0 006 20.25z" /></svg>
                    <p>[ COLAR O PRINT DO VS CODE AQUI ]</p>
                    <p style="font-size: 0.7em; font-weight: normal; margin-top: 10px;">Mostrar o arquivo aberto com EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_SMTP_HOST, EMAIL_SMTP_PORT, EMAIL_HOME_ADDRESS</p>
                </div>"""
s5_replace = """                <img src="print_cronos_vscode.png" alt="VS Code Credenciais" style="border-radius: 10px; max-width: 850px; margin-top: 20px; box-shadow: 0 10px 30px rgba(157, 78, 221, 0.3);">"""
content = content.replace(s5_target, s5_replace)

# Replace Slide 6, 7, 8 entirely to match the new structure
new_slides_6_to_8 = """
            <!-- Slide 6: O Teste de Fogo (Print 2) -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>O <span class="accent-green">Teste de Fogo</span> (Disparo Manual)</h2>
                <p>Vamos mandar ele buscar e enviar um e-mail AGORA para ver se funciona!</p>
                
                <img src="print_cronos_trigger.png" alt="Cron Trigger" style="border-radius: 10px; max-width: 850px; margin-top: 15px; box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);">

                <aside class="notes">
                    Em vez de esperar o agente rodar sozinho, nós vamos testar ao vivo! Usando o comando 'cronos cron trigger', nós dizemos para ele: "Rode a sua tarefa agora". É a prova de que a conexão com o e-mail deu certo e que o robô está perfeitamente configurado e vivo.
                </aside>
            </section>

            <!-- Slide 7: O Resultado Tangível (Print 3) -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>O Resultado <span class="accent-pink">Tangível</span></h2>
                <p>O momento "Uau!" - O e-mail chegando na sua caixa de entrada.</p>
                
                <img src="print_cronos_email.png" alt="E-mail na Caixa de Entrada" style="border-radius: 10px; max-width: 900px; margin-top: 15px; box-shadow: 0 15px 40px rgba(255, 0, 127, 0.4);">

                <aside class="notes">
                    E aqui está! O resultado tangível. Vocês acabaram de receber um e-mail formatado, limpo, escrito 100% de forma autônoma pelo CRONOS. Ele pesquisou as notícias, usou o modelo da inteligência artificial para resumir as top 5 e entregou direto pra você.
                </aside>
            </section>

            <!-- Slide 8: Piloto Automático (Print 4) -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Colocando no <span class="accent-blue">Piloto Automático</span></h2>
                <p>Agendando para rodar sozinho todo dia às 08:00 com o Cron Job.</p>
                
                <img src="print_cronos_cron.png" alt="Agendamento Cron" style="border-radius: 10px; max-width: 850px; margin-top: 15px; box-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);">

                <aside class="notes">
                    Agora que vimos que funciona perfeitamente, vamos deixar o agente contratado. Usamos o comando cron create com "0 8 * * *", que significa rodar todo dia às 8 da manhã. A partir de amanhã, você não precisa fazer nada, o Cronos já estará trabalhando no plano de fundo.
                </aside>
            </section>
"""

# Find the start of Slide 6 and the end of Slide 8 in the original content
start_s6 = content.find("<!-- Slide 6: Agendando a Rotina -->")
end_s8 = content.find("<!-- Slide 9: Expandindo Horizontes -->")

if start_s6 != -1 and end_s8 != -1:
    content = content[:start_s6] + new_slides_6_to_8.strip() + "\n\n            " + content[end_s8:]

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte4.html', 'w', encoding='utf-8') as f:
    f.write(content)

