# Rocher

Rocher is a Python package for the Monoco editor. It provide a prebuild version as Python package allowing to embed the editor in any Python application as classic Python package.

## Installation

```bash
pip install rocher
```

## Usage

The package provide only one method path:
    
```python   
import rocher

rocher.path()
```

This is the path where the monaco editor is installed. You can serve after this path with you favorite Python web framework.

See the [samples/](Samples) folder for more examples to use it with multiple frameworks.

## Why the name Rocher?

Le Rocher is the hill where the Principality of Monaco is build. 

## Versioning

The version number of this package is the version of the Monaco Editor.

## Update the Monaco Editor

Edit update_editor.sh and change the version number. Then run the script. It will download the new version of the editor and update the package.

And run:    
```bash
hatch build -t sdist 
```
To build the packaged version.

## License

Licensed under the MIT License, see [LICENSE](LICENSE) for more information.

## Credits

All credits goes to the Monaco Editor team. This package is just a wrapper around their work.