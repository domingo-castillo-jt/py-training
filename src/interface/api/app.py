import os

import rollbar  # type: ignore
import rollbar.contrib.flask  # type: ignore
from flask import Flask, got_request_exception

from src.interface.api.api import api
from src.interface.api.cli import cli

app = Flask(__name__)


write_token = "6408eab7199940528fd17e193b7c7f5e"


@app.before_first_request
def init_rollbar() -> None:
    """init rollbar module"""
    rollbar.init(
        # access token
        "3c4fed617abb463caab073397f26507a",
        # environment name
        "production",
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False,
    )

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


app.register_blueprint(api)
app.register_blueprint(cli)
