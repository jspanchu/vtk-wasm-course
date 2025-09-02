# 05-Table

This directory contains sample HTML/WAT/JS files that show how WebAssembly memories can be manipulated
from JavaScript

## Building

First, convert the `table.wat` file into a `table.wasm` file.

```pwsh
&$env:EMSDK/upstream/bin/wasm-as.exe ./table.wat
```
