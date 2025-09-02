# 03-Imports and Exports in WebAssembly

This directory has a `simple.wat` file which contains WebAssembly instructions in ASCII
text. Hence the file extension is `.wat`, which stands for WebAssembly Text

The `simple.js` sets up a dictionary that defines functions which are imported by the `simple.wasm`

## Building

1. First, convert the wat file into a .wasm using the `wasm-as.exe` program.
    ```pwsh
        &$env:EMSDK\upstream\bin\wasm-as.exe .\simple.wat
    ```
2. Now that `simple.wasm` is generated, run `node .\simple.js`.

## Result

You should see the following line printed in the terminal.

```pwsh
$ node .\simple.js
Imported function called with arg: 42
```
