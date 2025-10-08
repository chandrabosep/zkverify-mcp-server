# zkVerify MCP Server

**Comprehensive MCP server for zkVerify documentation, resources, and tools with hybrid live/cached data fetching.**

> **Created by [Chandra Bose](https://github.com/chandrabosep)**

This project provides a **ready-to-use MCP server** for developers to integrate zkVerify resources into AI assistants such as **Claude Desktop** and **Cursor**, enabling access to documentation, tutorials, SDK examples, and live fetching tools with intelligent fallback to cached data.

---

## **Features**

### **Resources (11 total)**
Pre-configured resources with hybrid live/cached data:
- `zkverify://overview` - Platform overview and key features
- `zkverify://contract-addresses` - Contract addresses for all networks
- `zkverify://supported-proofs` - Supported proof systems and capabilities
- `zkverify://important-links` - Important links and external resources
- `zkverify://tutorials` - Step-by-step tutorials
- `zkverify://explorations` - Advanced use cases and explorations
- `zkverify://testnet` - Testnet information and getting started
- `zkverify://architecture` - Detailed architecture documentation
- `zkverify://sdk` - SDK installation and usage
- `zkverify://relayer-mainnet` - Relayer API documentation (Mainnet)
- `zkverify://relayer-testnet` - Relayer API documentation (Testnet)

### **Tools (12 total)**
Interactive tools with intelligent data fetching:
- `fetch_zkverify_docs` - Fetch live documentation from specific sections
- `get_proof_system_info` - Detailed proof system information (Groth16, Fflonk, RISC Zero, etc.)
- `get_network_info` - Network details, RPC endpoints, explorer, and faucet
- `generate_sdk_code` - TypeScript code examples for common operations
- `calculate_verification_cost` - Cost comparison across blockchains
- `get_tutorial_info` - Detailed tutorial information and guides
- `get_exploration_info` - Advanced exploration details
- `get_testnet_phases` - Incentivized testnet phases and challenges
- `get_node_operator_guide` - Node operator setup and guides
- `get_verifier_guide` - Custom verifier integration guides
- `get_relayer_api_info` - Relayer API documentation and endpoints
- `generate_relayer_example` - Relayer API code examples

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

### **Prerequisites**

Before setting up the zkVerify MCP server for Claude Desktop, ensure you have:

1. **Docker Desktop installed and running**
   - Download from: https://www.docker.com/products/docker-desktop/

2. **Docker MCP Toolkit enabled**
   - Follow the official guide: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/
   - The MCP Toolkit must be enabled in Docker Desktop settings
   - Verify by running: `docker mcp --version`

> ⚠️ **Important**: Without Docker running and MCP Toolkit enabled, the server will not work with Claude Desktop.

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
            - name: get_tutorial_info
            - name: get_exploration_info
            - name: get_testnet_phases
            - name: get_node_operator_guide
            - name: get_verifier_guide
            - name: get_relayer_api_info
            - name: generate_relayer_example
        resources:
            - name: "zkverify://overview"
            - name: "zkverify://contract-addresses"
            - name: "zkverify://supported-proofs"
            - name: "zkverify://important-links"
            - name: "zkverify://tutorials"
            - name: "zkverify://explorations"
            - name: "zkverify://testnet"
            - name: "zkverify://architecture"
            - name: "zkverify://sdk"
            - name: "zkverify://relayer-mainnet"
            - name: "zkverify://relayer-testnet"
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

Show me the contract addresses for zkVerify

How do I set up a node operator?

What are the testnet phases and challenges?

Generate a relayer API example for submitting proofs
```

Or use tools explicitly:

```
@zkverify fetch_zkverify_docs overview
@zkverify get_proof_system_info groth16
@zkverify get_network_info testnet
@zkverify generate_sdk_code submit_proof
@zkverify calculate_verification_cost groth16 100
@zkverify get_tutorial_info nextjs-circom
@zkverify get_testnet_phases
@zkverify get_node_operator_guide docker
@zkverify generate_relayer_example submit-proof testnet
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

// Get tutorial information
// @zkverify get_tutorial_info typescript-example

// Generate relayer code
// @zkverify generate_relayer_example register-vk testnet

// Get node operator guide
// @zkverify get_node_operator_guide docker
```

---

## **Testing the Server**

### **Claude Integration Test**

In Claude Desktop, ask:

```
@zkverify What proof systems does zkVerify support?
@zkverify Show me the testnet RPC endpoints
@zkverify Generate code to connect to zkVerify
@zkverify Get contract addresses for zkVerify
@zkverify Show me node operator guides
@zkverify Get testnet phases information
```

### **Cursor Integration Test**

In Cursor, use:

```typescript
// @zkverify generate_sdk_code submit_proof
// @zkverify calculate_verification_cost groth16 10
// @zkverify get_tutorial_info nextjs-circom
// @zkverify generate_relayer_example submit-proof testnet
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
        logger.info("Successfully fetched live new topic")
        return f"""# New Topic (Live from Docs)

{content[:4000]}

Source: https://docs.zkverify.io/new-topic
Last fetched: Live data"""
    
    # Fallback
    logger.warning("Failed to fetch new topic from docs")
    return """❌ Unable to fetch new topic from documentation.

Please visit https://docs.zkverify.io/new-topic directly for the latest information."""
```

Update `custom.yaml` (add to the resources list):

```yaml
resources:
    - name: "zkverify://overview"
    # ... existing resources ...
    - name: "zkverify://new-topic"
```

### **Adding New Tools**

Add to `zkverify_server.py`:

```python
@mcp.tool()
async def new_tool(param: str = "") -> str:
    """Single-line description of what this tool does."""
    logger.info(f"Executing new_tool with param: {param}")
    
    try:
        # Validate parameter
        if not param:
            return "❌ Error: Please provide a parameter"
        
        # Try live fetch
        result = await fetch_live_data(param)
        if result:
            return f"✅ {result}"
        
        # Fallback
        return fallback_data(param)
        
    except Exception as e:
        logger.error(f"Error in new_tool: {e}")
        return f"❌ Error: {str(e)}"
```

Update `custom.yaml` (add to the tools list):

```yaml
tools:
    - name: fetch_zkverify_docs
    # ... existing tools ...
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

- **zkVerify Official Docs**: https://docs.zkverify.io/
- **zkVerify GitHub**: https://github.com/zkverify
- **zkVerify Discord**: https://discord.gg/zkverify
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Claude Desktop**: https://claude.ai/
- **Cursor**: https://cursor.sh/

---

## **License**

MIT License. Free to use and modify.

---

## **Author**

Created by [Chandra Bose](https://github.com/chandrabosep)

For questions, issues, or suggestions, please open an issue on GitHub.

---

## **Changelog**

### **v2.1.0** - Complete Feature Set
- ✨ **11 resources** covering all zkVerify documentation
- ✨ **12 interactive tools** for comprehensive zkVerify integration
- ✨ Added contract addresses resource
- ✨ Added supported proofs resource
- ✨ Added important links resource
- ✨ Added relayer API resources (mainnet & testnet)
- ✨ Added tutorial info tool
- ✨ Added exploration info tool
- ✨ Added testnet phases tool
- ✨ Added node operator guide tool
- ✨ Added verifier integration guide tool
- ✨ Added relayer API info tool
- ✨ Added relayer example generation tool

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