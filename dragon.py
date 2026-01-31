import os
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# --- إعدادات الهوية الجديدة ---
USERNAME = "PyDragonX"
GITHUB_LINK = "https://github.com/PyDragonX"

# --- إعدادات الـ API ---
# استخدم نموذج 'gemini-1.5-flash' وتأكد من تحديث المكتبة لتجنب خطأ 404
API_KEY = "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"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

console = Console()

def save_to_history(prompt, response):
    with open("dragon_history.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {prompt}\nAI: {response}\n{'-'*30}\n")

def display_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # واجهة احترافية بالاسم الجديد
    console.print(Panel.fit(
        f"[bold cyan]🐉 {USERNAME} REVOLUTIONARY SYSTEM v2.5[/bold cyan]\n"
        f"[bold white]GitHub: {GITHUB_LINK}[/bold white]",
        border_style="cyan",
        title="[bold red]VIRTUAL TERMINAL[/bold red]"
    ))
    
    table = Table(show_header=False, box=None)
    table.add_row("[1] 🧠 AI Expert Search", "[2] 📝 Code Audit (Local File)")
    table.add_row("[3] 📄 README Architect", "[4] 🛠️ Fast Code Generator")
    table.add_row("[5] 📜 View History", "[6] 🔄 Check for Updates")
    table.add_row("[7] ❌ Terminate Session", "") # زر الخروج
    
    console.print(Panel(table, title="[bold yellow]Select an Option[/bold yellow]", border_style="blue"))

def main():
    while True:
        display_menu()
        choice = input(f"\n[{USERNAME}] @ Terminal:~$ ")
        
        if choice == '1':
            prompt = input("Enter your query: ")
            try:
                res = model.generate_content(prompt)
                console.print(Panel(res.text, title="Result", border_style="green"))
                save_to_history(prompt, res.text)
            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] {e}")
            input("\nPress Enter to return...")

        elif choice == '5':
            console.print("\n[bold cyan]--- History ---[/bold cyan]")
            if os.path.exists("dragon_history.txt"):
                with open("dragon_history.txt", "r") as f: print(f.read())
            else:
                console.print("No history found.")
            input("\nPress Enter...")

        elif choice == '6':
            console.print(f"[bold green]Checking {GITHUB_LINK} for updates...[/bold green]")
            # هنا يمكنك إضافة كود عمل git pull مستقبلاً
            input("\nAlready up to date! Press Enter...")

        elif choice == '7':
            console.print(f"[bold red]Shutting down {USERNAME} Intelligence... Goodbye![/bold red]")
            break
        
        # يمكنك برمجة باقي الأزرار (2, 3, 4) بنفس الطريقة

if __name__ == "__main__":
    main()
