# Konfigurasi Environment dan IDE

- Editor: Visual Studio Code, dibuka dari folder proyek python-untuk-pemula
- Interpreter: venv/bin/python (Python 3.14.9 di Arch Linux WSL2)
- Pengaturan editor: .vscode/settings.json (interpreter venv, indentasi 4 spasi)
- Virtual environment dibuat dengan: python -m venv venv
- Mengaktifkan environment: source venv/bin/activate
- Library dikelola dengan pip di dalam venv (contoh: pip install requests)
- File .gitignore mengecualikan venv/, __pycache__/, dan .env
