from flask import Flask

from src.core.use_cases.get_all_items_use_case import get_all_items_use_case

app = Flask(__name__)


@app.cli.command("get-all-items")
def get_all():
    return get_all_items_use_case()
