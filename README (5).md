# Basic Python HTTP Server

A minimal HTTP server implemented from scratch using Python's `socket` module. This project demonstrates fundamental networking concepts, HTTP protocol parsing, routing, and static file serving without external dependencies.

## Project Structure

```text
basic-python-http-server/
├── README.md          # Project documentation
├── main.py            # HTTP server implementation
└── index.html         # Default HTML file served at '/'
```

- **main.py**: Contains the server socket setup, request parsing, and response logic.
- **index.html**: Simple HTML page returned when a client requests the root path.

## Usage

1. **Place your `index.html`** in the project root (or modify the code to point to your HTML file).
2. **Start the server**:
   ```bash
   python3 main.py
   ```
3. **Open in a browser**:
   Navigate to `http://127.0.0.1:6969/` (or the host/port configured in `main.py`).

## Configuration

- **HOST**: IP address to bind (default: `127.0.0.1`)
- **PORT**: TCP port to listen on (default: `6969`)

Edit the `HOST` and `PORT` variables at the top of `main.py` to change these settings.

## Extending this Project

- **Routing**: Add more `if path == '/other'` branches to handle additional URLs.
- **Static Files**: Serve CSS, JS, or image files by checking file extensions and returning appropriate `Content-Type` headers.
- **Dynamic Responses**: Generate HTML based on request parameters (e.g., query strings).
- **Concurrency**: Use threads or `asyncio` to handle multiple client connections simultaneously.

## License

This project is released under the [MIT License](LICENSE).
