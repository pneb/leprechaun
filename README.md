# Leprechaun

A lightweight and efficient asyncio-like library for Python 3.

## Installation

To install Leprechaun, use `pip`:

```
pip install git+https://github.com/pneb/leprechaun
```

## Usage

Here is an example of how to use Leprechaun to run a simple coroutine that prints "Hello, World!" every second:

```py
import leprechaun

async def main():
    while True:
        print("Hello, World!")
        await leprechaun.sleep(1)

leprechaun = leprechaun.Leprechaun()
leprechaun.run_until_complete(main())
```

For more detailed documentation and usage examples, see the [Leprechaun API reference](https://pneb.github.io/leprechaun/). (Coming Soon)

## Features

- Provides a simple and efficient way to write asynchronous code using coroutines and the `async` and `await` keywords.
- Schedules and runs tasks concurrently using a lightweight event loop.
- Offers a `sleep` function to pause a coroutine for a specified number of seconds.

## Limitations

Leprechaun is designed to be a simple and lightweight alternative to asyncio, and as such, it does not offer as many features as asyncio. In particular, it does not support many of the more advanced features of asyncio such as networking, subprocesses, and synchronization primitives. However, it is well-suited for simple concurrent programming tasks that do not require these advanced features.

## License

Leprechaun is released under the MIT License. See [LICENSE](https://github.com/pneb/leprechaun/blob/master/LICENSE) for more information.
