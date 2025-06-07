import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.align import Align
import questionary
import time

console = Console()

def clear_screen():
    console.clear()

def print_banner():
    banner_text = Text("Game Finder", style="bold blue")
    panel = Panel(Align.center(banner_text), padding=(1, 2))
    console.print(panel)
    console.print()

def print_loading(message, duration=1):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        progress.add_task(f"{message}...", total=None)
        time.sleep(duration)

def print_simple_loading(message):
    console.print(f"🔍 {message}...", end="")

def print_success(message):
    console.print(f"✅ {message}")

def print_error(message):
    console.print(f"❌ {message}")

def get_platform_choice():
    choices = [
        {"name": "Steam", "value": ["steam"]},
        {"name": "Nuuvem", "value": ["nuuvem"]},
        {"name": "Epic Games", "value": ["epic"]},
        {"name": "Todas as plataformas", "value": ["steam", "nuuvem", "epic"]},
        {"name": "Verificar Jogos Gratuitos Epic Games", "value": "free_epic"},
        {"name": "❌ Sair", "value": "exit"}
    ]
    
    answer = questionary.select(
        "Escolha uma opção:",
        choices=choices
    ).ask()
    
    if answer == "exit":
        console.print(Panel("Obrigado por usar o Game Finder! 👋"))
        sys.exit(0)
    
    if answer != "free_epic" and isinstance(answer, list) and "epic" in answer:
        warning_text = "⚠️ AVISO: A busca na Epic Games abrirá uma aba do Chrome visível."
        console.print(Panel(warning_text, title="⚠️ Atenção"))
        console.print()
    
    return answer

def get_user_input():
    while True:
        game_name = questionary.text("Digite o nome do jogo para buscar:").ask()
        
        if game_name and game_name.strip():
            return game_name.strip()
        elif game_name is None:
            return None
        else:
            console.print("❌ O nome do jogo não pode estar vazio!")

def format_game_info(result, is_free=False):
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column("Field", width=15)
    table.add_column("Value")
    
    table.add_row("Plataforma:", result['platform'])
    table.add_row("Jogo:", result['name'])
    table.add_row("URL:", result.get('url', 'N/A'))
    
    if is_free:
        table.add_row("Status:", "🆓 GRATUITO")
        title = "🆓 JOGO GRATUITO"
    elif result.get('has_discount') and result.get('discount') != "Sem desconto":
        if result.get('original_price') != result.get('current_price'):
            table.add_row("Preço Original:", result['original_price'])
        table.add_row("Preço Final:", result['current_price'])
        table.add_row("Desconto:", result['discount'])
        title = "🏷️ PROMOÇÃO ATIVA!"
    else:
        table.add_row("Preço:", result.get('current_price', 'N/A'))
        title = result['platform']
    
    return Panel(table, title=title, padding=(0, 1))

def format_results(results, is_free_games=False):
    if not results:
        error_panel = Panel(
            "❌ Nenhum resultado encontrado!\n💡 Dica: Tente um termo diferente",
            title="❌ Sem Resultados"
        )
        console.print(error_panel)
    else:
        if is_free_games:
            success_text = f"🆓 {len(results)} jogos gratuitos encontrados na Epic Games:"
        else:
            success_text = f"🎉 Encontrados {len(results)} resultado(s):"
        
        console.print(Panel(success_text))
        console.print()
        
        for i, result in enumerate(results, 1):
            console.print(format_game_info(result, is_free_games))
            if i < len(results):
                console.print()

def ask_continue():
    return questionary.confirm("Deseja fazer outra busca?", default=True).ask()

def print_final_message():
    final_panel = Panel(
        Align.center(Text("Obrigado por usar!", style="bold green")),
        padding=(1, 2)
    )
    console.print(final_panel)
