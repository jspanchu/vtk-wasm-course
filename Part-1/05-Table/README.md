# 05-Table

This directory contains sample HTML/WAT/JS files that show how WebAssembly tables can be used
from JavaScript

## Building

First, convert the `table.wat` file into a `table.wasm` file.

```pwsh
&$env:EMSDK/upstream/bin/wasm-as.exe ./table.wat
```
