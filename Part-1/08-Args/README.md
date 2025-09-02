# 07 Command line arguments

The `main.cpp` file uses `getenv` to read command line args. Although command line args do not
make total sense in a web application, native C++ apps might use them and expect them to be set to a specific
value in order to do something useful.

To compile it, run:

```sh
em++ -sMODULARIZE=1 -sEXPORT_NAME=createModule main.cpp -o main.js
```

To serve the generated HTML page, use:

```sh
python -m http.server
```

Then open [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

You should see it print the following in the dev console:

```
Argument 0: ./this.program
Argument 1: --refinement-ratio
Argument 2: 0.9
```
