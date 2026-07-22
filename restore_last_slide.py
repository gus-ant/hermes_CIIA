with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'r', encoding='utf-8') as f:
    content = f.read()

slide_code = """
            <!-- Slide: Conclusão da Parte 3 / Ponte para a Parte 4 -->
            <section data-transition="zoom" data-background-color="#000000">
                <div style="margin-bottom: 15px;">
                    <span class="badge"
                        style="background: rgba(52, 211, 153, 0.1); border: 1px solid rgba(52, 211, 153, 0.3); color: #34d399; padding: 6px 16px; border-radius: 20px; font-size: 0.8em; font-weight: bold; text-transform: uppercase;">
                        Conquista Desbloqueada 🚀
                    </span>
                </div>

                <h1 style="font-size: 2.5em; line-height: 1.1; margin-bottom: 15px;">
                    O Cérebro do Hermes <br><span class="accent-gradient">Já Está Vivo!</span>
                </h1>

                <div class="glass-box"
                    style="padding: 20px 30px; text-align: left; max-width: 1250px; width: 100%; margin: 0 auto; border-left: 5px solid var(--neon-green);">
                    <p style="font-size: 1.0em; color: #fff; font-weight: bold; margin-bottom: 12px;">
                        O que você conquistou nesta etapa:
                    </p>

                    <div
                        style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 0.9em; color: #d1d1e9; margin-bottom: 15px;">
                        <div
                            style="background: rgba(255,255,255,0.03); padding: 12px 18px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                            ✅ <strong>Ambiente Configurado:</strong> VS Code e Antigravity prontos no seu computador.
                        </div>
                        <div
                            style="background: rgba(255,255,255,0.03); padding: 12px 18px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                            ✅ <strong>Conexão Segura:</strong> Chave de API ativada no OpenRouter e guardada no arquivo <code>.env</code>.
                        </div>
                        <div
                            style="background: rgba(255,255,255,0.03); padding: 12px 18px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                            ✅ <strong>Barreira Vencida:</strong> Perdeu o medo do Terminal e executou comandos reais.
                        </div>
                        <div
                            style="background: rgba(255,255,255,0.03); padding: 12px 18px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                            ✅ <strong>Motor Rodando:</strong> O Hermes Gateway está ativado e respondendo localmente.
                        </div>
                    </div>

                    <div
                        style="background: rgba(157, 78, 221, 0.15); border: 1px solid rgba(157, 78, 221, 0.4); border-radius: 10px; padding: 12px 20px; text-align: center;">
                        <p style="margin: 0; font-weight: bold; font-size: 0.95em; color: var(--neon-purple);">
                            🔥 Próximo Passo (Parte 4):
                        </p>
                        <p style="margin: 3px 0 0 0; font-size: 0.88em; color: #fff; line-height: 1.3;">
                            Conectar braços ao cérebro: Vamos integrar ferramentas de busca web e e-mail SMTP para transformar o Hermes no <strong>Agente CRONOS</strong> em piloto automático!
                        </p>
                    </div>
                </div>

                <aside class="notes">
                    Parabéns a todos! Olhem o que nós acabamos de fazer: vencemos o medo da tela preta, configuramos o VS Code, conectamos nossa chave de API no OpenRouter e colocamos o motor do Hermes para rodar direto no computador de vocês.
                </aside>
            </section>
"""

content = content.replace('    <!-- Reveal.js JS -->', slide_code + '\n        </div>\n    </div>\n\n    <!-- Reveal.js JS -->')

with open('/Users/gustavo/Documents/hermes_CIIA/apresentacao_agentes_parte3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored conclusion slide with wide layout.")
