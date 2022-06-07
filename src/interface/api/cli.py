from src.core.use_cases.get_all_items_use_case import get_all_items_use_case

def cli_routes(app):
    @app.cli.command("get-all-items")
    def get_all_items():
        print(get_all_items_use_case())
