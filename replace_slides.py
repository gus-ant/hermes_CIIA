import re

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_gerais.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slides = """            <!-- Slide 1: Capa & Boas-vindas -->
            <section data-transition="zoom" data-background-color="#000000">
                <div
                    style="position: relative; height: 40px; display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
                    <!-- Floating digital tools -->
                    <svg class="icon-med accent-blue float-fast" style="position: absolute; left: 20%;"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                        <path d="M3 3v18h18M18 9l-5 5-4-4-5 5" />
                    </svg>
                    <svg class="icon-med accent-green float-slow" style="position: absolute; right: 20%;"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                        <path
                            d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
                    </svg>
                    <!-- Center user -->
                    <svg class="icon-large accent-purple" style="z-index: 10;" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="1.5">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
                    </svg>
                </div>

                <h1 style="font-size: 3em; margin-bottom: 20px;">Introdução aos <span class="accent-gradient">Agentes de IA</span></h1>
                <p style="font-size: 1.2em; color: #d1d1e9;">Como construir sua equipe de assistentes virtuais em linguagem natural.</p>

                <aside class="notes">
                    Olá a todos! Sejam muito bem-vindos. Hoje nós não vamos falar sobre programação complexa ou teoria acadêmica de IA. Vamos falar sobre como criar uma equipe de assistentes virtuais altamente qualificados — os chamados Agentes — para assumirem o trabalho braçal e repetitivo do seu dia a dia, usando apenas o bom e velho português.
                </aside>
            </section>

            <!-- Slide 2: O Problema -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>O Dia Só Tem 24 Horas <span class="accent-pink">(E Falta Tempo)</span></h2>

                <div class="glass-box">
                    <ul style="font-size: 1.1em; line-height: 1.8; text-align: left; color: #fff; padding-left: 20px;">
                        <li><span class="accent-pink" style="font-weight: bold;">80% do dia</span> gasto com e-mails, pesquisas e cópia de dados.</li>
                        <li><span class="accent-pink" style="font-weight: bold;">Cansaço mental</span> e falta de tempo para decisões estratégicas.</li>
                    </ul>
                </div>

                <aside class="notes">
                    Quem nunca terminou o dia com a sensação de ter trabalhado duro, mas só apagou incêndios ou respondeu e-mails repetitivos? Gastamos nossa energia intelectual com processos operacionais. A pergunta central de hoje é: e se você pudesse delegar 100% disso para assistentes digitais?
                </aside>
            </section>

            <!-- Slide 3: ChatGPT vs. Agente -->
            <section data-transition="convex" data-background-color="#000000">
                <h2><span class="accent-pink">O Estagiário Reativo</span> vs. <span class="accent-green">O Funcionário Sênior</span></h2>

                <div class="flex-container">
                    <div class="flex-item" style="border-color: rgba(255, 0, 127, 0.3);">
                        <svg class="icon-large accent-pink" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 9.75a.625.625 0 11-1.25 0 .625.625 0 011.25 0zm0 0H8.25m4.125 0a.625.625 0 11-1.25 0 .625.625 0 011.25 0zm0 0H12m4.125 0a.625.625 0 11-1.25 0 .625.625 0 011.25 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
                        </svg>
                        <h3 class="accent-pink">ChatGPT Comum (Reativo)</h3>
                        <p>Espera comandos diretos a cada etapa; só responde quando provocado.</p>
                    </div>

                    <div class="flex-item" style="border-color: rgba(0, 255, 204, 0.3);">
                        <svg class="icon-large accent-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c.253.962.584 1.892.985 2.783.247.55.06 1.21-.463 1.511l-.657.38c-.551.318-1.26.117-1.527-.461a20.845 20.845 0 01-1.44-4.282m3.102.069a18.03 18.03 0 01-.59-4.59c0-1.586.205-3.124.59-4.59m0 9.18a23.848 23.848 0 018.835 2.535M10.34 6.66a23.847 23.847 0 008.835-2.535m0 0A23.74 23.74 0 0018.795 3m.38 1.125a23.91 23.91 0 011.014 5.395m-1.014 8.855c-.118.38-.245.754-.38 1.125m.38-1.125a23.91 23.91 0 001.014-5.395m0-3.46c.495.413.811 1.035.811 1.73 0 .695-.316 1.317-.811 1.73m0-3.46a24.347 24.347 0 010 3.46" />
                        </svg>
                        <h3 class="accent-green">Agente Virtual (Proativo)</h3>
                        <p>Recebe um objetivo final, planeja a execução, usa ferramentas e entrega o resultado pronto.</p>
                    </div>
                </div>

                <aside class="notes">
                    Um chatbot tradicional é como um estagiário brilhante, mas que exige que você segure a mão dele em cada clique. O Agente de IA é o seu funcionário sênior: você dá a missão final — como 'Analise o mercado e envie o resumo diário' —, ele planeja os passos, executa e só volta quando o trabalho estiver concluído.
                </aside>
            </section>

            <!-- Slide 4: Bagunça vs. Organização -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>A <span class="accent-pink">Bagunça do Chatbot</span> vs. A <span class="accent-green">Precisão do Agente</span></h2>

                <div class="flex-container">
                    <div class="flex-item" style="border-color: rgba(255, 0, 127, 0.3); text-align: left; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <h3 class="accent-pink" style="font-size: 1.2em;">Bagunça</h3>
                            <p style="font-size: 0.85em; margin-bottom: 15px;">Um único chat misturando receitas, planilhas e e-mails sem foco.</p>
                        </div>
                    </div>

                    <div class="flex-item" style="border-color: rgba(0, 255, 204, 0.3); text-align: left; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <h3 class="accent-green" style="font-size: 1.2em;">Organização</h3>
                            <p style="font-size: 0.85em; margin-bottom: 15px;">Uma missão isolada, com escopo fechado, ferramentas dedicadas e entrega padronizada.</p>
                        </div>
                    </div>
                </div>

                <aside class="notes">
                    A maioria das pessoas falha com IA porque tenta usar a janela do ChatGPT para tudo ao mesmo tempo. O agente trabalha com escopo fechado: uma missão, as ferramentas certas e uma regra clara de sucesso.
                </aside>
            </section>

            <!-- Slide 5: A Tríade da Mente do Agente -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Como Pensa um <span class="accent-blue">Agente Virtual?</span></h2>

                <div class="flex-container">
                    <div class="flex-item" style="border-color: rgba(249, 212, 35, 0.3);">
                        <svg class="icon-large accent-yellow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 002.25-2.25V6.75A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25v10.5A2.25 2.25 0 004.5 19.5zm6-10.125a1.875 1.875 0 11-3.75 0 1.875 1.875 0 013.75 0zm1.294 6.336a6.721 6.721 0 01-3.17.789 6.721 6.721 0 01-3.168-.789 3.376 3.376 0 016.338 0z" />
                        </svg>
                        <h3 class="accent-yellow" style="font-size: 1.5em;">Identidade</h3>
                        <p style="font-size: 0.85em;">Quem ele é e qual o seu papel profissional.</p>
                    </div>
                    <div class="flex-item" style="border-color: rgba(0, 210, 255, 0.3);">
                        <svg class="icon-large accent-blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 14.15v4.25c0 1.094-.787 2.036-1.872 2.18-2.087.277-4.216.42-6.378.42s-4.291-.143-6.378-.42c-1.085-.144-1.872-1.086-1.872-2.18v-4.25m16.5 0a2.18 2.18 0 00.75-1.661V8.706c0-1.081-.768-2.015-1.837-2.175a48.114 48.114 0 00-3.413-.387m4.5 8.006c-.194.165-.42.295-.673.38A23.978 23.978 0 0112 15.75c-2.648 0-5.195-.429-7.577-1.22a2.016 2.016 0 01-.673-.38m0 0A2.18 2.18 0 013 12.489V8.706c0-1.081.768-2.015 1.837-2.175a48.111 48.111 0 013.413-.387m7.5 0V5.25A2.25 2.25 0 0013.5 3h-3a2.25 2.25 0 00-2.25 2.25v.894m7.5 0a48.667 48.667 0 00-7.5 0M12 12.75h.008v.008H12v-.008z" />
                        </svg>
                        <h3 class="accent-blue" style="font-size: 1.5em;">Ferramentas</h3>
                        <p style="font-size: 0.85em;">O que ele pode usar (navegador, e-mail, arquivos).</p>
                    </div>
                    <div class="flex-item" style="border-color: rgba(0, 255, 204, 0.3);">
                        <svg class="icon-large accent-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.042 21.672L13.684 16.6m0 0l-2.51 2.225.569-9.47 5.227 7.917-3.286-.672zM12 2.25V4.5m5.834.166l-1.591 1.591M20.25 10.5H18M7.757 14.743l-1.59 1.59M6 10.5H3.75m4.007-4.243l-1.59-1.59" />
                        </svg>
                        <h3 class="accent-green" style="font-size: 1.5em;">Objetivo</h3>
                        <p style="font-size: 0.85em;">Qual o resultado final esperado.</p>
                    </div>
                </div>

                <aside class="notes">
                    Para estruturar qualquer agente, dividimos a mente dele em 3 partes: quem ele é (Identidade), quais 'mãos' ele usa (Ferramentas) e qual a linha de chegada (Objetivo).
                </aside>
            </section>

            <!-- Slide 6: A Alma do Agente -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>A Alma do Agente: <span class="accent-blue">O System Prompt</span></h2>

                <div class="glass-box" style="padding: 30px; text-align: left;">
                    <ul style="font-size: 1.1em; line-height: 1.8; color: #fff; padding-left: 20px;">
                        <li><span class="accent-blue" style="font-weight: bold;">Definição do papel:</span> (ex: Analista de Comunicação).</li>
                        <li><span class="accent-blue" style="font-weight: bold;">A Regra de Ouro:</span> Definir o que ele NÃO deve fazer é mais importante do que dizer o que fazer (evita alucinações e economiza custos).</li>
                    </ul>
                </div>

                <aside class="notes">
                    O System Prompt é o contrato de trabalho do agente. É aqui que definimos o tom e as fronteiras. Dizer 'não resuma conteúdos patrocinados' evita que o agente perca tempo ou traga dados inúteis.
                </aside>
            </section>

            <!-- Slide 7: O Ecossistema Hermes -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>O Ecossistema Hermes: <span class="accent-gradient">Conectando a IA ao Mundo</span></h2>

                <div class="glass-box" style="padding: 30px; text-align: left;">
                    <ul style="font-size: 1.1em; line-height: 1.8; color: #fff; padding-left: 20px;">
                        <li><span class="accent-purple" style="font-weight: bold;">Orquestrador (Hermes):</span> O maestro que coordena a execução.</li>
                        <li><span class="accent-blue" style="font-weight: bold;">Modelo (LLM):</span> O cérebro conversacional.</li>
                        <li><span class="accent-green" style="font-weight: bold;">Ferramentas:</span> Web Search (olhos) + E-mail/APIs (mãos).</li>
                    </ul>
                </div>

                <aside class="notes">
                    O modelo de linguagem sozinho é um cérebro sem corpo. O Hermes atua como o orquestrador que entrega mãos (ferramentas de e-mail) e olhos (busca web) para que a IA interaja com o mundo real.
                </aside>
            </section>

            <!-- Slide 8: Desmistificando a Sopa de Letrinhas -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Os Pré-requisitos Técnicos em <span class="accent-blue">Linguagem Simples</span></h2>

                <div class="glass-box" style="padding: 30px; text-align: left;">
                    <ul style="font-size: 1.0em; line-height: 1.8; color: #fff; padding-left: 20px;">
                        <li><span class="accent-green" style="font-weight: bold;">API (Chave de Acesso):</span> A tomada/ponte digital que autoriza nosso agente a usar os cérebros de IA (OpenAI, Claude) e enviar e-mails.</li>
                        <li><span class="accent-blue" style="font-weight: bold;">IDE (Mesa de Trabalho):</span> O programa (ex: VS Code ou Antigravity) onde organizamos os arquivos e as instruções do nosso agente.</li>
                        <li><span class="accent-pink" style="font-weight: bold;">Terminal (Painel de Bordo):</span> A janela de comandos onde apertamos o "play" e vemos o raciocínio do agente rodar em tempo real.</li>
                    </ul>
                </div>

                <aside class="notes">
                    Antes de vermos isso rodando, vamos traduzir três termos que assustam muita gente. Uma API nada mais é do que uma chave/crachá digital que dá permissão para o agente usar um serviço. A IDE é a nossa oficina visual onde ficam os arquivos do projeto. E o Terminal é a tela de controle onde ligamos o agente e assistimos ele trabalhar. Não precisamos programar linhas de código complexas, apenas conectar essas pontes!
                </aside>
            </section>

            <!-- Slide 9: A Memória do Agente -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>Memória do Agente: <span class="accent-green">Do Temporário ao Contínuo</span></h2>

                <div class="flex-container">
                    <div class="flex-item" style="border-color: rgba(255, 0, 127, 0.3); text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
                        <h4 class="accent-pink" style="font-size: 1.2em; margin-bottom: 10px;">🧠 Memória Básica</h4>
                        <p style="font-size: 0.9em; line-height: 1.3; color: #aaa; margin: 0;">Esquece tudo ao fechar a janela.</p>
                    </div>
                    <div class="flex-item" style="border-color: rgba(0, 255, 204, 0.3); text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
                        <h4 class="accent-green" style="font-size: 1.2em; margin-bottom: 10px;">🔄 Memória Contínua</h4>
                        <p style="font-size: 0.9em; line-height: 1.3; color: #aaa; margin: 0;">Grava preferências, históricos e decisões em arquivos locais.</p>
                    </div>
                </div>

                <aside class="notes">
                    Agentes de alto nível não esquecem o trabalho feito ontem. O Hermes salva históricos em arquivos locais, garantindo que o agente aprenda seu estilo e não repita buscas desnecessárias.
                </aside>
            </section>

            <!-- Slide 10: Exemplo Prático 1 -->
            <section data-transition="convex" data-background-color="#000000">
                <h2>Caso Prático: <span class="accent-green">Monitor de Mercado 24/7</span></h2>

                <div class="glass-box" style="padding: 30px; text-align: center;">
                    <p style="font-size: 1.2em; font-weight: bold; color: var(--neon-green); margin-bottom: 20px;">O Fluxo:</p>
                    <p style="font-size: 1.1em; color: #fff; line-height: 1.8;">
                        Acorda às 6h da manhã <span class="scheme-arrow">→</span> 
                        Varre portais do setor <span class="scheme-arrow">→</span> 
                        Filtra ruídos <span class="scheme-arrow">→</span> 
                        Entrega um dossiê no e-mail ou celular.
                    </p>
                </div>

                <aside class="notes">
                    Agora que entendemos os pilares e as ferramentas, vejam isso na prática. Um agente de monitoramento acorda antes de você, lê as notícias da sua área, descarta anúncios e deixa os 3 pontos mais relevantes no seu e-mail antes do café.
                </aside>
            </section>

            <!-- Slide 11: Exemplo Prático 2 -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2>Caso Prático: <span class="accent-pink">Organizador Autônomo de Arquivos</span></h2>

                <div class="glass-box" style="padding: 30px; text-align: center;">
                    <p style="font-size: 1.2em; font-weight: bold; color: var(--neon-pink); margin-bottom: 20px;">O Fluxo:</p>
                    <p style="font-size: 1.1em; color: #fff; line-height: 1.8;">
                        Arquivo salvo na pasta de Downloads <span class="scheme-arrow">→</span> 
                        Agente analisa o PDF/imagem <span class="scheme-arrow">→</span> 
                        Renomeia no padrão e move para a pasta correta.
                    </p>
                </div>

                <aside class="notes">
                    Outro uso real: uma pasta inteligente que analisa recibos ou relatórios baixados, identifica o cliente e move o documento para a pasta correta no Drive sem você mover um dedo.
                </aside>
            </section>

            <!-- Slide 12: Conclusão -->
            <section data-transition="zoom" data-background-color="#000000">
                <h2 style="font-size: 2.3em; margin-bottom: 20px;">O Futuro Pertence a Quem Sabe <span class="accent-gradient">Delegar</span></h2>

                <div class="glass-box" style="padding: 30px; text-align: left; max-width: 900px; margin: 0 auto;">
                    <ul style="font-size: 1.1em; line-height: 1.8; color: #fff; padding-left: 20px;">
                        <li><span class="accent-green" style="font-weight: bold;">Recuperação</span> de tempo livre.</li>
                        <li><span class="accent-blue" style="font-weight: bold;">Foco</span> na estratégia e relacionamento humano.</li>
                        <li><span class="accent-purple" style="font-weight: bold;">Criação</span> de sistemas incansáveis.</li>
                    </ul>
                </div>

                <aside class="notes">
                    Com os conceitos e termos consolidados, na Parte 2 nós vamos abrir o capô e desenhar a arquitetura completa do nosso primeiro agente autônomo real: o AGENTE CRONOS.
                </aside>
            </section>"""

# Using regex to replace everything between <div class="slides"> and </div>
# The div starts at line 260: <div class="slides">
pattern = re.compile(r'(<div class="slides">\n).*?(\n\s*</div>\n\s*</div>\n\s*<!-- Reveal\.js JS -->)', re.DOTALL)
new_content = pattern.sub(r'\g<1>' + new_slides + r'\g<2>', content)

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_gerais.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
