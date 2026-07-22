const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const mockups = [
    {
        name: 'print_antigravity.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #1e1e1e; color: #fff; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .window { width: 800px; background-color: #252526; border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.5); border: 1px solid #333; }
                .header { background-color: #333333; padding: 10px; text-align: center; font-size: 14px; font-weight: bold; color: #ccc; border-bottom: 1px solid #1e1e1e; display: flex; justify-content: space-between; align-items: center;}
                .dots { display: flex; gap: 8px; margin-left: 10px; }
                .dot { width: 12px; height: 12px; border-radius: 50%; }
                .dot.red { background-color: #ff5f56; }
                .dot.yellow { background-color: #ffbd2e; }
                .dot.green { background-color: #27c93f; }
                .content { padding: 20px; font-family: "JetBrains Mono", "Fira Code", Consolas, monospace; font-size: 16px; line-height: 1.6; }
                .user-msg { background-color: #2b2d31; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #00d2ff; }
                .ai-msg { padding: 15px; }
                .log-line { color: #888; font-size: 14px; margin: 5px 0; }
                .log-line span.success { color: #27c93f; }
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
                        <strong>User:</strong> Instale o Hermes Agent no meu computador e configure o ambiente para mim.
                    </div>
                    <div class="ai-msg">
                        <div style="margin-bottom: 15px;"><strong>Antigravity:</strong> Iniciando processo de instalação e configuração do Hermes Agent...</div>
                        <div class="log-line">[<span class="action">EXEC</span>] Cloning repository hermes-agent-core...</div>
                        <div class="log-line">[<span class="success">OK</span>] Repository cloned successfully to ~/hermes-agent</div>
                        <div class="log-line">[<span class="action">EXEC</span>] Creating virtual environment (python -m venv venv)...</div>
                        <div class="log-line">[<span class="success">OK</span>] Virtual environment created.</div>
                        <div class="log-line">[<span class="action">EXEC</span>] Installing dependencies (pip install -r requirements.txt)...</div>
                        <div class="log-line">[<span class="success">OK</span>] All dependencies installed successfully.</div>
                        <div class="log-line">[<span class="action">EXEC</span>] Initializing local databases...</div>
                        <div class="log-line">[<span class="success">OK</span>] Environment is fully configured and ready!</div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        `
    },
    {
        name: 'print_openrouter.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #0f172a; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .modal { width: 500px; background-color: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7); border: 1px solid #334155; }
                .modal-header { padding: 20px; border-bottom: 1px solid #334155; }
                .modal-title { color: #f8fafc; font-size: 18px; font-weight: 600; margin: 0; }
                .modal-body { padding: 20px; }
                .alert { background-color: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 8px; padding: 15px; margin-bottom: 20px; }
                .alert-title { color: #10b981; font-weight: 600; font-size: 14px; margin: 0 0 5px 0; }
                .alert-text { color: #94a3b8; font-size: 13px; margin: 0; }
                .key-container { background-color: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 15px; display: flex; justify-content: space-between; align-items: center; }
                .key-text { color: #f8fafc; font-family: "Fira Code", monospace; font-size: 15px; letter-spacing: 0.5px; position: relative;}
                .blur-box { position: absolute; left: 100px; top: -2px; width: 140px; height: 24px; background-color: #0f172a; display: flex; align-items: center; justify-content: center; letter-spacing: 4px; color: #64748b; }
                .btn { background-color: #3b82f6; color: white; border: none; border-radius: 6px; padding: 8px 16px; font-size: 14px; font-weight: 500; cursor: pointer; }
                .modal-footer { padding: 15px 20px; background-color: #0f172a; border-top: 1px solid #334155; display: flex; justify-content: flex-end; }
                .btn-done { background-color: #334155; color: white; border: none; border-radius: 6px; padding: 10px 20px; font-size: 14px; font-weight: 500; }
            </style>
        </head>
        <body>
            <div class="modal">
                <div class="modal-header">
                    <h3 class="modal-title">API Key Created: Hermes-Agent</h3>
                </div>
                <div class="modal-body">
                    <div class="alert">
                        <p class="alert-title">Success!</p>
                        <p class="alert-text">Please copy this key and save it somewhere safe. For security reasons, we will not show it to you again.</p>
                    </div>
                    <div class="key-container">
                        <div class="key-text">
                            sk-or-v1-8a9f4k2m9v8x7z6b3b12
                            <div class="blur-box">****************</div>
                        </div>
                        <button class="btn">Copy</button>
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="btn-done">Done</button>
                </div>
            </div>
        </body>
        </html>
        `
    },
    {
        name: 'print_terminal_config.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: transparent; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .mac-terminal { width: 700px; background-color: rgba(30, 30, 30, 0.95); border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #444; backdrop-filter: blur(10px); }
                .mac-header { background-color: #323232; height: 28px; display: flex; align-items: center; padding: 0 10px; }
                .mac-dots { display: flex; gap: 8px; }
                .mac-dot { width: 12px; height: 12px; border-radius: 50%; }
                .mac-dot.red { background-color: #ff5f56; }
                .mac-dot.yellow { background-color: #ffbd2e; }
                .mac-dot.green { background-color: #27c93f; }
                .mac-title { flex-grow: 1; text-align: center; color: #999; font-family: -apple-system, sans-serif; font-size: 13px; font-weight: 500; margin-left: -40px; }
                .mac-body { padding: 15px; font-family: "Menlo", "Monaco", "Courier New", monospace; font-size: 18px; line-height: 1.5; color: #fff; }
                .prompt { color: #00ffcc; }
                .command { color: #fff; }
                .question { color: #00d2ff; font-weight: bold; }
                .answer { color: #f9d423; }
                .success { color: #27c93f; }
            </style>
        </head>
        <body>
            <div class="mac-terminal">
                <div class="mac-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="mac-title">gustavo@MacBook-Pro: ~/hermes-agent</div>
                </div>
                <div class="mac-body">
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command">hermes configure</span></div>
                    <br>
                    <div><span class="question">?</span> Select Provider: <span class="answer">OpenRouter</span></div>
                    <div><span class="question">?</span> Select Model: <span class="answer">anthropic/claude-3.5-sonnet</span></div>
                    <div><span class="question">?</span> Enter API Key: <span class="answer">[hidden]</span></div>
                    <br>
                    <div><span class="success">[✔]</span> Provider set to OpenRouter</div>
                    <div><span class="success">[✔]</span> Model set to claude-3.5-sonnet</div>
                    <div><span class="success">[✔]</span> API Key saved to .env file!</div>
                    <div><span class="success">[✔]</span> Configuration complete!</div>
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
        name: 'print_vscode_env.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: #1e1e1e; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;}
                .vscode { width: 900px; height: 500px; background-color: #1e1e1e; border-radius: 8px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #333; display: flex; flex-direction: column; }
                .vs-header { height: 35px; background-color: #323233; display: flex; align-items: center; padding: 0 10px; border-bottom: 1px solid #2b2b2b;}
                .mac-dots { display: flex; gap: 8px; }
                .mac-dot { width: 12px; height: 12px; border-radius: 50%; }
                .mac-dot.red { background-color: #ff5f56; }
                .mac-dot.yellow { background-color: #ffbd2e; }
                .mac-dot.green { background-color: #27c93f; }
                .vs-title { flex-grow: 1; text-align: center; color: #ccc; font-size: 13px; }
                .vs-main { display: flex; flex-grow: 1; }
                .vs-sidebar { width: 200px; background-color: #252526; border-right: 1px solid #333; padding: 10px 0; }
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
            </style>
        </head>
        <body>
            <div class="vscode">
                <div class="vs-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="vs-title">hermes-agent - Visual Studio Code</div>
                </div>
                <div class="vs-main">
                    <div class="vs-sidebar">
                        <div class="vs-explorer-title">Explorer</div>
                        <div class="vs-file"><span>📁</span> src</div>
                        <div class="vs-file"><span>📁</span> tests</div>
                        <div class="vs-file active"><span>⚙️</span> .env</div>
                        <div class="vs-file"><span>📄</span> .gitignore</div>
                        <div class="vs-file"><span>📄</span> package.json</div>
                        <div class="vs-file"><span>📄</span> README.md</div>
                    </div>
                    <div class="vs-editor">
                        <div class="vs-tabs">
                            <div class="vs-tab"><span>⚙️</span> .env</div>
                        </div>
                        <div class="vs-code">
                            <div><span class="line-number">1</span><span class="comment"># HERMES AGENT CONFIGURATION</span></div>
                            <div><span class="line-number">2</span><span class="variable">HERMES_PROVIDER</span><span class="operator">=</span><span class="string">openrouter</span></div>
                            <div><span class="line-number">3</span><span class="variable">HERMES_MODEL</span><span class="operator">=</span><span class="string">anthropic/claude-3.5-sonnet</span></div>
                            <div><span class="line-number">4</span><span class="variable">OPENROUTER_API_KEY</span><span class="operator">=</span><span class="string">sk-or-v1-xxxxxxxxxxxxxxxxx</span></div>
                            <div><span class="line-number">5</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        `
    },
    {
        name: 'print_terminal_start.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: transparent; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .mac-terminal { width: 700px; background-color: rgba(30, 30, 30, 0.95); border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #444; backdrop-filter: blur(10px); }
                .mac-header { background-color: #323232; height: 28px; display: flex; align-items: center; padding: 0 10px; }
                .mac-dots { display: flex; gap: 8px; }
                .mac-dot { width: 12px; height: 12px; border-radius: 50%; }
                .mac-dot.red { background-color: #ff5f56; }
                .mac-dot.yellow { background-color: #ffbd2e; }
                .mac-dot.green { background-color: #27c93f; }
                .mac-title { flex-grow: 1; text-align: center; color: #999; font-family: -apple-system, sans-serif; font-size: 13px; font-weight: 500; margin-left: -40px; }
                .mac-body { padding: 15px; font-family: "Menlo", "Monaco", "Courier New", monospace; font-size: 18px; line-height: 1.5; color: #fff; }
                .prompt { color: #00ffcc; }
                .command { color: #fff; }
                .info { color: #00d2ff; }
                .success { color: #27c93f; }
                .separator { color: #888; }
                .robot { color: #f9d423; font-weight: bold;}
            </style>
        </head>
        <body>
            <div class="mac-terminal">
                <div class="mac-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="mac-title">gustavo@MacBook-Pro: ~/hermes-agent</div>
                </div>
                <div class="mac-body">
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command">hermes start</span></div>
                    <br>
                    <div><span class="info">[INFO]</span> Initializing Hermes Agent Core v2.0...</div>
                    <div><span class="success">[OK]</span> Connecting to OpenRouter API... Connected!</div>
                    <div><span class="success">[OK]</span> Loading SQLite Local Memory (memory.db)... Done.</div>
                    <div><span class="success">[OK]</span> Hermes Gateway Online! Listening for prompts...</div>
                    <div class="separator">-------------------------------------------------------------</div>
                    <div class="robot">🤖 Hermes Agent is active and ready. Type 'exit' to stop.</div>
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
        name: 'print_terminal_chat.png',
        html: `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background-color: transparent; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
                .mac-terminal { width: 800px; background-color: rgba(30, 30, 30, 0.95); border-radius: 10px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #444; backdrop-filter: blur(10px); }
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
                .robot { color: #f9d423; font-weight: bold;}
                .response { color: #ccc; margin-left: 25px; border-left: 2px solid #555; padding-left: 15px; margin-top: 10px; margin-bottom: 20px;}
            </style>
        </head>
        <body>
            <div class="mac-terminal">
                <div class="mac-header">
                    <div class="mac-dots"><div class="mac-dot red"></div><div class="mac-dot yellow"></div><div class="mac-dot green"></div></div>
                    <div class="mac-title">gustavo@MacBook-Pro: ~/hermes-agent</div>
                </div>
                <div class="mac-body">
                    <div><span class="prompt">➜  hermes-agent</span> <span class="command">hermes chat "Olá Hermes! Quem é você e qual a sua função principal no meu computador?"</span></div>
                    <br>
                    <div class="robot">🤖 Hermes Agent:</div>
                    <div class="response">
                        "Olá! Eu sou o Hermes, seu assistente autônomo de IA. Estou configurado para buscar informações na web, processar dados e executar tarefas no seu computador."
                    </div>
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
        await page.setViewport({ width: 1200, height: 800, deviceScaleFactor: 2 });
        await page.setContent(mockup.html);
        
        // Wait a bit to ensure styles are applied
        await new Promise(r => setTimeout(r, 500));
        
        // Find the main container to screenshot just that part if possible, otherwise fullscreen with transparent background
        const element = await page.$('.mac-terminal, .window, .modal, .vscode');
        
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
