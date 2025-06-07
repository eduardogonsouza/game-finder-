from ui import print_banner, get_platform_choice, get_user_input, format_results, ask_continue, print_final_message, clear_screen
from search_manager import SearchManager
from rich.console import Console
import sys

console = Console()

def main():
    try:
        while True:
            clear_screen()
            print_banner()
            
            choice = get_platform_choice()
            
            if choice == "free_epic":
                console.print("🔍 Buscando jogos gratuitos na Epic Games...")
                search_manager = SearchManager()
                results = search_manager.get_free_epic_games()
                console.print()
                format_results(results, is_free_games=True)
                console.print()
                
                if not ask_continue():
                    break
                continue
            
            game_name = get_user_input()
            if game_name is None:
                break
            
            console.print(f"🔍 Procurando '{game_name}' nas plataformas selecionadas...")
            search_manager = SearchManager()
            results = search_manager.search_all_platforms(choice, game_name)
            
            console.print()
            format_results(results)
            console.print()
            
            if not ask_continue():
                break
        
        print_final_message()
        
    except KeyboardInterrupt:
        console.print("\n👋 Até logo!")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
