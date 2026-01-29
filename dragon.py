import os
import time
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax

# إعدادات الواجهة
console = Console()

# إعداد مفتاح API - استبدل 'YOUR_API_KEY' بمفتاحك الخاص
genai.configure(api_key="AIzaSyC3Nyp_aH0DfQAoYqCdbvA5mhBVlTt1wNs")

def banner():
    os.system('clear')
    banner_text = """
    ██████  ██████   █████   ██████   ██████  ███    ██ 
    ██   ██ ██   ██ ██   ██ ██       ██    ██ ████   ██ 
    ██   ██ ██████  ███████ ██   ███ ██    ██ ██ ██  ██ 
    ██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██  ██ ██ 
    ██████  ██   ██ ██   ██  ██████   ██████  ██   ████ 
    """
    console.print(f"[bold red]{banner_text}[/bold red]")
    console.print("[bold yellow]The Revolutionary AI Search Tool (English Only)[/bold yellow]")
    console.print(Panel("[bold cyan]Developer: toolss0824828402\nGitHub: https://github.com/toolss0824828402[/bold cyan]"))

def get_ai_response(user_query, persona):
    # نظام الأنماط (Personas)
    personas_config = {
        "expert": "You are a senior technical expert. Provide deep, detailed, and professional technical answers in English only.",
        "simple": "Explain concepts like I am 5 years old (ELI5). Use simple analogies and easy English only.",
        "code": "Focus strictly on providing clean, optimized, and documented code snippets in English only."
    }
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # دمج التعليمات لضمان الإنجليزية فقط
    full_prompt = f"Instruction: {personas_config[persona]}. User Query: {user_query}"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def save_log(query, response):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    filename = f"logs/search_{int(time.time())}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Query: {query}\n\n## Response:\n{response}")
    return filename

def main():
    banner()
    console.print("\n[bold white]Select AI Persona:[/bold white]")
    console.print("1. [bold red]--expert[/bold red] (Deep Technical)")
    console.print("2. [bold green]--simple[/bold green] (Easy Explanation)")
    console.print("3. [bold blue]--code[/bold blue] (Coding Focus)")
    
    choice = input("\nSelect (1/2/3): ")
    persona_map = {"1": "expert", "2": "simple", "3": "code"}
    selected_persona = persona_map.get(choice, "expert")
    
    query = input(f"\n[?] Enter your search query: ")
    
    # مؤشر الانتظار (Loading Spinner)
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:2
        progress.add_task(description="AI is thinking...", total=None)
        answer = get_ai_response(query, selected_persona)
    
    # عرض الإجابة بتنسيق ملون (Rich Text)
    console.print(Panel(answer, title="[bold green]AI Response (English)[/bold green]", border_style="blue"))
    
    # حفظ السجل تلقائياً
    log_file = save_log(query, answer)
    console.print(f"\n[dim white]✔ Response saved to: {log_file}[/dim white]")
    
    # خيار النسخ السريع (يعتمد على البيئة، هنا كمثال نصي)
    console.print("[bold yellow]Tip: Long press to copy text in Termux![/bold yellow]")

if __name__ == "__main__":
    main()
