# zkVerify MCP Server

**Comprehensive MCP server for zkVerify documentation, resources, and tools with hybrid live/cached data fetching.**

> **Created by [Chandra Bose](https://github.com/chandrabosep)**

This project provides a **ready-to-use MCP server** for developers to integrate zkVerify resources into AI assistants such as **Claude Desktop** and **Cursor**, enabling access to documentation, tutorials, SDK examples, and live fetching tools with intelligent fallback to cached data.

---

## **Features**

### **Resources (9 total)**
Pre-configured resources with hybrid live/cached data:
- `zkverify://overview` - Platform overview and key features
- `zkverify://architecture` - Detailed architecture documentation
- `zkverify://sdk` - SDK installation and usage
- `zkverify://tutorials` - Step-by-step tutorials
- `zkverify://api` - API reference
- `zkverify://faq` - Frequently asked questions
- `zkverify://contracts` - Smart contract integration
- `zkverify://proofs` - Proof system details
- `zkverify://vflow` - Verification workflow

### **Tools (5 total)**
Interactive tools with intelligent data fetching:
- `fetch_zkverify_docs` - Fetch live documentation from specific sections
- `get_proof_system_info` - Detailed proof system information (Groth16, Fflonk, RISC Zero)
- `get_network_info` - Network details, RPC endpoints, explorer, and faucet
- `generate_sdk_code` - TypeScript code examples for common operations
- `calculate_verification_cost` - Cost comparison across blockchains


### **Compatibility**
- ✅ Compatible with **Claude Desktop (Docker)**
- ✅ Compatible with **Cursor (local Python)**
- ✅ Easy setup and configuration

---

## **Project Structure**

```
zkverify-mcp/
├── Dockerfile             # Docker build file
├── requirements.txt       # Python dependencies
├── zkverify_server.py     # MCP server implementation (hybrid mode)
├── run_zkverify.sh        # Shell script for Cursor
├── README.md              # This file
├── CLAUDE.md              # Claude-specific instructions
└── .gitignore             # Git ignore file
```

> **Note:** `venv/` is not included in the repo. Developers can create their own virtual environment for local Python setup.

---

## **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/chandrabosep/zkverify-mcp-server.git
cd zkverify-mcp-server
```

---

## **A. Docker Setup (Claude Desktop)**

### **Step 1: Build the Docker Image**

```bash
docker build -t zkverify-mcp-server .
```

### **Step 2: Create Custom Catalog**

```bash
mkdir -p ~/.docker/mcp/catalogs
nano ~/.docker/mcp/catalogs/custom.yaml
```

Add this configuration:

```yaml
version: 2
name: custom
displayName: Custom MCP Servers
registry:
    zkverify:
        description: "Comprehensive zkVerify documentation and knowledge context provider with hybrid live/cached data"
        title: "zkVerify Documentation"
        type: server
        dateAdded: "2025-01-01T00:00:00Z"
        image: zkverify-mcp-server:latest
        ref: ""
        readme: ""
        toolsUrl: ""
        source: "https://github.com/chandrabosep/zkverify-mcp-server"
        upstream: ""
        icon: ""
        tools:
            - name: fetch_zkverify_docs
            - name: get_proof_system_info
            - name: get_network_info
            - name: generate_sdk_code
            - name: calculate_verification_cost
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
        metadata:
            category: integration
            tags:
                - blockchain
                - zero-knowledge
                - zkverify
                - documentation
            license: MIT
            owner: chandrabosep
```

### **Step 3: Update Registry**

Edit `~/.docker/mcp/registry.yaml` and add under the `registry:` key:

```yaml
registry:
    # ... existing servers ...
    zkverify:
        ref: ""
```

**IMPORTANT**: Make sure this is under the `registry:` key, not at root level.

### **Step 4: Configure Claude Desktop**

Find your Claude Desktop config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

Edit the file:

```json
{
    "mcpServers": {
        "mcp-toolkit-gateway": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "-v", "/var/run/docker.sock:/var/run/docker.sock",
                "-v", "/Users/YOUR_USERNAME/.docker/mcp:/mcp",
                "docker/mcp-gateway",
                "--catalog=/mcp/catalogs/docker-mcp.yaml",
                "--catalog=/mcp/catalogs/custom.yaml",
                "--config=/mcp/config.yaml",
                "--registry=/mcp/registry.yaml",
                "--tools-config=/mcp/tools.yaml",
                "--transport=stdio"
            ]
        }
    }
}
```

> **Replace `/Users/YOUR_USERNAME`** with your actual home directory:
> - macOS: `/Users/yourusername`
> - Windows: `C:\\Users\\yourusername` (use double backslashes)
> - Linux: `/home/yourusername`

### **Step 5: Restart Claude Desktop**

1. Quit Claude Desktop completely
2. Start Claude Desktop again
3. Your zkVerify MCP server should now be available!

### **Step 6: Verify Installation**

```bash
# Check if server appears in list
docker mcp server list

# View server logs
docker logs [container_name]
```

---

## **B. Local Python Setup (Cursor)**

### **Step 1: Create Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate    # Windows
```

### **Step 2: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 3: Make Script Executable (macOS/Linux)**

```bash
chmod +x run_zkverify.sh
```

### **Step 4: Configure Cursor**

Open Cursor settings and add to MCP servers configuration:

```json
{
    "mcpServers": {
        "zkverify": {
            "command": "/absolute/path/to/zkverify-mcp/run_zkverify.sh",
            "args": [],
            "env": {}
        }
    }
}
```

> Replace `/absolute/path/to/zkverify-mcp/` with your actual project path.

**Alternative (Direct Python)**:

```json
{
    "mcpServers": {
        "zkverify": {
            "command": "/absolute/path/to/venv/bin/python",
            "args": ["/absolute/path/to/zkverify_server.py"],
            "env": {}
        }
    }
}
```

### **Step 5: Restart Cursor**

The zkVerify MCP server should now be available in Cursor.

---

## **Usage Examples**

### **In Claude Desktop**

Ask Claude naturally:

```
Tell me about zkVerify's architecture

What proof systems does zkVerify support?

Show me how to submit a Groth16 proof using the SDK

Calculate the cost savings for 100 proofs on zkVerify vs Ethereum

What are the zkVerify testnet RPC endpoints?
```

Or use tools explicitly:

```
@zkverify fetch_zkverify_docs overview
@zkverify get_proof_system_info groth16
@zkverify get_network_info testnet
@zkverify generate_sdk_code submit_proof
@zkverify calculate_verification_cost groth16 100
```

### **In Cursor**

Use the MCP tools in your code context:

```typescript
// Ask about zkVerify integration
// @zkverify generate_sdk_code connect

// Get network information
// @zkverify get_network_info testnet

// Compare costs
// @zkverify calculate_verification_cost fflonk 50
```

---

## **Testing the Server**

### **Claude Integration Test**

In Claude Desktop, ask:

```
@zkverify What proof systems does zkVerify support?
@zkverify Show me the testnet RPC endpoints
@zkverify Generate code to connect to zkVerify
```

### **Cursor Integration Test**

In Cursor, use:

```typescript
// @zkverify generate_sdk_code submit_proof
// @zkverify calculate_verification_cost groth16 10
```

---

## **Troubleshooting**

### **Common Issues**

#### **Tools Not Appearing in Claude**

1. Verify Docker image is built:
   ```bash
   docker images | grep zkverify-mcp-server
   ```

2. Check catalog file exists:
   ```bash
   cat ~/.docker/mcp/catalogs/custom.yaml
   ```

3. Verify registry entry:
   ```bash
   cat ~/.docker/mcp/registry.yaml | grep zkverify
   ```

4. Check Claude config includes custom catalog:
   ```bash
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

5. Restart Claude Desktop completely

---

## **Development**

### **Adding New Resources**

Add to `zkverify_server.py`:

```python
@mcp.resource("zkverify://new-topic")
async def get_new_topic() -> str:
    """Description of new topic."""
    
    # Try live fetch
    content = await fetch_from_docs("https://docs.zkverify.io/new-topic")
    
    if content:
        return f"# New Topic (Live)\n\n{content}"
    
    # Fallback
    return """# New Topic (Cached)
    
    [Your cached content here]
    
    ⚠️ Using cached data."""
```

Update `custom.yaml`:

```yaml
resources:
    - name: "zkverify://new-topic"
```

### **Adding New Tools**

Add to `zkverify_server.py`:

```python
@mcp.tool()
async def new_tool(param: str = "") -> str:
    """Single-line description of what this tool does."""
    logger.info(f"Executing new_tool with: {param}")
    
    try:
        # Try live fetch
        result = await fetch_live_data(param)
        if result:
            return f"✅ {result}"
        
        # Fallback
        return fallback_data(param)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"❌ Error: {str(e)}"
```

Update `custom.yaml`:

```yaml
tools:
    - name: new_tool
```

### **Testing Changes**

1. Rebuild Docker image:
   ```bash
   docker build -t zkverify-mcp-server .
   ```

2. Test locally:
   ```bash
   python zkverify_server.py
   ```

3. Test with Claude Desktop (restart required)

4. Check logs for errors:
   ```bash
   docker logs [container_name]
   ```

### **Code Guidelines**

- ✅ Use single-line docstrings only
- ✅ Use `logger` for all output (stderr)
- ✅ Never use `print()` statements
- ✅ Default parameters to empty strings (`param: str = ""`)
- ✅ Always handle exceptions
- ✅ Return formatted strings from tools
- ✅ Try live fetch first, fallback to cached
- ✅ Indicate data source in responses

---

## **Dependencies**

From `requirements.txt`:

```
mcp[cli]>=1.2.0
httpx
beautifulsoup4
lxml
```

---

## **Contributing**

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly (both Docker and local)
5. Submit a pull request

### **Contribution Guidelines**

- Follow existing code style
- Add tests for new features
- Update README for new tools/resources
- Ensure hybrid data fetching works
- Check logs are going to stderr only
- No `print()` statements

---

## **Resources**

- **Docker MCP Toolkit**: [Docker MCP Toolkit Documentation](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/)
- **zkVerify Official Docs**: https://docs.zkverify.io/
- **MCP Protocol**: https://modelcontextprotocol.io/

---

## **License**

MIT License. Free to use and modify.

---

## **Author**

Created by [Chandra Bose](https://github.com/chandrabosep)

For questions, issues, or suggestions, please open an issue on GitHub.

---

## **Changelog**

### **v2.0.0** - Hybrid Data Mode
- ✨ Added hybrid live/cached data fetching
- ✨ Added 4 new tools (previously only 1)
- ✨ Intelligent fallback mechanism
- ✨ Transparent data source indicators
- ✨ Enhanced error handling
- ✨ Improved documentation coverage

### **v1.0.0** - Initial Release
- ✅ 9 resources for zkVerify documentation
- ✅ 1 tool for live doc fetching
- ✅ Docker and local Python support
- ✅ Claude Desktop and Cursor integration

---

**⭐ If this project helps you, please star it on GitHub!**