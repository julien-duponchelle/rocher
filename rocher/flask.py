from .rocher import editor_html, colorize_html, path

def editor_register(app) -> None:
    """
    Registers the editor with a Flask app.
    """
    from flask import Blueprint

    static_editor_path = "/static/vs"

    # Serve the static files from the Monaco editor
    blueprint = Blueprint(
        "monaco", __name__, static_url_path=static_editor_path, static_folder=path()
    )
    app.register_blueprint(blueprint)

    # Expose the editor_html function to Jinja templates with static directory already set
    def flask_editor_html(*args, **kwargs):
        return editor_html(static_editor_path, *args, **kwargs)

    def flask_colorize_html(*args, **kwargs):
        return colorize_html(static_editor_path, *args, **kwargs)
    app.jinja_env.globals.update(rocher_editor=flask_editor_html, rocher_colorize=flask_colorize_html)