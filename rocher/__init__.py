import os

def path() -> str:
    """
    Returns the absolute path to the installation of the Monaco editor.
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "vs")


def flask_editor_register(app) -> str:
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
    app.jinja_env.globals.update(rocher_editor=flask_editor_html)


def editor_html(static_root: str, container_id: str, language: str,  value: str, **kwargs) -> str:
    """
    Returns the HTML for the editor.

    static_root: The path to the static directory of the Monaco editor.
    container_id: The ID of the HTML element to contain the editor.
    language: The language of the code to be edited.
    value: The code to be edited.
    """

    if static_root.endswith("/"):
        static_root = static_root[:-1]

    output =  f"""
    <script src="{static_root}/loader.js"></script>
    <script>
        require.config({{ paths: {{ vs: '{static_root}' }} }});
        define('rocher_editor', ['vs/editor/editor.main'], function() {{ return  monaco.editor.create(document.getElementById('{container_id}'), {{
    """
    output += "value: '"
    output += value.replace("'", "\\'").replace("\n", "\\n")
    output += "',\n"

    for key, value in kwargs.items():
        if isinstance(value, bool):
            output += f"""{key}: {str(value).lower()},\n"""
        elif isinstance(value, int) or isinstance(value, float):
            output += f"""{key}: {value},\n"""
        else:
            output += f"""{key}: '{value}',\n"""

    output += f"""
                    language: '{language}'
                }});
            }});
    </script>
    """

    return output