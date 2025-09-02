import createFileViewerModule from "./build/FileViewer.js";
import { writeFileToWASMMemory } from "./utilities/writeFileToWasmMemory.js";

var wasmModule = null; // Will hold the wasm module after it's loaded
var fileViewer = null; // Will hold the FileViewer instance

/**
 * Load a file from a Blob into the WASM module's virtual filesystem.
 * @param {Blob} file - The Blob to load.
 * @return {Promise<void>}
 */
async function loadFileFromBlob(file) {
  if (!wasmModule) return;
  let fileBuffer = await writeFileToWASMMemory(file);
  await fileViewer.WriteDataFileToVirtualFS(file.name, fileBuffer, file.size);
  wasmModule._free(fileBuffer);
}

// Main execution
// Get the fileUrl parameter from the URL
let url = new URL(window.location.href);
let fileUrl = url.searchParams.get('fileUrl');
// Download the file.
let { blob, filename } = await download(fileUrl);
let file = new File([blob], filename, { type: blob.type });
// Create the wasm module
wasmModule = await createFileViewerModule();
// Create the FileViewer instance
fileViewer = new wasmModule.FileViewer();
// Copy the downloaded file into the wasm module's virtual filesystem
await loadFileFromBlob(file);
// Load the file and render it
fileViewer.ShowFile(filename);
