# Installation Instructions Using the emsdk

First, check the platform-specific notes below and install any prerequisites. The core Emscripten SDK (emsdk) driver is a Python script. You can get it for the first time with:

## Get the emsdk repo

```sh
git clone https://github.com/emscripten-core/emsdk.git
```

## Enter that directory

```sh
cd emsdk
```

> **Note:**  
> You can also get the emsdk without git, by selecting “Clone or download ⇒ Download ZIP” on the emsdk GitHub page.

Run the following emsdk commands to get the latest tools from GitHub and set them as active:

## Fetch the latest version of the emsdk (not needed the first time you clone)

```sh
git pull
```

## Download and install the latest SDK tools

```sh
./emsdk install latest
```

## Make the "latest" SDK "active" for the current user (writes `.emscripten` file)

```sh
./emsdk activate latest
```

## Activate PATH and other environment variables in the current terminal

```sh
# Windows
./emsdk_env.ps1
# Linux/macOS
source ./emsdk_env.sh
```

> **Tip:**  
> If you want to avoid executing `source ./emsdk_env.sh` every time you open a new terminal, you can follow the instructions given by the `emsdk activate` command above to add this command to your startup scripts.

> **Note:**  
> On Windows, run `emsdk.bat` instead of `./emsdk`, and `emsdk_env.bat` instead of `source ./emsdk_env.sh`.

> **Note:**  
> On Windows, if you use the `activate` command, the step of `emsdk_env.bat` is optional. If you want to know more, see [activate SDK version](https://emscripten.org/docs/getting_started/downloads.html#activate-sdk-version).

> **Note:**  
> `git pull` will fetch the current list of tags, but very recent ones may not yet be present there. You can run `./emsdk update-tags` to update the list of tags directly.

If you change the location of the SDK (e.g., take it to another computer on a USB drive), re-run the `./emsdk activate latest` and `source ./emsdk_env.sh` commands.
