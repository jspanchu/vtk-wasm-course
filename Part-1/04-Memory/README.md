# 04-Memory

This directory contains sample HTML/WAT/JS files that show how WebAssembly memories can be manipulated
from JavaScript

## Building

First, convert the `memory.wat` file into a `memory.wasm` file.

```pwsh
&$env:EMSDK/upstream/bin/wasm-as.exe ./memory.wat
```

## Running

Start a HTTP server in this directory, then open [http://localhost:8000](http://localhost:8000) in your browser and check the developer console for the result

```pwsh
python -m http.server
```
