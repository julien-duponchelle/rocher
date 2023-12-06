# Rocher

Rocher is a Python package for the Monaco code editor. The Monaco Editor is the code editor that powers VS. Code. It provides a prebuilt version of the editor as a Python package, allowing you to embed it into any Python application as a standard Python package.

## Installation

```bash
pip install rocher
```

## Usage

The package provides only one function path():
    
```python   
import rocher

rocher.path()
```

This is the path where the Monaco editor is installed. You can serve after this path with your favorite Python web framework.

See the [samples/](Samples) folder for more examples to use it with multiple frameworks.

## Why the name Rocher?

Le Rocher is the hill where the Principality of Monaco is built. 

## Versioning

The version number of this package is the version of the Monaco Editor.

## Update the Monaco Editor

Edit update_editor.sh and change the version number. Then run the script. It will download the new version of the Monaco editor and update the package.

And run:    
```bash
hatch build -t sdist 
```
To build the packaged version.



## License

Licensed under the MIT License, see [LICENSE](LICENSE) for more information.

## Credits

All credit goes to the Monaco Editor team. This package is just a wrapper around their work.