import os
import sys
import time
import json
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

# إعدادات النظام
console = Console()

# إعداد مفتاح الـ API (يفضل وضعه في متغير بيئة)
API_KEY = "AIzaSyB-ulLc4L383-d6DvYD0U-hV4aKHhuo2Wo"
genai.configure(api_key=API_KEY)

class DragonAI:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.history = []
        self.output_dir = "dragon_outputs"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def banner(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        banner_art = """
        ██████  ██████   █████   ██████   ██████  ███    ██ 
        ██   ██ ██   ██ ██   ██ ██       ██    ██ ████   ██ 
        ██   ██ ██████  ███████ ██   ███ ██    ██ ██ ██  ██ 
        ██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██  ██ ██ 
        ██████  ██   ██ ██   ██  ██████   ██████  ██   ████ 
        """
        console.print(Text(banner_art, style="bold red"))
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="right")
        grid.add_row(
            "[bold yellow]⚡ REVOLUTIONARY WEB INTELLIGENCE[/bold yellow]",
            "[bold cyan]v2.0 PRO EDITION[/bold cyan]"
        )
        console.print(Panel(grid, border_style="red"))
        console.print(f"[bold white]Commander:[/bold white] [bold green]Monkey D Dragon[/bold green] | [bold white]GitHub:[/bold white] [blue]toolss0824828402[/blue]\n")

    def get_response(self, prompt, mode="expert"):
        personas = {
            "expert": "Senior Security & Software Architect. English only. Technical depth.",
            "simple": "Explain like I'm 5. Analogies. Simple English.",
            "code": "Pure Code Mode. Documentation in English. Optimized logic.",
            "audit": "Security Auditor. Find vulnerabilities in the provided code."
        }
        
        full_prompt = f"System: {personas.get(mode)}\nUser: {prompt}"
        
        try:
            chat = self.model.start_chat(history=self.history)
            response = chat.send_message(full_prompt)
            # تحديث الذاكرة
            self.history.append({"role": "user", "parts": [prompt]})
            self.history.append({"role": "model", "parts": [response.text]})
            return response.text
        except Exception as e:
            return f"[bold red]Critical Error:[/bold red] {str(e)}"

    def save_work(self, content, ext="md"):
        filename = f"{self.output_dir}/dragon_{int(time.time())}.{ext}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return filename

    def analyze_file(self):
        path = console.input("[bold yellow]📂 Drag file here or enter path: [/bold yellow]")
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = f.read()
            return content, path
        return None, None

    def menu(self):
        self.banner()
        table = Table(show_header=False, border_style="dim")
        table.add_row("[1] 🧠 AI Expert Search", "[2] 📝 Code Audit (Local File)")
        table.add_row("[3] 📄 README Architect", "[4] 🛠 Fast Code Generator")
        table.add_row("[5] 📜 View History", "[6] ❌ Terminate Session")
        console.print(table)
        
        return input("\n[?] Command > ")

    def run(self):
        while True:
            cmd = self.menu()
            
            if cmd == "6": break
            
            prompt = ""
            mode = "expert"
            
            if cmd == "1":
                prompt = console.input("[bold cyan]Prompt (English): [/bold cyan]")
            elif cmd == "2":
                content, path = self.analyze_file()
                if content:
                    prompt = f"Audit this file for bugs/vulnerabilities: \n{content}"
                    mode = "audit"
                else: continue
            elif cmd == "3":
                desc = console.input("[bold cyan]Project Description: [/bold cyan]")
                prompt = f"Create a professional GitHub README.md for: {desc}"
            elif cmd == "4":
                prompt = console.input("[bold cyan]What code do you need?: [/bold cyan]")
                mode = "code"
            
            with Progress(SpinnerColumn(spinner_name="dots12"), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
                progress.add_task(description="[bold red]Dragon is accessing database...[/bold red]", total=None)
                response = self.get_response(prompt, mode)

            # عرض النتيجة بـ Markdown احترافي
            console.print(Panel(Markdown(response), title="[bold green]DRAGON INTELLIGENCE[/bold green]", border_style="blue"))
            
            saved_file = self.save_work(response)
            console.print(f"[dim]✔ Knowledge saved to: {saved_file}[/dim]")
            input("\n[Press Enter to continue...]")

if __name__ == "__main__":
    app = DragonAI()
    app.run()
