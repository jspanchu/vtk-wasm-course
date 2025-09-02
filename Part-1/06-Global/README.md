# 06-Global

This directory contains sample HTML/WAT/JS files that show how WebAssembly globals can be read
and written to from JavaScript

## Building

First, convert the `global.wat` file into a `global.wasm` file.

```pwsh
&$env:EMSDK/upstream/bin/wasm-as.exe ./global.wat
```
