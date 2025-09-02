# 01 Compiling C++ to WebAssembly

The `hello.cpp` file is a simple C++ application that prints a string and exits.

To compile it, run:

```sh
em++ hello.cpp -o hello.html
```

To run locally with Node.js:

```sh
node hello.js
```

To serve the generated HTML page, use:

```sh
python -m http.server
```

Then open [http://localhost:8000/hello.html](http://localhost:8000/hello.html) in your browser.
