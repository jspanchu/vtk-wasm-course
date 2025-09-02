const fs = require('fs');

const imports = {
  my_namespace: {
    imported_func: (arg) => console.log("Imported function called with arg:", arg)
  }
};

const wasmBuffer = fs.readFileSync('simple.wasm');
WebAssembly.instantiate(wasmBuffer, imports)
  .then(obj => {
    const instance = obj.instance;
    instance.exports.exported_func();
  });
