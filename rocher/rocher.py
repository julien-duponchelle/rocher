import json
import os


def path() -> str:
    """
    Returns the absolute path to the installation of the Monaco editor.
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "vs")


def colorize_html(static_root: str, container_id: str, initialize=True, **kwargs) -> str:
    """
    Return code to colorize the contents of an HTML element.

    static_root: The path to the static directory of the Monaco editor.
    container_id: The ID of the HTML element to contain the editor.
    initialize: Whether to initialize the Monaco editor (default: True). Need to be set to False if the editor is already loaded.
    **kwargs: Additional arguments to pass to the Monaco editor.
    """
    output = ""
    if initialize:
        output += _init_monaco_editor(static_root)
    output += _monaco_editor("colorizeElement", container_id, **kwargs)
    return output

def editor_html(static_root: str, container_id: str, language: str,  value: str, **kwargs) -> str:
    """
    Returns the HTML for the editor.

    static_root: The path to the static directory of the Monaco editor.
    container_id: The ID of the HTML element to contain the editor.
    language: The language of the code to be edited.
    value: The code to be edited.
    **kwargs: Additional arguments to pass to the Monaco editor.
    """
    output = _init_monaco_editor(static_root)
    output += _monaco_editor("create", container_id, language=language, value=value, **kwargs)
    return output


def _init_monaco_editor(static_root: str) -> str:
    if static_root.endswith("/"):
        static_root = static_root[:-1]
    output =  f"""
    <script src="{static_root}/loader.js"></script>
    <script>
        require.config({{ paths: {{ vs: '{static_root}' }} }});
    </script>
    """
    return output


def _monaco_editor(method: str, container_id: str, **kwargs) -> str:
    """
    Internal function to return the HTML for the editor.
    """
    output =  f"""
    <script>
        define('rocher_editor_{container_id}', ['vs/editor/editor.main'], function() {{
            return  monaco.editor.{method}(document.getElementById('{container_id}'), {{
    """
    output += json.dumps(kwargs)[1:-1]
    print(output)
    output += """});
            });
    </script>
    """

    return output