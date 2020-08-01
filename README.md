# MDConverter
Library to convert Markdown to Atlassian Markup.

## Usage
The easiest way to use the library is by running the following command in the terminal:
```
python3 MDConverter.py infile outfile
```
Where infile is a path to the markdown file to convert and outfile is a path to the file to save the result to.

You can also use this library programmaticaly by creating a `Converter` instance with the elements to convert (from the `Elements` module) and call its `convert` function. Example:

```python
converter = Converter([Elements.NormalHeaderElement(), Elements.LinkElement()])
to_convert = """
# Header 1
[link](https://google.com)
## Header 2
"""

converter.convert(to_convert)
```

Result:
```
h1. Header 1
[link|https://google.com|]
h2. Header 2
```

## Current Capabilities
The current elements that the library can identify and convert are:

* Headers
  * Normal Headers
    ```
    # Header 1
    ## Header 2
    ```
  * Underline Headers
    ```
    Header 1
    ========
    Header 2
    --------
    ```
* Emphasis
  ```
  *Emphasis*
  _Emphasis_
  **Strong Emphasis**
  __Strong Emphasis__
  ```
* Block Quote
  ```
  > Block Quote
  ```
* Lists
  ```
  1. Ordered List
  * Unordered List
  - Unordered List
  + Unordered List
  ```
* Code Block

      ```

      This is code

      ```
* Inline code
  ```
  Here is some `inline code`.
  ```
* Links
  ```
  [This](http://google.com "Is a link")
  ```
* Images
  ```
  ![This is an image](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
  ```
    
## Expanding the Library

In order to add more elements, simply implement the IElement interface. Examples for implemented elements can be found in the `Elements` module.
