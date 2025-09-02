# 07 Environment Variables

The `main.cpp` file uses `getenv` to read environment variables. Although environment variables do not
make total sense in a web application, native C++ apps might use them and expect them to be set to a specific
value in order to do something useful.

To compile it, run:

```sh
em++ -sMODULARIZE=1 -sEXPORT_NAME=createModule "-sEXPORTED_RUNTIME_METHODS=['ENV']" main.cpp -o main.js
```

To serve the generated HTML page, use:

```sh
python -m http.server
```

Then open [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

You should see it print "HI!" in the dev console.
