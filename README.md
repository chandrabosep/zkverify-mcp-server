# zkVerify MCP Server

**Comprehensive MCP server for zkVerify documentation, resources, and tools.**

> **Created by [Chandra Bose](https://github.com/chandrabosep)**


This project provides a **ready-to-use MCP server** for developers to integrate zkVerify resources into AI assistants such as **Claude Desktop** and **Cursor**, enabling access to documentation, tutorials, SDK examples, and live fetching tools.

---

## **Features**

-   9 pre-configured resources covering zkVerify:

    -   `overview`, `architecture`, `sdk`, `tutorials`, `api`, `faq`, `contracts`, `proofs`, `vflow`

-   1 tool for fetching live documentation: `fetch_zkverify_docs`
-   Offline support for embedded knowledge
-   Compatible with **Claude Desktop (Docker)** and **Cursor (local Python)**
-   Easy setup and configuration

---

## **Project Structure**

```
zkverify-mcp/
├── Dockerfile             # Docker build file
├── requirements.txt       # Python dependencies
├── zkverify_server.py     # MCP server implementation
├── run_zkverify.sh        # Shell script for Cursor
├── readme.txt             # Original notes
├── CLAUDE.md              # Claude-specific instructions
```

> **Note:** `venv/` is not included in the repo. Developers can create their own virtual environment for local Python setup.

---

## **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/zkverify-mcp-server.git
cd zkverify-mcp-server
```

---

## **A. Docker Setup (Claude Desktop)**

1. Build the Docker image:

```bash
docker build -t zkverify-mcp-server .
```

2. Create your **custom catalog**:

```bash
mkdir -p ~/.docker/mcp/catalogs
nano ~/.docker/mcp/catalogs/custom.yaml
```

Add:

```yaml
version: 2
name: custom
displayName: Custom MCP Servers
registry:
    zkverify:
        description: "Comprehensive zkVerify documentation and knowledge context provider"
        title: "zkVerify Documentation"
        type: server
        dateAdded: "2025-01-01T00:00:00Z"
        image: zkverify-mcp-server:latest
        tools:
            - name: fetch_zkverify_docs
        resources:
            - name: "zkverify://overview"
            - name: "zkverify://architecture"
            - name: "zkverify://sdk"
            - name: "zkverify://tutorials"
            - name: "zkverify://api"
            - name: "zkverify://faq"
            - name: "zkverify://contracts"
            - name: "zkverify://proofs"
            - name: "zkverify://vflow"
```

3. Update your **registry.yaml**:

```yaml
registry:
    zkverify:
        ref: ""
```

4. Update **Claude Desktop config** (`claude_desktop_config.json`):

```json
{
	"mcpServers": {
		"zkverify": {
			"command": "docker",
			"args": [
				"run",
				"-i",
				"--rm",
				"-v",
				"/Users/YOUR_USERNAME/.docker/mcp:/mcp",
				"zkverify-mcp-server:latest",
				"--catalog=/mcp/catalogs/custom.yaml",
				"--registry=/mcp/registry.yaml",
				"--transport=stdio"
			]
		}
	}
}
```

> Replace `/Users/YOUR_USERNAME` with your macOS home directory.

5. Restart Claude Desktop.
6. Verify the MCP server and tool appear in the **MCP Toolkit → Servers** menu.

---

## **B. Local Python Setup (Cursor)**

1. Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate    # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make the server script executable (macOS/Linux):

```bash
chmod +x run_zkverify.sh
```

4. Configure Cursor to use the server:

```json
{
	"mcpServers": {
		"zkverify": {
			"command": "/path/to/zkverify-mcp/run_zkverify.sh",
			"args": [],
			"env": {}
		}
	}
}
```

> Replace `/path/to/zkverify-mcp/` with your actual path.

5. Start Cursor, and the `zkverify` MCP server should be available.

---

## **Testing the Server**

-   **Docker (Claude Desktop)**:

```bash
docker run -i --rm -v ~/.docker/mcp:/mcp zkverify-mcp-server:latest \
  --catalog=/mcp/catalogs/custom.yaml \
  --registry=/mcp/registry.yaml \
  --transport=stdio
```

-   **Claude tool test**:

```
@zkverify fetch_zkverify_docs overview
@zkverify fetch_zkverify_docs architecture
```

-   **Cursor tool test**:

```javascript
// @zkverify fetch_zkverify_docs overview
```

---

## **Troubleshooting**

-   **JSON parse error in Claude** → Ensure all `print()` statements are removed; logs should use `logger` with `stream=sys.stderr`.
-   **Server not detected** → Check `registry.yaml` and `claude_desktop_config.json` paths.
-   **Docker issues** → Verify image is built:

```bash
docker images | grep zkverify-mcp-server
```

-   **Cursor issues** → Ensure Python virtual environment is active and `run_zkverify.sh` is executable.

---

## **Contributing**

-   Add new resources using `@mcp.resource()` in `zkverify_server.py`.
-   Add new tools using `@mcp.tool()`.
-   Use **logger** for all debug/info output (stderr only).
-   Test locally before pushing changes.

---

## **License**

MIT License. Free to use and modify.

