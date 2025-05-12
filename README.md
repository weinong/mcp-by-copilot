# Disney Jokes MCP Server

A simple Model Context Protocol (MCP) server that returns jokes related to Disney animation movies.

## Overview

This project implements a Model Context Protocol (MCP) server that provides Disney-themed jokes. It's built using the MCP Python SDK and can be easily integrated with MCP clients like Claude Desktop.

## Features

- Get jokes about Disney characters like Mickey, Elsa, Simba, etc.
- Get jokes about Disney movies like Frozen, Lion King, Toy Story, etc.
- Get random Disney-themed jokes when no specific parameters are provided
- List available joke categories

## Tools

The server exposes the following MCP tools:

1. `get_disney_joke` - Returns a joke related to Disney animation movies
   - Parameters:
     - `character` (optional): Disney character to get a joke about (e.g., "mickey", "elsa")
     - `movie` (optional): Disney movie to get a joke about (e.g., "frozen", "lion_king")

2. `list_available_joke_categories` - Returns a list of available Disney joke categories

## Setup

### Requirements

- Python 3.10 or higher
- `uv` package manager

### Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   uv add "mcp[cli]"
   ```

## Usage

Run the server:

```bash
python disney_jokes.py
```

### Integration with Claude Desktop

To use this server with Claude Desktop:

1. Install [Claude Desktop](https://claude.ai/download)
2. Configure Claude Desktop to use this MCP server by editing the Claude Desktop config file
3. Ask Claude questions like "Tell me a joke about Mickey Mouse" or "Can you share a Frozen joke?"

## License

MIT