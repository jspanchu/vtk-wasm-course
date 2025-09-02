/** EXERCISE: Complete the `writeFileToWASMMemory(file, wasmModule)` function to write a JS File object into WebAssembly memory.
 *  Hint: Use the `wasmModule._malloc` function to allocate `file.size` bytes in the WASM module.
 *        Then, iterate over each chunk, convert it to an ArrayBuffer, and copy it to the WASM memory using
 *        the `wasmModule.HEAPU8.set` method.
 *        Finally, the function should return the pointer of the allocated memory.
 */

/**
 * Break a Blob into individual blobs of `chunkSize` number of bytes.
 * @param {Blob} blob - The Blob to be chunked.
 * @param {number} chunkSize - The size of each chunk in bytes.
 * @returns {Blob[]} An array of Blob chunks.
 */
function chunkify(blob, chunkSize) {
  const numChunks = Math.ceil(blob.size / chunkSize);
  let i = 0;
  const chunks = [];
  while (i < numChunks) {
    const offset = (i++) * chunkSize;
    chunks.push(blob.slice(offset, offset + chunkSize));
  }
  return chunks;
}

/**
 * Binary search for a max value without knowing the exact value, only that it
 * can be under or over It dose not test every number but instead looks for
 * 1,2,4,8,16,32,64,128,96,95 to figure out that you thought about #96 from
 * 0-infinity
 *
 * @example findFirstPositive(x => matchMedia(`(max-resolution: ${x}dpi)`).matches)
 * @author Jimmy Wärting
 * @see {@link https://stackoverflow.com/a/72124984/1008999}
 * @param {function} f       The function to run the test on (should return truthy or falsy values)
 * @param {bigint} [b=1]  Where to start looking from
 * @param {function} d privately used to calculate the next value to test
 * @returns {bigint} Integer
 */
function findFirstPositive(f, b = 1n, d = (e, g, c) => g < e ? -1 : 0 < f(c = e + g >> 1n) ? c == e || 0 >= f(c - 1n) ? c : d(e, c - 1n) : d(c + 1n, g)) {
  for (; 0 >= f(b); b <<= 1n); return d(b >> 1n, b) - 1n;
}
const tries = [];
export const maxSize = findFirstPositive(x => {
  tries.push(Number(x).toLocaleString())
  try { new ArrayBuffer(Number(x)); return false } catch { return true }
});

// Utility functions
export async function writeFileToWASMMemory(file, wasmModule) {
  if (!wasmModule) return 0;
  // Break the file into chunks to handle large files safely.
  let chunks = chunkify(file, Number(maxSize));
  // TODO: Write chunk by chunk into linear WASM memory.
  //       See the exercise description at the top of this file for hints.
}
