from flask import Blueprint
from src.core.use_cases.get_all_items_use_case import get_all_items_use_case

cli = Blueprint('cli', __name__)
@cli.cli.command("get-all-items")
def get_all_items():
    print(get_all_items_use_case())
