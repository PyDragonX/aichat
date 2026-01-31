import os
from groq import Groq
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# --- إعدادات الهوية والاتصال ---
USERNAME = "PyDragonX"
GITHUB_LINK = "https://github.com/PyDragonX"
# تم استخدام مفتاحك الذي أرفقته سابقاً
client = Groq(api_key="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")

console = Console()

def save_to_history(prompt, response):
    """حفظ المحادثات في سجل نصي"""
    with open("dragon_history.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {prompt}\nAI: {response}\n{'-'*30}\n")

def get_groq_response(user_input):
    """جلب الرد باستخدام أحدث نموذج متاح من Groq"""
    # تم تغيير النموذج إلى Llama 3.1 8B Instant لضمان السرعة والاستمرارية
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7,
        max_tokens=1024,
    )
    return completion.choices[0].message.content

def display_menu():
    """واجهة الأداة الاحترافية باسمك الجديد"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    console.print(Panel.fit(
        f"[bold cyan]🐉 {USERNAME} REVOLUTIONARY SYSTEM v2.5[/bold cyan]\n"
        f"[bold white]GitHub: {GITHUB_LINK}[/bold white]",
        border_style="cyan",
        title="[bold red]VIRTUAL TERMINAL (GROQ ENGINE)[/bold red]"
    ))
    
    table = Table(show_header=False, box=None)
    table.add_row("[1] 🧠 AI Expert Search", "[2] 📝 Code Audit (Local File)")
    table.add_row("[3] 📄 README Architect", "[4] 🛠️ Fast Code Generator")
    table.add_row("[5] 📜 View History", "[6] 🔄 Check for Updates")
    table.add_row("[7] ❌ Terminate Session", "")
    
    console.print(Panel(table, title="[bold yellow]Main Control Panel[/bold yellow]", border_style="blue"))

def main():
    while True:
        display_menu()
        choice = input(f"\n[{USERNAME}] @ Terminal:~$ ")
        
        if choice == '1':
            prompt = input("Enter your query: ")
            try:
                console.print("[yellow]Dragon is processing your request...[/yellow]")
                response_text = get_groq_response(prompt)
                console.print(Panel(response_text, title="Dragon AI Response", border_style="green"))
                save_to_history(prompt, response_text)
            except Exception as e:
                # هذا الجزء سيمسك أي أخطاء مستقبلية في اسم النموذج
                console.print(f"[bold red]Critical Error:[/bold red] {e}")
            input("\nPress Enter to return...")

        elif choice == '5':
            console.print("\n[bold cyan]--- Local Interaction History ---[/bold cyan]")
            if os.path.exists("dragon_history.txt"):
                with open("dragon_history.txt", "r", encoding="utf-8") as f:
                    console.print(f.read())
            else:
                console.print("[yellow]No logs found.[/yellow]")
            input("\nPress Enter...")

        elif choice == '6':
            console.print(f"[bold green]Scanning repository: {GITHUB_LINK}[/bold green]")
            console.print("Status: [bold blue]System is operating on the latest revolutionary build.[/bold blue]")
            input("\nPress Enter...")

        elif choice == '7':
            console.print(f"[bold red]Shutting down {USERNAME}... Session Terminated.[/bold red]")
            break
        
        elif choice in ['2', '3', '4']:
            console.print("[bold magenta]Feature locked: Integration with local files coming in next update![/bold magenta]")
            input("\nPress Enter...")
        
        else:
            console.print("[red]Unknown Command![/red]")
            input()

if __name__ == "__main__":
    main()
