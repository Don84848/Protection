import os
import requests
from urllib.parse import urlparse
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.text import Text
import pyfiglet
from time import sleep

console = Console()

def display_banner():
    try:
        banner_text = pyfiglet.figlet_format("Extractor", font="small")
    except Exception:
        banner_text = "=== Extractor ==="
        
    colored_banner = Text(banner_text, style="bold magenta")
    
    console.print(Panel(
        colored_banner, 
        box=box.DOUBLE, 
        border_style="magenta",
        title="[bold red] v1.0 [/bold red]",
        subtitle="[bold yellow] Developer: AD | TG: @lapsusdev [/bold yellow]"
    ))
    
    desc = Text("🌐 URL to Source Code Extractor\nFetch & Extract Front-End Source Code Instantly!", style="bold cyan", justify="center")
    console.print(Panel(desc, box=box.ROUNDED, border_style="cyan"))
    console.print()

def get_valid_filename(url):
    domain = urlparse(url).netloc
    if not domain:
        domain = "extracted_page"
    domain = domain.replace("www.", "").replace("/", "_").replace(":", "_")
    return f"{domain}_source.html"

def extract_source(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
    with Progress(
        SpinnerColumn(spinner_name="dots2"),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("[yellow]🔌 Connecting to Server...", total=None)
        sleep(0.5)
        
        try:
            progress.update(task, description="[cyan]📥 Downloading Source Code...")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            progress.update(task, description="[green]💾 Saving to file...")
            sleep(0.5)
            
            filename = get_valid_filename(url)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
                
            return filename, len(response.text)
            
        except requests.exceptions.MissingSchema:
            progress.update(task, description="[red]❌ Error: Invalid URL (Include http:// or https://)[/red]")
            sleep(1)
            return None, 0
        except Exception as e:
            progress.update(task, description=f"[red]❌ Connection Error: {e}[/red]")
            sleep(1)
            return None, 0

def format_size(size):
    for unit in ['B', 'KB', 'MB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} GB"

def main():
    console.clear()
    display_banner()
    
    target_url = Prompt.ask("[bold green]🔗 Enter Website URL (e.g., https://example.com)[/bold green]")
    
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
        console.print(f"[dim]Auto-added https:// -> {target_url}[/dim]\n")
    
    console.print()
    filename, size = extract_source(target_url)
    
    if filename:
        console.print(Panel(
            f"🎉 [bold green]Source Code Extracted Successfully![/bold green] 🚀\n\n"
            f"🌐 [bold cyan]Target URL:[/bold cyan] [yellow]{target_url}[/yellow]\n"
            f"📁 [bold cyan]Saved File:[/bold cyan] [yellow]{filename}[/yellow]\n"
            f"📦 [bold cyan]File Size:[/bold cyan]  [yellow]{format_size(size)}[/yellow]\n\n"
            f"💡 [dim]Tip: You can now protect this file using protect.py![/dim]",
            box=box.HEAVY,
            border_style="green",
            title="[bold white]Result[/bold white]"
        ))
    
    another = Prompt.ask("\n[bold cyan]🔄 Extract another website?[/bold cyan]", choices=["y", "n"], default="n")
    if another.lower() == 'y':
        main()
    else:
        console.print("\n[bold green]🌐 Thanks for using Extractor Toolkit! Stay productive. 🚀[/bold green]\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]⚠️ Exited by user. Goodbye![/yellow]")
