# zkVerify MCP Server

A Model Context Protocol (MCP) server that provides comprehensive zkVerify documentation and knowledge context to AI assistants.

## Purpose

This MCP server provides a secure interface for AI assistants to access zkVerify's complete documentation, enabling them to answer questions about zkVerify, explain APIs and SDKs, assist with integration, and help developers build zero-knowledge proof applications.

## Features

### Current Implementation

#### Resources (Context Providers)
- **`zkverify://overview`** - Complete platform overview and ecosystem information
- **`zkverify://architecture`** - Detailed architecture documentation including core components
- **`zkverify://sdk`** - SDK documentation with code examples for TypeScript/JavaScript
- **`zkverify://tutorials`** - Step-by-step tutorials for common integration scenarios
- **`zkverify://api`** - Complete API reference for REST, WebSocket, and RPC methods
- **`zkverify://faq`** - Frequently asked questions covering general, technical, and economic topics
- **`zkverify://contracts`** - Smart contract addresses and integration examples
- **`zkverify://proofs`** - Details about supported proof systems (Groth16, Fflonk, RISC Zero)
- **`zkverify://vflow`** - VFlow verification workflow engine documentation

#### Tools
- **`fetch_zkverify_docs`** - Fetch live documentation from zkVerify docs website

## Prerequisites

- Docker Desktop with MCP Toolkit enabled
- Docker MCP CLI plugin (`docker mcp` command)
- Internet connection (for fetching live documentation)

## Installation

See the step-by-step instructions provided with the files.

## Usage Examples

In Claude Desktop, you can ask:

### General Questions
- "What is zkVerify and how does it work?"
- "Explain the zkVerify architecture"
- "What proof systems does zkVerify support?"
- "How much does zkVerify verification cost?"

### Developer Questions
- "How do I submit a Groth16 proof to zkVerify?"
- "Show me how to integrate zkVerify with my Next.js app"
- "What's the TypeScript code to verify a proof?"
- "How do I set up batch proof submission?"

### Integration Questions
- "What are the zkVerify testnet contract addresses?"
- "How do I integrate zkVerify with my Solidity smart contract?"
- "Show me the zkVerify SDK installation steps"
- "What's the API endpoint for proof submission?"

### Technical Support
- "How do I run a zkVerify validator node?"
- "What are the system requirements for running a node?"
- "How do I get testnet tokens?"
- "Where can I find zkVerify support?"

### Live Documentation
- "Fetch the latest zkVerify architecture documentation"
- "Get current developer guides from zkVerify docs"
- "Show me the latest testnet information"

## Architecture

```
Claude Desktop → MCP Gateway → zkVerify MCP Server → Resources/Tools
                                        ↓
                              zkVerify Documentation
                              (Embedded & Live Fetch)
```

## Development

### Local Testing

```bash
# Run directly (without Docker)
python zkverify_server.py

# Test MCP protocol
echo '{"jsonrpc":"2.0","method":"resources/list","id":1}' | python zkverify_server.py

# Test tool execution
echo '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"fetch_zkverify_docs","arguments":{"section":"overview"}},"id":1}' | python zkverify_server.py
```

### Adding New Resources

1. Add a new resource function to `zkverify_server.py`:
```python
@mcp.resource("zkverify://new_topic")
async def get_new_topic() -> str:
    return """Documentation content here"""
```

2. Update the catalog entry with the new resource
3. Rebuild the Docker image

### Updating Documentation

The server provides both embedded documentation (for offline use) and live fetching capabilities. To update embedded docs:

1. Edit the resource functions in `zkverify_server.py`
2. Rebuild the Docker image
3. Restart the server

## Troubleshooting

### Server Not Starting
- Check Docker logs: `docker logs [container_name]`
- Verify Python dependencies installed correctly
- Ensure port is not in use

### Resources Not Appearing
- Verify server is running: `docker mcp server list`
- Check Claude Desktop config includes the server
- Restart Claude Desktop

### Live Fetch Not Working
- Check internet connection
- Verify zkVerify docs website is accessible
- Check for rate limiting

### No Responses in Claude
- Ensure MCP Gateway is running
- Check catalog configuration
- Verify custom.yaml is properly formatted

## Security Considerations

- Server runs as non-root user in Docker
- No authentication required (public documentation only)
- Optional API key support can be added for future features
- All data is read-only
- No sensitive information is stored or transmitted

## Resource Details

### Overview Resource
Provides high-level information about zkVerify, including key features, use cases, and getting started guide.

### Architecture Resource
Details the core architecture including mainchain, proof submission interface, verification pallets, and settlement layer.

### SDK Resource
Complete documentation for zkverifyjs SDK with code examples for initialization, proof submission, and status queries.

### Tutorials Resource
Step-by-step guides for common tasks like submitting first proof, Next.js integration, and running validator nodes.

### API Resource
Full API reference including REST endpoints, WebSocket subscriptions, RPC methods, and error codes.

### FAQ Resource
Comprehensive FAQ covering general, technical, developer, and economic questions.

### Contracts Resource
Smart contract addresses for testnet/mainnet bridges and integration examples.

### Proofs Resource
Detailed information about supported proof systems including Groth16, Fflonk, and RISC Zero.

### VFlow Resource
Documentation for the VFlow verification workflow engine including routing, aggregation, and optimization.

## License

MIT License

## Support

- zkVerify Documentation: https://docs.zkverify.io/
- zkVerify Discord: https://discord.gg/zkverify
- zkVerify Telegram: https://t.me/zkverify
- GitHub Issues: https://github.com/zkverify/zkverify-docs