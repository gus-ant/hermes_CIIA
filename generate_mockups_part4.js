const puppeteer = require('puppeteer');

const mockups = [
    {
        name: 'print_cronos_antigravity.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #1e1e1e; color: #fff; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .window { width: 850px; background-color: #252526; border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.5); border: 1px solid #333; }
                .header { background-color: #333333; padding: 10px; text-align: center; font-size: 14px; font-weight: bold; color: #ccc; border-bottom: 1px solid #1e1e1e; display: flex; justify-content: space-between; align-items: center;}
                .dots { display: flex; gap: 8px; margin-left: 10px; }
                .dot { width: 12px; height: 12px; border-radius: 50%; }
                .dot.red { background-color: #ff5f56; }
                .dot.yellow { background-color: #ffbd2e; }
                .dot.green { background-color: #27c93f; }
                .content { padding: 20px; font-family: "JetBrains Mono", "Fira Code", Consolas, monospace; font-size: 16px; line-height: 1.6; }
                .user-msg { background-color: #2b2d31; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #ff007f; }
                .ai-msg { padding: 15px; }
                .log-line { color: #888; font-size: 15px; margin: 5px 0; }
                .log-line span.success { color: #27c93f; font-weight: bold;}
                .log-line span.action { color: #00d2ff; }
            </style>
        </head>
        <body>
            <div class="window">
                <div class="header">
                    <div class="dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
                    <div>Antigravity 2.0 - Workspace</div>
                    <div style="width: 40px;"></div>
                </div>
                <div class="content">
                    <div class="user-msg">
                        <strong>User:</strong> Crie um agente chamado CRONOS focado em procurar notícias. Configure o ambiente dele para que ele consiga varrer sites de forma autônoma e me enviar os relatórios diários exclusivamente por e-mail.
                    </div>
                    <div class="ai-msg">
                        <div style="margin-bottom: 15px;"><strong>Antigravity:</strong> Criando estrutura isolada para o novo agente CRONOS...</div>
                        <div class="log-line">[<span class="success">✔</span>] Profile 'cronos' created at ~/.hermes/profiles/cronos/</div>
                        <div class="log-line">[<span class="success">✔</span>] Web search plugin enabled.</div>
                        <div class="log-line">[<span class="success">✔</span>] SMTP Mailer plugin configured.</div>
                        <div style="margin-top: 15px; color:#ccc;"><strong>Antigravity:</strong> O agente CRONOS foi criado. Para configurar as chaves de e-mail dele, abra o arquivo <code>.env</code> com o comando: <br><span style="color:#ff007f">code ~/.hermes/profiles/cronos/.env</span></div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        `
    },
    {
        name: 'print_cronos_vscode.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: #1e1e1e; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;}
                .vscode { width: 950px; height: 500px; background-color: #1e1e1e; border-radius: 8px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #333; display: flex; flex-direction: column; }
                .vs-header { height: 35px; background-color: #323233; display: flex; align-items: center; padding: 0 10px; border-bottom: 1px solid #2b2b2b;}
                .mac-dots { display: flex; gap: 8px; }
                .mac-dot { width: 12px; height: 12px; border-radius: 50%; }
                .mac-dot.red { background-color: #ff5f56; }
                .mac-dot.yellow { background-color: #ffbd2e; }
                .mac-dot.green { background-color: #27c93f; }
                .vs-title { flex-grow: 1; text-align: center; color: #ccc; font-size: 13px; }
                .vs-main { display: flex; flex-grow: 1; }
                .vs-sidebar { width: 220px; background-color: #252526; border-right: 1px solid #333; padding: 10px 0; }
                .vs-explorer-title { color: #bbb; font-size: 11px; text-transform: uppercase; padding: 0 20px 10px; letter-spacing: 1px; }
                .vs-file { padding: 5px 20px; color: #ccc; font-size: 13px; display: flex; align-items: center; gap: 8px; cursor: pointer; }
                .vs-file:hover { background-color: #2a2d2e; }
                .vs-file.active { background-color: #37373d; color: #fff; }
                .vs-editor { flex-grow: 1; background-color: #1e1e1e; display: flex; flex-direction: column; }
                .vs-tabs { display: flex; background-color: #252526; height: 35px; }
                .vs-tab { padding: 0 20px; background-color: #1e1e1e; color: #fff; border-top: 1px solid #007acc; display: flex; align-items: center; font-size: 13px; gap: 8px; }
                .vs-code { padding: 20px; font-family: "Consolas", "Courier New", monospace; font-size: 18px; line-height: 1.6; color: #d4d4d4; }
                .comment { color: #6a9955; }
                .variable { color: #4fc1ff; }
                .operator { color: #d4d4d4; }
                .string { color: #ce9178; }
                .line-number { color: #858585; display: inline-block; width: 30px; text-align: right; margin-right: 15px; user-select: none; }
                .blur-box { display: inline-block; width: 150px; height: 20px; background-color: #000; vertical-align: middle; margin-left: 5px;}
            </style>
        </head>
        <body>
            <div class="vscode">
                <div class="vs-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="vs-title">cronos - Visual Studio Code</div>
                </div>
                <div class="vs-main">
                    <div class="vs-sidebar">
                        <div class="vs-explorer-title">Explorer</div>
                        <div class="vs-file"><span>📁</span> memory</div>
                        <div class="vs-file"><span>📁</span> plugins</div>
                        <div class="vs-file active"><span>⚙️</span> .env</div>
                        <div class="vs-file"><span>📄</span> system_prompt.txt</div>
                    </div>
                    <div class="vs-editor">
                        <div class="vs-tabs">
                            <div class="vs-tab"><span>⚙️</span> .env</div>
                        </div>
                        <div class="vs-code">
                            <div><span class="line-number">1</span><span class="comment"># CRONOS EMAIL CONFIGURATION</span></div>
                            <div><span class="line-number">2</span><span class="variable">EMAIL_ADDRESS</span><span class="operator">=</span><span class="string">seu.email@gmail.com</span></div>
                            <div><span class="line-number">3</span><span class="variable">EMAIL_PASSWORD</span><span class="operator">=</span><span class="string">xxxx-xxxx-xxxx-xxxx</span></div>
                            <div><span class="line-number">4</span><span class="variable">EMAIL_SMTP_HOST</span><span class="operator">=</span><span class="string">smtp.gmail.com</span></div>
                            <div><span class="line-number">5</span><span class="variable">EMAIL_SMTP_PORT</span><span class="operator">=</span><span class="string">587</span></div>
                            <div><span class="line-number">6</span><span class="variable">EMAIL_HOME_ADDRESS</span><span class="operator">=</span><span class="string">seu.email@gmail.com</span></div>
                            <div><span class="line-number">7</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        `
    },
    {
        name: 'print_cronos_trigger.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: transparent; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .mac-terminal { width: 850px; background-color: rgba(30, 30, 30, 0.95); border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #444; backdrop-filter: blur(10px); }
                .mac-header { background-color: #323232; height: 28px; display: flex; align-items: center; padding: 0 10px; }
                .mac-dots { display: flex; gap: 8px; }
                .mac-dot { width: 12px; height: 12px; border-radius: 50%; }
                .mac-dot.red { background-color: #ff5f56; }
                .mac-dot.yellow { background-color: #ffbd2e; }
                .mac-dot.green { background-color: #27c93f; }
                .mac-title { flex-grow: 1; text-align: center; color: #999; font-family: -apple-system, sans-serif; font-size: 13px; font-weight: 500; margin-left: -40px; }
                .mac-body { padding: 15px 25px; font-family: "Menlo", "Monaco", "Courier New", monospace; font-size: 18px; line-height: 1.6; color: #fff; }
                .prompt { color: #00ffcc; }
                .command { color: #fff; }
                .info { color: #00d2ff; }
                .success { color: #27c93f; font-weight: bold;}
                .step { color: #f9d423; }
            </style>
        </head>
        <body>
            <div class="mac-terminal">
                <div class="mac-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="mac-title">gustavo@MacBook-Pro: ~/hermes-agent</div>
                </div>
                <div class="mac-body">
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command">cronos cron trigger "Newsletter do Cronos"</span></div>
                    <br>
                    <div><span class="info">[INFO]</span> Triggering task 'Newsletter do Cronos'...</div>
                    <div><span class="step">[STEP 1/3]</span> Searching web for daily news... <span class="success">Done.</span></div>
                    <div><span class="step">[STEP 2/3]</span> Synthesizing top 5 articles with Claude 3.5... <span class="success">Done.</span></div>
                    <div><span class="step">[STEP 3/3]</span> Sending email via SMTP to seu.email@gmail.com...</div>
                    <br>
                    <div><span class="success">[SUCCESS]</span> Email delivered successfully!</div>
                    <br>
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command"></span><span style="display:inline-block; width:8px; height:18px; background:#fff; vertical-align:middle; animation: blink 1s step-end infinite;"></span></div>
                </div>
            </div>
            <style>@keyframes blink { 50% { opacity: 0; } }</style>
        </body>
        </html>
        `
    },
    {
        name: 'print_cronos_email.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: "Google Sans", Roboto, Arial, sans-serif; background-color: #f6f8fc; margin: 0; padding: 30px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .gmail-window { width: 950px; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid #e0e0e0; display: flex; flex-direction: column; }
                .gmail-header { padding: 15px 20px; border-bottom: 1px solid #f1f3f4; display: flex; align-items: center; justify-content: space-between; }
                .subject-line { font-size: 22px; color: #202124; font-weight: normal; display: flex; align-items: center; gap: 10px; }
                .badge { background-color: #f1f3f4; color: #5f6368; font-size: 12px; padding: 2px 6px; border-radius: 4px; }
                .gmail-meta { padding: 15px 20px; display: flex; align-items: center; gap: 15px; }
                .avatar { width: 40px; height: 40px; background-color: #9d4edd; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold; }
                .sender-info { flex-grow: 1; }
                .sender-name { font-size: 14px; font-weight: bold; color: #202124; }
                .sender-email { font-size: 12px; color: #5f6368; }
                .email-date { font-size: 12px; color: #5f6368; }
                .gmail-body { padding: 20px 75px 40px 75px; font-size: 14px; color: #202124; line-height: 1.6; }
                .email-card { background: #fdfdfd; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; }
                .email-title { font-size: 18px; color: #1a73e8; margin-top: 0; }
                .news-item { margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #f1f3f4; }
                .news-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
                .news-title { font-weight: bold; font-size: 15px; margin-bottom: 5px;}
                .news-link { color: #1a73e8; text-decoration: none; font-size: 13px; }
            </style>
        </head>
        <body>
            <div class="gmail-window">
                <div class="gmail-header">
                    <div class="subject-line">
                        📊 Newsletter Diária - As 5 Principais Notícias de Hoje <span class="badge">Inbox</span>
                    </div>
                </div>
                <div class="gmail-meta">
                    <div class="avatar">C</div>
                    <div class="sender-info">
                        <div class="sender-name">Agente CRONOS <span class="sender-email">&lt;seu.email@gmail.com&gt;</span></div>
                        <div class="sender-email">to me</div>
                    </div>
                    <div class="email-date">08:00 AM (0 minutes ago)</div>
                </div>
                <div class="gmail-body">
                    <p>Bom dia,</p>
                    <p>Aqui está o seu resumo diário com as atualizações mais importantes do mercado coletadas e analisadas hoje:</p>
                    
                    <div class="email-card">
                        <h3 class="email-title">Destaques do Dia</h3>
                        
                        <div class="news-item">
                            <div class="news-title">1. OpenAI anuncia novo modelo focado em raciocínio lógico avançado</div>
                            <div>O novo modelo promete resolver problemas complexos de matemática e programação com um tempo de 'reflexão' antes da resposta, redefinindo benchmarks do setor.</div>
                            <a href="#" class="news-link">Ler artigo completo &rarr;</a>
                        </div>
                        
                        <div class="news-item">
                            <div class="news-title">2. Banco Central indica estabilidade da taxa Selic</div>
                            <div>Em ata divulgada na manhã de hoje, o Copom indicou que não há previsão de novos cortes na taxa básica de juros a curto prazo devido a pressões inflacionárias globais.</div>
                            <a href="#" class="news-link">Ler artigo completo &rarr;</a>
                        </div>
                        
                        <div class="news-item">
                            <div class="news-title">3. Startups de Inteligência Artificial captam investimento recorde no trimestre</div>
                            <div>Investimentos em startups early-stage focadas em IA generativa ultrapassaram a marca de US$ 10 bilhões apenas nos últimos três meses.</div>
                            <a href="#" class="news-link">Ler artigo completo &rarr;</a>
                        </div>
                    </div>
                    
                    <p style="color: #5f6368; font-size: 12px; margin-top: 20px;">
                        <em>Este e-mail foi gerado e enviado de forma autônoma pelo Agente CRONOS.</em>
                    </p>
                </div>
            </div>
        </body>
        </html>
        `
    },
    {
        name: 'print_cronos_cron.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: transparent; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .mac-terminal { width: 900px; background-color: rgba(30, 30, 30, 0.95); border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #444; backdrop-filter: blur(10px); }
                .mac-header { background-color: #323232; height: 28px; display: flex; align-items: center; padding: 0 10px; }
                .mac-dots { display: flex; gap: 8px; }
                .mac-dot { width: 12px; height: 12px; border-radius: 50%; }
                .mac-dot.red { background-color: #ff5f56; }
                .mac-dot.yellow { background-color: #ffbd2e; }
                .mac-dot.green { background-color: #27c93f; }
                .mac-title { flex-grow: 1; text-align: center; color: #999; font-family: -apple-system, sans-serif; font-size: 13px; font-weight: 500; margin-left: -40px; }
                .mac-body { padding: 15px 25px; font-family: "Menlo", "Monaco", "Courier New", monospace; font-size: 18px; line-height: 1.6; color: #fff; }
                .prompt { color: #00ffcc; }
                .command { color: #fff; }
                .success { color: #27c93f; font-weight: bold;}
                .key { color: #00d2ff; }
                .value { color: #ccc; }
            </style>
        </head>
        <body>
            <div class="mac-terminal">
                <div class="mac-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="mac-title">gustavo@MacBook-Pro: ~/hermes-agent</div>
                </div>
                <div class="mac-body">
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command">cronos cron create "0 8 * * *" "Visite um site de notícias confiável, leia as manchetes do dia, crie uma newsletter amigável com as 5 mais relevantes e me envie o resumo." --name "Newsletter do Cronos" --deliver email</span></div>
                    <br>
                    <div><span class="success">[✔]</span> Cron job created successfully!</div>
                    <div><span class="key">Task Name:</span> <span class="value">Newsletter do Cronos</span></div>
                    <div><span class="key">Schedule:</span> <span class="value">0 8 * * * (Everyday at 08:00 AM)</span></div>
                    <div><span class="key">Delivery Method:</span> <span class="value">Email (smtp.gmail.com)</span></div>
                    <div><span class="key">Status:</span> <span class="value" style="color: #27c93f">Active and running in background</span></div>
                    <br>
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command"></span><span style="display:inline-block; width:8px; height:18px; background:#fff; vertical-align:middle; animation: blink 1s step-end infinite;"></span></div>
                </div>
            </div>
            <style>@keyframes blink { 50% { opacity: 0; } }</style>
        </body>
        </html>
        `
    }
];

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    
    for (const mockup of mockups) {
        console.log(`Generating ${mockup.name}...`);
        const page = await browser.newPage();
        await page.setViewport({ width: 1300, height: 900, deviceScaleFactor: 2 });
        await page.setContent(mockup.html);
        
        // Wait a bit to ensure styles are applied
        await new Promise(r => setTimeout(r, 500));
        
        // Find the main container to screenshot just that part if possible, otherwise fullscreen with transparent background
        const element = await page.$('.mac-terminal, .window, .vscode, .gmail-window');
        
        if (element) {
             await element.screenshot({ path: mockup.name, omitBackground: true });
        } else {
             await page.screenshot({ path: mockup.name });
        }
        await page.close();
        console.log(`Saved ${mockup.name}`);
    }

    await browser.close();
})();
