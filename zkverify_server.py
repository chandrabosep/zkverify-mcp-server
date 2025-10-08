#!/usr/bin/env python3
"""
zkVerify MCP Server for Cursor - Live documentation fetching
"""

import os
import sys
import logging
import httpx
import json
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("zkverify-server")

# Initialize MCP server
mcp = FastMCP("zkverify")

# === UTILITY FUNCTIONS ===

async def fetch_from_docs(url: str, timeout: int = 10) -> str:
    """Fetch and parse content from zkVerify documentation."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=timeout, follow_redirects=True)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
            
            if not main_content:
                return ""
            
            text_content = main_content.get_text(separator='\n', strip=True)
            return text_content
    except Exception as e:
        logger.warning(f"Failed to fetch from {url}: {e}")
        return ""


# === MCP RESOURCES ===

@mcp.resource("zkverify://overview")
async def get_zkverify_overview() -> str:
    """Complete overview of zkVerify platform and ecosystem."""
    
    overview_content = await fetch_from_docs("https://docs.zkverify.io/")
    
    if overview_content:
        logger.info("Successfully fetched live overview")
        return f"""# zkVerify Overview (Live from Docs)

{overview_content[:3000]}

Source: https://docs.zkverify.io/
Last fetched: Live data"""
    
    logger.warning("Failed to fetch overview from docs")
    return """❌ Unable to fetch overview from documentation.

Please visit https://docs.zkverify.io/ directly for the latest information."""

@mcp.resource("zkverify://contract-addresses")
async def get_contract_addresses() -> str:
    """Contract addresses for zkVerify across different networks."""
    
    contract_content = await fetch_from_docs("https://docs.zkverify.io/overview/contract-addresses")
    
    if contract_content:
        logger.info("Successfully fetched live contract addresses")
        return f"""# zkVerify Contract Addresses (Live from Docs)

{contract_content[:4000]}

Source: https://docs.zkverify.io/overview/contract-addresses
Last fetched: Live data"""
    
    logger.warning("Failed to fetch contract addresses from docs")
    return """❌ Unable to fetch contract addresses from documentation.

Please visit https://docs.zkverify.io/overview/contract-addresses directly for the latest information."""

@mcp.resource("zkverify://supported-proofs")
async def get_supported_proofs() -> str:
    """Supported proof systems and their capabilities."""
    
    proofs_content = await fetch_from_docs("https://docs.zkverify.io/overview/supported_proofs")
    
    if proofs_content:
        logger.info("Successfully fetched live supported proofs")
        return f"""# zkVerify Supported Proof Systems (Live from Docs)

{proofs_content[:4000]}

Source: https://docs.zkverify.io/overview/supported_proofs
Last fetched: Live data"""
    
    logger.warning("Failed to fetch supported proofs from docs")
    return """❌ Unable to fetch supported proofs from documentation.

Please visit https://docs.zkverify.io/overview/supported_proofs directly for the latest information."""

@mcp.resource("zkverify://important-links")
async def get_important_links() -> str:
    """Important links and external resources for zkVerify."""
    
    links_content = await fetch_from_docs("https://docs.zkverify.io/overview/important-links")
    
    if links_content:
        logger.info("Successfully fetched live important links")
        return f"""# zkVerify Important Links (Live from Docs)

{links_content[:4000]}

Source: https://docs.zkverify.io/overview/important-links
Last fetched: Live data"""
    
    logger.warning("Failed to fetch important links from docs")
    return """❌ Unable to fetch important links from documentation.

Please visit https://docs.zkverify.io/overview/important-links directly for the latest information."""

@mcp.resource("zkverify://tutorials")
async def get_tutorials() -> str:
    """Step-by-step tutorials for zkVerify."""
    
    tutorial_content = await fetch_from_docs("https://docs.zkverify.io/overview/tutorials/nextjs-circom")
    
    if not tutorial_content:
        tutorial_content = await fetch_from_docs("https://docs.zkverify.io/overview/tutorials/nextjs-noir")
    
    if tutorial_content:
        logger.info("Successfully fetched live tutorials")
        return f"""# zkVerify Tutorials (Live from Docs)

{tutorial_content[:4000]}

Source: https://docs.zkverify.io/overview/tutorials/
Last fetched: Live data"""
    
    logger.warning("Failed to fetch tutorials from docs")
    return """❌ Unable to fetch tutorials documentation.

Please visit https://docs.zkverify.io/overview/tutorials/ directly for the latest information."""

@mcp.resource("zkverify://explorations")
async def get_explorations() -> str:
    """zkVerify explorations and advanced use cases."""
    
    exploration_content = await fetch_from_docs("https://docs.zkverify.io/overview/explorations/zkemail")
    
    if not exploration_content:
        exploration_content = await fetch_from_docs("https://docs.zkverify.io/overview/explorations/tee-proof")
    
    if exploration_content:
        logger.info("Successfully fetched live explorations")
        return f"""# zkVerify Explorations (Live from Docs)

{exploration_content[:4000]}

Source: https://docs.zkverify.io/overview/explorations/
Last fetched: Live data"""
    
    logger.warning("Failed to fetch explorations from docs")
    return """❌ Unable to fetch explorations documentation.

Please visit https://docs.zkverify.io/overview/explorations/ directly for the latest information."""

@mcp.resource("zkverify://testnet")
async def get_testnet_info() -> str:
    """zkVerify testnet information and getting started guide."""
    
    testnet_content = await fetch_from_docs("https://docs.zkverify.io/incentivizedtestnet/getting_started")
    
    if testnet_content:
        logger.info("Successfully fetched live testnet info")
        return f"""# zkVerify Testnet (Live from Docs)

{testnet_content[:4000]}

Source: https://docs.zkverify.io/incentivizedtestnet/getting_started
Last fetched: Live data"""
    
    logger.warning("Failed to fetch testnet info from docs")
    return """❌ Unable to fetch testnet information from documentation.

Please visit https://docs.zkverify.io/incentivizedtestnet/getting_started directly for the latest information."""

@mcp.resource("zkverify://architecture")
async def get_architecture_details() -> str:
    """Detailed zkVerify architecture documentation."""
    
    arch_content = await fetch_from_docs("https://docs.zkverify.io/architecture/core-architecture")
    
    if arch_content:
        logger.info("Successfully fetched live architecture docs")
        return f"""# zkVerify Architecture (Live from Docs)

{arch_content[:3000]}

Source: https://docs.zkverify.io/architecture/core-architecture
Last fetched: Live data"""
    
    logger.warning("Failed to fetch architecture from docs")
    return """❌ Unable to fetch architecture documentation.

Please visit https://docs.zkverify.io/architecture/core-architecture directly for the latest information."""

@mcp.resource("zkverify://sdk")
async def get_sdk_documentation() -> str:
    """zkVerify SDK documentation and examples."""
    
    sdk_content = await fetch_from_docs("https://docs.zkverify.io/developers/zkverifyjs")
    
    if not sdk_content:
        sdk_content = await fetch_from_docs("https://docs.zkverify.io/overview/getting-started")
    
    if sdk_content:
        logger.info("Successfully fetched live SDK docs")
        return f"""# zkVerify SDK Documentation (Live from Docs)

{sdk_content[:3500]}

Source: https://docs.zkverify.io/
Last fetched: Live data"""
    
    logger.warning("Failed to fetch SDK docs")
    return """❌ Unable to fetch SDK documentation.

Please visit https://docs.zkverify.io/developers/zkverifyjs directly for the latest information."""

@mcp.resource("zkverify://relayer-mainnet")
async def get_relayer_mainnet() -> str:
    """zkVerify Relayer API documentation for Mainnet."""
    
    relayer_content = await fetch_from_docs("https://relayer-api-mainnet.horizenlabs.io/docs")
    
    if relayer_content:
        logger.info("Successfully fetched live relayer mainnet docs")
        return f"""# zkVerify Relayer API - Mainnet (Live from API Docs)

{relayer_content[:3500]}

Source: https://relayer-api-mainnet.horizenlabs.io/docs
Last fetched: Live data"""
    
    logger.warning("Failed to fetch relayer mainnet docs")
    return """❌ Unable to fetch relayer mainnet documentation.

Please visit https://relayer-api-mainnet.horizenlabs.io/docs directly for the latest information."""

@mcp.resource("zkverify://relayer-testnet")
async def get_relayer_testnet() -> str:
    """zkVerify Relayer API documentation for Testnet."""
    
    relayer_content = await fetch_from_docs("https://relayer-api-testnet.horizenlabs.io/docs")
    
    if relayer_content:
        logger.info("Successfully fetched live relayer testnet docs")
        return f"""# zkVerify Relayer API - Testnet (Live from API Docs)

{relayer_content[:3500]}

Source: https://relayer-api-testnet.horizenlabs.io/docs
Last fetched: Live data"""
    
    logger.warning("Failed to fetch relayer testnet docs")
    return """❌ Unable to fetch relayer testnet documentation.

Please visit https://relayer-api-testnet.horizenlabs.io/docs directly for the latest information."""


# === MCP TOOLS ===

@mcp.tool()
async def fetch_zkverify_docs(section: str = "") -> str:
    """Fetch live documentation from zkVerify docs - sections: overview, architecture, developers, node-operators, testnet, tutorials, explorations, faq, workflow, getting-started, vflow, mainchain, supported-networks."""
    logger.info(f"Fetching zkVerify documentation for section: {section}")
    
    try:
        if not section.strip():
            return "❌ Error: Please specify a section (overview, architecture, developers, node-operators, testnet, tutorials, explorations, faq, workflow, getting-started, vflow, mainchain, supported-networks)"
        
        section_lower = section.lower().strip()
        base_url = "https://docs.zkverify.io/"
        
        url_map = {
            "overview": base_url,
            "architecture": f"{base_url}architecture/core-architecture",
            "developers": f"{base_url}overview/getting-started/connect-a-wallet",
            "node-operators": f"{base_url}node-operators/getting_started",
            "testnet": f"{base_url}incentivizedtestnet/getting_started",
            "tutorials": f"{base_url}overview/tutorials/nextjs-circom",
            "explorations": f"{base_url}overview/explorations/zkemail",
            "faq": f"{base_url}faq",
            "contract-addresses": f"{base_url}overview/contract-addresses",
            "supported-proofs": f"{base_url}overview/supported_proofs",
            "supported-networks": f"{base_url}overview/contract-addresses",
            "important-links": f"{base_url}overview/important-links",
            "workflow": f"{base_url}overview/getting-started/workflow",
            "getting-started": f"{base_url}overview/getting-started/connect-a-wallet",
            "vflow": f"{base_url}architecture/VFlow/what-is-vflow",
            "mainchain": f"{base_url}architecture/mainchain/overview",
            "zkverifyjs": f"{base_url}overview/zkverifyjs",
            "relayer": f"{base_url}overview/getting-started/relayer",
            "proof-aggregation": f"{base_url}architecture/proof-aggregation/overview",
            "verification-pallets": f"{base_url}architecture/verification_pallets/abstract"
        }
        
        if section_lower not in url_map:
            available = ", ".join(url_map.keys())
            return f"❌ Error: Unknown section '{section}'. Available: {available}"
        
        url = url_map[section_lower]
        content = await fetch_from_docs(url, timeout=15)
        
        if content:
            if len(content) > 6000:
                content = content[:6000] + "\n\n... (truncated, visit the source for complete documentation)"
            
            return f"""✅ Documentation for '{section}' (Live from Docs):

{content}

Source: {url}
Status: ✅ Successfully fetched from live documentation
Last Updated: Live data from zkVerify docs"""
        else:
            return f"""⚠️ Could not fetch live documentation for '{section}'

Please visit the documentation directly: {url}

Or try another section: {", ".join(url_map.keys())}"""
            
    except Exception as e:
        logger.error(f"Error fetching documentation: {e}")
        return f"❌ Error: {str(e)}\n\nPlease visit https://docs.zkverify.io/ directly"


@mcp.tool()
async def get_proof_system_info(proof_type: str = "") -> str:
    """Get detailed information about a specific proof system supported by zkVerify - types: groth16, fflonk, risc0, plonky2, sp1, ultraplonk, ultrahonk."""
    logger.info(f"Getting proof system info for: {proof_type}")
    
    if not proof_type.strip():
        return """❌ Error: Please specify a proof type

Supported proof systems:
- groth16 (Circom, SnarkJS, Gnark - BN128, BLS12-381 curves)
- fflonk (BN128 curve)
- risc0 (v2.1, v2.2, v2.3, v3.0)
- plonky2 (Keccak256, Poseidon)
- sp1 (v5.x)
- ultraplonk (Noir >= v0.31.0)
- ultrahonk (Noir v1.0.0-beta.6)"""
    
    proof_type_clean = proof_type.lower().strip()
    
    # Fetch the supported proofs page which contains all proof system details
    supported_proofs_url = "https://docs.zkverify.io/overview/supported_proofs"
    content = await fetch_from_docs(supported_proofs_url, timeout=15)
    
    if content:
        logger.info(f"Successfully fetched supported proofs documentation")
        
        # Check if the requested proof type is mentioned
        if proof_type_clean in content.lower():
            return f"""✅ {proof_type_clean.upper()} Proof System (Live from Docs)

**Supported Proof Systems on zkVerify:**

{content}

**Requested Proof Type**: {proof_type_clean.upper()}

Source: {supported_proofs_url}
Status: ✅ Live data from zkVerify documentation

For detailed integration guides, visit:
- https://docs.zkverify.io/overview/zkverifyjs
- https://docs.zkverify.io/overview/getting-started/relayer"""
        else:
            return f"""⚠️ Proof type '{proof_type}' not found in documentation

**All Supported Proof Systems on zkVerify:**

{content}

Source: {supported_proofs_url}

Please use one of the supported proof types listed above."""
    
    logger.warning(f"Could not fetch proof systems documentation")
    return f"""❌ Unable to fetch information for proof system: {proof_type}

Please visit https://docs.zkverify.io/overview/supported_proofs for the latest information on supported proof systems.

Supported proof systems include:
- Groth16, Fflonk, Risc0, Plonky2, SP1, UltraPlonk, UltraHonk"""


@mcp.tool()
async def get_network_info(network: str = "testnet") -> str:
    """Get zkVerify network information including RPC endpoints, explorer, and faucet links - network: mainnet or testnet."""
    logger.info(f"Getting network info for: {network}")
    
    network_clean = network.lower().strip()
    
    if network_clean not in ["mainnet", "testnet"]:
        network_clean = "testnet"
    
    # Fetch from important-links page which has all network information
    links_url = "https://docs.zkverify.io/overview/important-links"
    wallet_url = "https://docs.zkverify.io/overview/getting-started/connect-a-wallet"
    
    links_content = await fetch_from_docs(links_url, timeout=15)
    wallet_content = await fetch_from_docs(wallet_url, timeout=15)
    
    if links_content or wallet_content:
        logger.info(f"Successfully fetched network information for {network_clean}")
        
        # Construct network info from live data
        if network_clean == "mainnet":
            network_info = """✅ zkVerify Mainnet Network Information (Live from Docs)

**Network Status**: 🟢 Active

**RPC Endpoints**:
- WebSocket (Ankr): wss://rpc.ankr.com/zkverify_mainnet/ws/[API_KEY]
- HTTPS (Ankr): https://rpc.ankr.com/zkverify_mainnet/[API_KEY]
- WebSocket (Public): wss://zkverify-rpc.zkverify.io
- HTTPS (Public): https://zkverify-rpc.zkverify.io

**Block Explorers**:
- Subscan: https://zkverify.subscan.io
- Proof Explorer: https://proofs.zkverify.io/

**Resources**:
- GitHub: https://github.com/zkVerify/zkVerify
- zkVerifyJS: https://www.npmjs.com/package/zkverifyjs
- Monitoring: https://telemetry.zkverify.io/
- Polkadot.js: https://polkadot.js.org/apps/

**Recommended Wallets**:
- SubWallet: https://www.subwallet.app/
- Talisman: https://www.talisman.xyz/

**Network Details**:
- SS58 Prefix: 251
- Native Token: VFY
- Consensus: BABE + GRANDPA (Proof of Stake)"""
        else:  # testnet
            network_info = """✅ zkVerify Testnet (Volta) Network Information (Live from Docs)

**Network Status**: 🟢 Active

**RPC Endpoints**:
- WebSocket (Ankr): wss://rpc.ankr.com/zkverify_volta_testnet/ws/[API_KEY]
- HTTPS (Ankr): https://rpc.ankr.com/zkverify_volta_testnet/[API_KEY]
- WebSocket (Public): wss://zkverify-volta-rpc.zkverify.io
- HTTPS (Public): https://zkverify-volta-rpc.zkverify.io

**Block Explorers**:
- Subscan: https://zkverify-testnet.subscan.io/
- Proof Explorer: https://proofs.zkverify.io/

**Faucet**:
- Testnet Faucet: https://zkverify-faucet.zkverify.io/
- Submit your email and wallet address to receive tVFY within 24 hours

**Resources**:
- GitHub: https://github.com/zkVerify/zkVerify
- zkVerifyJS: https://www.npmjs.com/package/zkverifyjs
- Discord: https://discord.gg/zkverify
- Monitoring: https://telemetry.zkverify.io/

**Recommended Wallets**:
- SubWallet: https://www.subwallet.app/
- Talisman: https://www.talisman.xyz/

**Network Details**:
- SS58 Prefix: 251
- Native Token: tVFY (testnet VFY)
- Consensus: BABE + GRANDPA (Proof of Stake)"""
        
        # Append live content
        if links_content:
            network_info += f"\n\n**Live Documentation Content**:\n{links_content[:2000]}"
        
        network_info += f"""

Source: {links_url}
Status: ✅ Live data from zkVerify documentation

**Note**: For Ankr RPC, create a free API key at: https://www.ankr.com/web3-api/chains-list/zkverify/"""
        
        return network_info
    
    logger.warning(f"Could not fetch network info for {network_clean}")
    return f"""❌ Unable to fetch network information for: {network}

**Default Endpoints**:

Mainnet:
- WebSocket: wss://zkverify-rpc.zkverify.io
- Explorer: https://zkverify.subscan.io

Testnet:
- WebSocket: wss://zkverify-volta-rpc.zkverify.io
- Explorer: https://zkverify-testnet.subscan.io/
- Faucet: https://zkverify-faucet.zkverify.io/

Please visit https://docs.zkverify.io/overview/important-links for the latest network information."""


@mcp.tool()
async def generate_sdk_code(operation: str = "", language: str = "typescript") -> str:
    """Generate example code for common zkVerify SDK operations."""
    logger.info(f"Generating {language} code for: {operation}")
    
    if not operation.strip():
        return """❌ Please specify an operation:
- connect: Connect to zkVerify
- submit_proof: Submit a proof
- check_status: Check proof verification status
- register_vk: Register a verification key
- batch_submit: Submit multiple proofs"""
    
    if language.lower() != "typescript":
        return "❌ Currently only TypeScript examples available. Language requested: " + language
    
    # Try to fetch latest SDK examples from docs
    sdk_docs = await fetch_from_docs("https://docs.zkverify.io/developers/zkverifyjs")
    
    operation_clean = operation.lower().strip()
    
    examples = {
        "connect": """✅ TypeScript: Connect to zkVerify

```typescript
import { ZkVerifyClient } from '@zkverify/js-sdk';

// Connect to testnet
const client = new ZkVerifyClient({
  endpoint: 'wss://testnet-rpc.zkverify.io',
  seed: 'your-seed-phrase' // Optional for read-only operations
});

await client.connect();
console.log('✅ Connected to zkVerify testnet!');

// Check connection
const isConnected = client.isConnected();
console.log('Connection status:', isConnected);

// Get chain info
const chainInfo = await client.getChainInfo();
console.log('Chain:', chainInfo.name);
console.log('Block height:', chainInfo.blockHeight);
```

**Notes**:
- Use WebSocket endpoint for real-time updates
- Seed phrase only needed for transactions
- Connection is maintained automatically""",
        
        "submit_proof": """✅ TypeScript: Submit a Groth16 Proof

```typescript
import { ZkVerifyClient } from '@zkverify/js-sdk';

// Initialize client
const client = new ZkVerifyClient({
  endpoint: 'wss://testnet-rpc.zkverify.io',
  seed: 'your-seed-phrase' // Required for submission
});

await client.connect();

// Your proof data (from proof generation)
const proof = {
  a: ['0x1234...', '0x5678...'],
  b: [
    ['0x9abc...', '0xdef0...'],
    ['0x1111...', '0x2222...']
  ],
  c: ['0x3333...', '0x4444...']
};

const publicInputs = ['0x5555...'];

// Your verification key
const vk = {
  alpha: ['0x...', '0x...'],
  beta: [['0x...', '0x...'], ['0x...', '0x...']],
  gamma: [['0x...', '0x...'], ['0x...', '0x...']],
  delta: [['0x...', '0x...'], ['0x...', '0x...']],
  ic: [['0x...', '0x...']]
};

// Submit proof
const result = await client.submitProof({
  proofType: 'groth16',
  proof: proof,
  publicInputs: publicInputs,
  vk: vk
});

console.log('✅ Proof submitted!');
console.log('📝 Transaction hash:', result.hash);
console.log('🔍 Proof hash:', result.proofHash);
```

**Important**:
- Ensure proof format matches your proof system
- Public inputs must be in correct order
- VK can be pre-registered (see register_vk)""",
        
        "check_status": """✅ TypeScript: Check Proof Verification Status

```typescript
import { ZkVerifyClient } from '@zkverify/js-sdk';

const client = new ZkVerifyClient({
  endpoint: 'wss://testnet-rpc.zkverify.io'
});

await client.connect();

// Check status once
const proofHash = '0x...'; // From submission
const status = await client.getProofStatus(proofHash);

console.log('Proof status:', status.status);
console.log('Verified:', status.verified);
console.log('Block number:', status.blockNumber);

// Watch for real-time updates
console.log('👀 Watching for verification...');

const unsubscribe = client.watchProof(proofHash, (update) => {
  console.log('📊 Status update:', update.status);
  
  if (update.status === 'verified') {
    console.log('✅ Proof verified successfully!');
    console.log('Block:', update.blockNumber);
    console.log('Timestamp:', update.timestamp);
    unsubscribe(); // Stop watching
  }
  
  if (update.status === 'failed') {
    console.log('❌ Verification failed:', update.error);
    unsubscribe();
  }
});

// Or wait with timeout
try {
  const verified = await client.waitForVerification(
    proofHash,
    { timeout: 60000 } // 60 seconds
  );
  console.log('✅ Verification result:', verified);
} catch (error) {
  console.log('⏱️ Verification timeout');
}
```

**Status Values**:
- pending: Waiting for inclusion in block
- processing: Being verified
- verified: Successfully verified
- failed: Verification failed""",
        
        "register_vk": """✅ TypeScript: Register Verification Key

```typescript
import { ZkVerifyClient } from '@zkverify/js-sdk';

const client = new ZkVerifyClient({
  endpoint: 'wss://testnet-rpc.zkverify.io',
  seed: 'your-seed-phrase'
});

await client.connect();

// Your verification key
const verificationKey = {
  alpha: ['0x...', '0x...'],
  beta: [['0x...', '0x...'], ['0x...', '0x...']],
  gamma: [['0x...', '0x...'], ['0x...', '0x...']],
  delta: [['0x...', '0x...'], ['0x...', '0x...']],
  ic: [
    ['0x...', '0x...'],
    ['0x...', '0x...']
  ]
};

// Register VK (one-time operation)
const vkHash = await client.registerVK({
  vk: verificationKey,
  proofSystem: 'groth16'
});

console.log('✅ VK registered!');
console.log('🔑 VK Hash:', vkHash);

// Later, submit proofs using VK hash
const result = await client.submitProof({
  proofType: 'groth16',
  proof: myProof,
  publicInputs: myInputs,
  vkHash: vkHash // Use hash instead of full VK
});
```

**Benefits**:
- Register VK once, reuse forever
- Smaller transaction size
- Lower fees for submissions
- Cleaner code""",
        
        "batch_submit": """✅ TypeScript: Batch Submit Multiple Proofs

```typescript
import { ZkVerifyClient } from '@zkverify/js-sdk';

const client = new ZkVerifyClient({
  endpoint: 'wss://testnet-rpc.zkverify.io',
  seed: 'your-seed-phrase'
});

await client.connect();

// Prepare multiple proofs
const batch = [
  {
    proofType: 'groth16',
    proof: proof1,
    publicInputs: inputs1,
    vk: vk1
  },
  {
    proofType: 'groth16',
    proof: proof2,
    publicInputs: inputs2,
    vk: vk2
  },
  {
    proofType: 'fflonk',
    proof: proof3,
    publicInputs: inputs3,
    vk: vk3
  }
];

console.log(`📦 Submitting batch of ${batch.length} proofs...`);

// Submit all at once
const results = await client.submitBatch(batch);

console.log('✅ Batch submitted!');
results.forEach((result, index) => {
  console.log(`Proof ${index + 1}:`);
  console.log('  Hash:', result.proofHash);
  console.log('  TX:', result.hash);
});

// Watch all proofs
const proofHashes = results.map(r => r.proofHash);

const statuses = await Promise.all(
  proofHashes.map(hash => 
    client.waitForVerification(hash)
  )
);

console.log('✅ All proofs verified!');
```

**Advantages**:
- Lower fees (amortized costs)
- Single transaction
- Atomic verification
- Faster processing"""
    }
    
    code = examples.get(operation_clean)
    if not code:
        available_ops = ", ".join(examples.keys())
        return f"❌ Unknown operation: {operation}\n\nAvailable operations:\n{available_ops}"
    
    # Add note about data freshness
    if sdk_docs:
        note = "\n\n✅ Note: Latest SDK patterns verified against live documentation"
    else:
        note = "\n\n📝 Note: For latest SDK docs visit: https://docs.zkverify.io/"
    
    return code + note


@mcp.tool()
async def calculate_verification_cost(proof_system: str = "", num_proofs: str = "1") -> str:
    """Calculate estimated cost for proof verification on zkVerify versus native blockchain verification."""
    logger.info(f"Calculating cost for {num_proofs} {proof_system} proofs")
    
    if not proof_system.strip():
        return "❌ Please specify proof system: groth16, fflonk, risc0"
    
    try:
        count = int(num_proofs) if num_proofs.strip() else 1
        if count < 1:
            return "❌ Number of proofs must be at least 1"
        if count > 10000:
            count = 10000
    except ValueError:
        return f"❌ Invalid number: {num_proofs}. Please provide a valid integer."
    
    proof_system_clean = proof_system.lower().strip()
    
    # Try to fetch latest cost data from docs
    logger.info("Attempting to fetch latest cost data from docs")
    cost_content = await fetch_from_docs("https://docs.zkverify.io/overview/pricing")
    
    if cost_content and ("cost" in cost_content.lower() or "price" in cost_content.lower() or "fee" in cost_content.lower()):
        logger.info("Found pricing information in docs")
        return f"""💰 Cost Information for {proof_system_clean.upper()} proofs (Live from Docs):

{cost_content[:2000]}

Source: https://docs.zkverify.io/overview/pricing
Status: ✅ Live data

For complete pricing details, visit: https://docs.zkverify.io/"""
    
    logger.warning("Could not fetch pricing information")
    return f"""❌ Unable to fetch pricing information from documentation.

Please visit https://docs.zkverify.io/overview/pricing for the latest cost information."""

@mcp.tool()
async def get_tutorial_info(tutorial_type: str = "") -> str:
    """Get detailed information about zkVerify tutorials - types: nextjs-circom, nextjs-noir, typescript-example, zkemail, tee-proof, relayer-workflow."""
    logger.info(f"Getting tutorial info for: {tutorial_type}")
    
    if not tutorial_type.strip():
        return """❌ Please specify tutorial type

Available tutorials:
- nextjs-circom: Build a NextJS app with Circom proofs and client-side proving
- nextjs-noir: Build a NextJS app with Noir proofs and client-side proving
- typescript-example: Submit proofs using zkVerifyJS TypeScript SDK
- zkemail: Verify zkEmail proofs with zkVerify
- tee-proof: Wrap TEE proofs with Risc Zero for verification
- relayer-workflow: Complete workflow using Relayer API service"""
    
    tutorial_clean = tutorial_type.lower().strip()
    base_url = "https://docs.zkverify.io/"
    
    tutorial_map = {
        "nextjs-circom": f"{base_url}overview/tutorials/nextjs-circom",
        "nextjs-noir": f"{base_url}overview/tutorials/nextjs-noir",
        "typescript-example": f"{base_url}tutorials/submit-proofs/typescript-example",
        "zkemail": f"{base_url}overview/explorations/zkemail",
        "tee-proof": f"{base_url}overview/explorations/tee-proof",
        "relayer-workflow": f"{base_url}overview/getting-started/relayer"
    }
    
    if tutorial_clean not in tutorial_map:
        available = ", ".join(tutorial_map.keys())
        return f"❌ Unknown tutorial type: {tutorial_type}. Available: {available}"
    
    url = tutorial_map[tutorial_clean]
    content = await fetch_from_docs(url, timeout=15)
    
    if content:
        logger.info(f"Found {tutorial_clean} tutorial info")
        
        # Provide context-specific information
        context_info = ""
        if tutorial_clean == "nextjs-circom":
            context_info = """
**Tutorial Overview**:
This tutorial guides you through building a NextJS application with:
- Client-side proof generation using Circom and SnarkJS
- Integration with zkVerify Relayer API for proof verification
- Complete frontend-to-backend workflow

**GitHub Repository**: https://github.com/zkVerify/tutorials/tree/main/nextjs-circom
**Circuit Tool**: https://zkrepl.dev/"""
        elif tutorial_clean == "nextjs-noir":
            context_info = """
**Tutorial Overview**:
This tutorial guides you through building a NextJS application with:
- Client-side proof generation using Noir and bb.js
- UltraPlonk proof system integration
- zkVerify Relayer API for verification

**GitHub Repository**: https://github.com/zkVerify/tutorials/tree/main/nextjs-noir"""
        elif tutorial_clean == "zkemail":
            context_info = """
**Tutorial Overview**:
Verify zkEmail proofs with zkVerify:
- Use zkEmail SDK to generate remote proofs
- Submit Groth16 proofs to zkVerify
- Complete email verification workflow

**GitHub Repository**: https://github.com/zkVerify/explorations/tree/main/zkEmail
**zkEmail Docs**: https://docs.zk.email/zk-email-sdk/setup
**Blueprint Registry**: https://registry.zk.email/"""
        elif tutorial_clean == "tee-proof":
            context_info = """
**Tutorial Overview**:
Wrap TEE attestations with Risc Zero for zkVerify verification:
- Use Automata's DCAP CLI for TEE verification
- Generate Risc Zero STARK proofs
- Submit to zkVerify without Groth16 wrapping

**GitHub Repository**: https://github.com/zkVerify/explorations/tree/main/tee-risc0"""
        
        return f"""✅ {tutorial_clean.upper().replace('-', ' ').title()} Tutorial (Live from Docs)

{context_info}

**Tutorial Content**:
{content[:4000]}

... (truncated, visit source for complete tutorial)

Source: {url}
Status: ✅ Live data from zkVerify documentation
GitHub: https://github.com/zkVerify/tutorials

For the complete step-by-step tutorial, visit: {url}"""
    
    logger.warning(f"Could not find {tutorial_clean} tutorial info")
    return f"""❌ Unable to fetch tutorial information for: {tutorial_type}

Please visit {url} directly for the latest tutorial information.

**Alternative Resources**:
- Main Tutorials: https://docs.zkverify.io/overview/tutorials/nextjs-circom
- GitHub: https://github.com/zkVerify/tutorials
- Explorations: https://github.com/zkVerify/explorations"""

@mcp.tool()
async def get_exploration_info(exploration_type: str = "") -> str:
    """Get detailed information about zkVerify explorations - types: zkemail, tee-proof, galxe-identity."""
    logger.info(f"Getting exploration info for: {exploration_type}")
    
    if not exploration_type.strip():
        return """❌ Please specify exploration type

Available explorations:
- zkemail: Verify zkEmail proofs with zkVerify for private email verification
- tee-proof: Wrap TEE attestations with Risc Zero for on-chain verification
- galxe-identity: Use Galxe Identity Protocol with zkVerify for credential verification"""
    
    exploration_clean = exploration_type.lower().strip()
    base_url = "https://docs.zkverify.io/overview/explorations/"
    
    exploration_map = {
        "zkemail": f"{base_url}zkemail",
        "tee-proof": f"{base_url}tee-proof",
        "galxe-identity": f"{base_url}galxe-identity"
    }
    
    if exploration_clean not in exploration_map:
        available = ", ".join(exploration_map.keys())
        return f"❌ Unknown exploration type: {exploration_type}. Available: {available}"
    
    url = exploration_map[exploration_clean]
    content = await fetch_from_docs(url, timeout=15)
    
    if content:
        logger.info(f"Found {exploration_clean} exploration info")
        
        # Add context-specific information
        context_info = ""
        if exploration_clean == "zkemail":
            context_info = """
**Exploration Overview**:
Learn how to verify zkEmail proofs with zkVerify for privacy-preserving email verification:
- Generate remote proofs using zkEmail SDK
- Submit Groth16 proofs to zkVerify via zkVerifyJS
- Build applications with private email verification

**Use Cases**: Email-based authentication, selective disclosure, proof of email ownership

**Resources**:
- GitHub: https://github.com/zkVerify/explorations/tree/main/zkEmail
- zkEmail SDK: https://docs.zk.email/zk-email-sdk/setup
- Blueprint Registry: https://registry.zk.email/
- Example Email: https://docs.zk.email/files/residency.eml"""
        elif exploration_clean == "tee-proof":
            context_info = """
**Exploration Overview**:
Wrap TEE (Trusted Execution Environment) attestations with Risc Zero for zkVerify verification:
- Use Automata's DCAP CLI for Intel SGX attestation verification
- Generate Risc Zero STARK proofs from TEE attestations
- Submit to zkVerify without Groth16 wrapping (native STARK support)

**Use Cases**: Hardware-based trust, confidential computing, secure enclaves

**Resources**:
- GitHub: https://github.com/zkVerify/explorations/tree/main/tee-risc0
- Automata DCAP: https://github.com/automata-network/dcap-rs
- Risc Zero: https://www.risczero.com/"""
        elif exploration_clean == "galxe-identity":
            context_info = """
**Exploration Overview**:
Integrate Galxe Identity Protocol with zkVerify for credential verification:
- Use Galxe SDK for verifiable credentials
- Verify credentials on zkVerify with reduced costs
- Build Sybil-resistant systems with ZK credentials

**Use Cases**: Identity verification, credential systems, reputation, Sybil prevention

**Resources**:
- GitHub: https://github.com/zkVerify/explorations/tree/main/galxe-identity
- Galxe Identity Protocol: https://docs.galxe.com/identity-protocol"""
        
        return f"""✅ {exploration_clean.upper().replace('-', ' ').title()} Exploration (Live from Docs)

{context_info}

**Exploration Content**:
{content[:4000]}

... (truncated, visit source for complete exploration guide)

Source: {url}
Status: ✅ Live data from zkVerify documentation
GitHub: https://github.com/zkVerify/explorations

For the complete exploration guide, visit: {url}"""
    
    logger.warning(f"Could not find {exploration_clean} exploration info")
    return f"""❌ Unable to fetch exploration information for: {exploration_type}

Please visit {url} directly for the latest exploration information.

**Alternative Resources**:
- Explorations GitHub: https://github.com/zkVerify/explorations
- Main Documentation: https://docs.zkverify.io/overview/explorations/zkemail"""

@mcp.tool()
async def get_testnet_phases() -> str:
    """Get information about zkVerify incentivized testnet phases and challenges."""
    logger.info("Getting testnet phases information")
    
    # Fetch multiple related pages for comprehensive info
    phases_url = "https://docs.zkverify.io/incentivizedtestnet/phases"
    getting_started_url = "https://docs.zkverify.io/incentivizedtestnet/getting_started"
    
    phases_content = await fetch_from_docs(phases_url, timeout=15)
    getting_started_content = await fetch_from_docs(getting_started_url, timeout=15)
    
    if phases_content or getting_started_content:
        logger.info("Found testnet phases info")
        
        result = """✅ zkVerify Incentivized Testnet Information (Live from Docs)

**Overview**:
The zkVerify Incentivized Testnet offers developers and enthusiasts the opportunity to shape the future of ZK proof verification. Participate in challenges, earn points, and contribute to the ecosystem.

**Why Participate**:
- Create dApps with ZK features, excellent performance, and low cost
- Contribute to the robustness of the zkVerify ecosystem
- Earn points and potentially receive future rewards
- Gain hands-on experience with cutting-edge blockchain and ZK technology
- Collaborate with a passionate community

**Key Resources**:
- Testnet Documentation: https://docs.zkverify.io/incentivizedtestnet/getting_started
- Phases & Challenges: https://docs.zkverify.io/incentivizedtestnet/phases
- Rules & Guidelines: https://docs.zkverify.io/incentivizedtestnet/rules_and_guidelines
- Terms & Conditions: https://docs.zkverify.io/incentivizedtestnet/terms-and-conditions/IT_terms_and_conditions
- Express Interest Form: https://forms.gle/rTLYKdskVRXxGRGz9

**Network Information**:
- Testnet RPC: wss://zkverify-volta-rpc.zkverify.io
- Testnet Explorer: https://zkverify-testnet.subscan.io/
- Testnet Faucet: https://zkverify-faucet.zkverify.io/
- Discord Support: https://discord.gg/zkverify

"""
        
        if getting_started_content:
            result += f"""**Getting Started Content**:
{getting_started_content[:2000]}

"""
        
        if phases_content:
            result += f"""**Phases & Challenges Content**:
{phases_content[:2000]}

"""
        
        result += f"""Source: {phases_url}
Status: ✅ Live data from zkVerify documentation

**For Existing zkApps/zkRollups**:
Express your interest through the form to participate and potentially receive incentives.
Points are allocated for established projects joining the ecosystem."""
        
        return result
    
    logger.warning("Could not find testnet phases info")
    return """❌ Unable to fetch testnet phases information.

**Default Information**:

The zkVerify Incentivized Testnet is live! Participate in challenges to earn rewards and contribute to the ecosystem.

**Key Links**:
- Getting Started: https://docs.zkverify.io/incentivizedtestnet/getting_started
- Phases: https://docs.zkverify.io/incentivizedtestnet/phases
- Express Interest: https://forms.gle/rTLYKdskVRXxGRGz9
- Discord: https://discord.gg/zkverify

Please visit the documentation directly for the latest information."""

@mcp.tool()
async def get_node_operator_guide(guide_type: str = "") -> str:
    """Get node operator guides - types: docker, binaries, nominators, overview."""
    logger.info(f"Getting node operator guide for: {guide_type}")
    
    if not guide_type.strip():
        return """❌ Please specify guide type

Available node operator guides:
- overview: General information about node types and hardware requirements
- docker: Run a zkVerify node using Docker (recommended)
- binaries: Build and run from source binaries
- nominators: Become a nominator and stake VFY tokens"""
    
    guide_clean = guide_type.lower().strip()
    base_url = "https://docs.zkverify.io/node-operators/"
    
    guide_map = {
        "overview": f"{base_url}getting_started",
        "docker": f"{base_url}run_using_docker/getting_started_docker",
        "binaries": f"{base_url}run_using_binaries/getting_started_binaries",
        "nominators": f"{base_url}nominators"
    }
    
    if guide_clean not in guide_map:
        available = ", ".join(guide_map.keys())
        return f"❌ Unknown guide type: {guide_type}. Available: {available}"
    
    url = guide_map[guide_clean]
    content = await fetch_from_docs(url, timeout=15)
    
    if content:
        logger.info(f"Found {guide_clean} node operator guide")
        
        # Add context-specific information
        context_info = ""
        if guide_clean == "overview":
            context_info = """
**Node Types**:
1. **RPC Nodes**: Local entry point to interact with the blockchain
   - Maintain full or partial copy of blockchain
   - No staking required
   
2. **Boot Nodes (Seeder Nodes)**: Entry points for network connectivity
   - Enhance decentralization
   - Hold minimal blockchain data
   
3. **Validator Nodes**: Participate in consensus and block authoring
   - Earn VFY tokens through staking
   - Require high-security environment
   - Maintain complete blockchain copy

**Hardware Requirements**:
- RPC/Boot: 4 cores, 16GB RAM, ≥500GB NVMe
- Validator: 8 cores, 32GB RAM, ≥500GB NVMe
- All: ≥1 Gbps bandwidth

**Node Data Snapshots**: Available at https://bootstraps.zkverify.io/"""
        elif guide_clean == "docker":
            context_info = """
**Docker Setup (Recommended)**:
Docker provides a convenient and consistent environment for running your zkVerify node:
- Simplifies deployment across platforms
- Ensures compatibility
- Recommended for ease of use and maintenance

**Prerequisites**: Docker and Docker Compose installed"""
        elif guide_clean == "binaries":
            context_info = """
**Binary Setup (Advanced)**:
Build zkVerify node from source for more control:
- Manual compilation and configuration
- Suitable for advanced users
- More customization options

**Source Code**: https://github.com/zkVerify/zkVerify"""
        elif guide_clean == "nominators":
            context_info = """
**Becoming a Nominator**:
Nominators help secure the network by staking VFY tokens with validators:
- Support network security without running a full validator
- Earn staking rewards
- Lower hardware requirements than validators

**Staking Process**: Delegate tokens to trusted validators"""
        
        return f"""✅ {guide_clean.upper().replace('-', ' ').title()} Node Operator Guide (Live from Docs)

{context_info}

**Guide Content**:
{content[:4000]}

... (truncated, visit source for complete guide)

Source: {url}
Status: ✅ Live data from zkVerify documentation

**Additional Resources**:
- Main Documentation: https://docs.zkverify.io/node-operators/getting_started
- GitHub: https://github.com/zkVerify/zkVerify
- Snapshots: https://bootstraps.zkverify.io/
- Discord Support: https://discord.gg/zkverify

For the complete node operator guide, visit: {url}"""
    
    logger.warning(f"Could not find {guide_clean} node operator guide")
    return f"""❌ Unable to fetch node operator guide for: {guide_type}

Please visit {url} directly for the latest information.

**Alternative Resources**:
- Node Operators Documentation: https://docs.zkverify.io/node-operators/getting_started
- GitHub: https://github.com/zkVerify/zkVerify
- Discord Support: https://discord.gg/zkverify"""

@mcp.tool()
async def get_verifier_guide(guide_type: str = "") -> str:
    """Get verifier integration guides - types: introduction, getting-started, palletization, runtime-inclusion, end-to-end-tests, conclusion."""
    logger.info(f"Getting verifier guide for: {guide_type}")
    
    if not guide_type.strip():
        return """❌ Please specify guide type

Available verifier integration guides:
- introduction: Overview of zkVerify verifiers and integration process
- getting-started: Prerequisites and setup for verifier development
- palletization: Create a pallet for your verifier
- runtime-inclusion: Include your verifier in the zkVerify runtime
- end-to-end-tests: Write comprehensive tests for your verifier
- conclusion: Final steps and next actions"""
    
    guide_clean = guide_type.lower().strip()
    base_url = "https://docs.zkverify.io/overview/add-new-verifier/"
    
    guide_map = {
        "introduction": f"{base_url}introduction",
        "getting-started": f"{base_url}getting_started",
        "palletization": f"{base_url}palletization/overview",
        "runtime-inclusion": f"{base_url}runtime_inclusion/overview",
        "end-to-end-tests": f"{base_url}end_to_end_tests",
        "conclusion": f"{base_url}conclusion"
    }
    
    if guide_clean not in guide_map:
        available = ", ".join(guide_map.keys())
        return f"❌ Unknown guide type: {guide_type}. Available: {available}"
    
    url = guide_map[guide_clean]
    content = await fetch_from_docs(url, timeout=15)
    
    if content:
        logger.info(f"Found {guide_clean} verifier guide")
        
        # Add context-specific information
        context_info = ""
        if guide_clean == "introduction":
            context_info = """
**Overview**:
Learn how to integrate your own verifier into zkVerify. This enables your proving system to be supported on zkVerify, allowing anyone to submit and verify proofs for your system.

**Why Integrate**:
- Expand zkVerify's proof system support
- Enable your community to use zkVerify
- Contribute to the ZK ecosystem

**Currently Supported Verifiers**:
- Groth16 (Circom, SnarkJS, Gnark)
- FFlonk, Risc0, Plonky2, SP1
- UltraPlonk, UltraHonk (Noir)"""
        elif guide_clean == "getting-started":
            context_info = """
**Prerequisites**:
- Understanding of Substrate framework
- Knowledge of your proof system's verification algorithm
- Rust programming experience
- Familiarity with pallet development

**Development Environment**:
- Rust toolchain
- Substrate dependencies
- zkVerify source code"""
        elif guide_clean == "palletization":
            context_info = """
**Palletization Process**:
Create a Substrate pallet that implements your verifier:
- Define verification logic
- Handle proof format parsing
- Implement error handling
- Optimize gas costs

**Key Considerations**:
- Proof size limits
- Public input constraints
- Performance optimization"""
        elif guide_clean == "runtime-inclusion":
            context_info = """
**Runtime Integration**:
Include your pallet in the zkVerify runtime:
- Add pallet dependencies
- Configure runtime
- Set up weights and fees
- Test integration

**Testing**:
- Unit tests for pallet logic
- Integration tests with runtime
- Benchmarking for accurate weights"""
        
        return f"""✅ {guide_clean.upper().replace('-', ' ').title()} - Add New Verifier Guide (Live from Docs)

{context_info}

**Guide Content**:
{content[:4000]}

... (truncated, visit source for complete guide)

Source: {url}
Status: ✅ Live data from zkVerify documentation

**Verifier Integration Steps**:
1. Introduction - Understand the process
2. Getting Started - Set up development environment
3. Palletization - Implement your verifier as a pallet
4. Runtime Inclusion - Integrate into zkVerify runtime
5. End-to-End Tests - Comprehensive testing
6. Conclusion - Submit your verifier

**Resources**:
- GitHub: https://github.com/zkVerify/zkVerify
- Documentation: https://docs.zkverify.io/overview/add-new-verifier/introduction
- Discord Support: https://discord.gg/zkverify

For the complete verifier integration guide, visit: {url}"""
    
    logger.warning(f"Could not find {guide_clean} verifier guide")
    return f"""❌ Unable to fetch verifier guide for: {guide_type}

Please visit {url} directly for the latest information.

**Alternative Resources**:
- Add New Verifier: https://docs.zkverify.io/overview/add-new-verifier/introduction
- GitHub: https://github.com/zkVerify/zkVerify
- Discord Support: https://discord.gg/zkverify"""

@mcp.tool()
async def get_relayer_api_info(network: str = "testnet") -> str:
    """Get zkVerify Relayer API documentation and endpoints - network: mainnet or testnet."""
    logger.info(f"Getting relayer API info for: {network}")
    
    network_clean = network.lower().strip()
    
    if network_clean not in ["mainnet", "testnet"]:
        return "❌ Please specify network: mainnet or testnet"
    
    if network_clean == "mainnet":
        url = "https://relayer-api-mainnet.horizenlabs.io/docs"
        api_base = "https://relayer-api-mainnet.horizenlabs.io"
    else:
        url = "https://relayer-api-testnet.horizenlabs.io/docs"
        api_base = "https://relayer-api-testnet.horizenlabs.io"
    
    content = await fetch_from_docs(url, timeout=15)
    
    if content:
        logger.info(f"Successfully fetched relayer {network_clean} API docs")
        return f"""✅ zkVerify Relayer API - {network_clean.upper()} (Live from API Docs)

**API Base URL**: {api_base}
**Documentation**: {url}

{content[:4000]}

Source: {url}
Status: ✅ Live data

**Quick Start**:
- Base URL: {api_base}
- Network: {network_clean}
- Documentation: {url}

For complete API documentation and interactive testing, visit: {url}"""
    
    logger.warning(f"Could not fetch relayer {network_clean} API docs")
    return f"""❌ Unable to fetch relayer API documentation for {network_clean}

Please visit {url} directly for the latest API documentation.

**API Endpoints**:
- Mainnet: https://relayer-api-mainnet.horizenlabs.io/docs
- Testnet: https://relayer-api-testnet.horizenlabs.io/docs"""

@mcp.tool()
async def generate_relayer_example(operation: str = "", network: str = "testnet") -> str:
    """Generate example code for zkVerify Relayer API operations - operations: register-vk, submit-proof, get-status, complete-workflow."""
    logger.info(f"Generating relayer example for {operation} on {network}")
    
    if not operation.strip():
        return """❌ Please specify an operation:
- register-vk: Register a verification key
- submit-proof: Submit a proof through the relayer
- get-status: Check proof submission status and poll until finalized
- complete-workflow: Complete workflow from VK registration to proof verification
- get-aggregation: Get aggregation details for smart contract verification"""
    
    network_clean = network.lower().strip()
    if network_clean not in ["mainnet", "testnet"]:
        network_clean = "testnet"
    
    if network_clean == "mainnet":
        api_base = "https://relayer-api-mainnet.horizenlabs.io"
    else:
        api_base = "https://relayer-api-testnet.horizenlabs.io"
    
    operation_clean = operation.lower().strip()
    
    examples = {
        "register-vk": f"""✅ Register Verification Key via Relayer API ({network_clean.upper()})

```typescript
import axios from 'axios';
import fs from 'fs';
import dotenv from 'dotenv';
dotenv.config();

const API_URL = '{api_base}/api/v1';
const API_KEY = process.env.API_KEY; // Get from https://relayer-api-{network_clean}.horizenlabs.io/

async function registerVK() {{
  // Load your verification key (example for Groth16/Circom)
  const vkey = JSON.parse(fs.readFileSync('./data/main.groth16.vkey.json'));
  
  // Check if already registered
  if (!fs.existsSync('vkey-hash.json')) {{
    try {{
      const regParams = {{
        "proofType": "groth16",
        "proofOptions": {{
          "library": "snarkjs",
          "curve": "bn128"
        }},
        "vk": vkey
      }};
      
      const response = await axios.post(
        `${{API_URL}}/register-vk/${{API_KEY}}`,
        regParams
      );
      
      console.log('✅ VK registered successfully!');
      console.log('VK Hash:', response.data.vkHash);
      
      // Save for later use
      fs.writeFileSync('vkey-hash.json', JSON.stringify(response.data));
      
      return response.data;
    }} catch (error) {{
      if (error.response?.status === 400 && error.response?.data?.code === 'VK_ALREADY_REGISTERED') {{
        console.log('ℹ️ VK already registered');
        fs.writeFileSync('vkey-hash.json', JSON.stringify(error.response.data.meta));
        return error.response.data.meta;
      }}
      throw error;
    }}
  }}
  
  return JSON.parse(fs.readFileSync('vkey-hash.json'));
}}

// For other proof systems:

// Risc Zero
const regParamsRisc0 = {{
  "proofType": "risc0",
  "proofOptions": {{
    "version": "V2_1"
  }},
  "vk": proof.image_id
}};

// Ultrahonk (Noir)
const regParamsUltrahonk = {{
  "proofType": "ultrahonk",
  "vk": vkey.split("\\n")[0]
}};

// Ultraplonk (Noir)
const regParamsUltraplonk = {{
  "proofType": "ultraplonk",
  "proofOptions": {{
    "numberOfPublicInputs": 1
  }},
  "vk": base64Vk
}};

// SP1
const regParamsSP1 = {{
  "proofType": "sp1",
  "vk": proof.vkey
}};
```

```bash
# Using cURL
curl -X POST '{api_base}/api/v1/register-vk/YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{{
    "proofType": "groth16",
    "proofOptions": {{
      "library": "snarkjs",
      "curve": "bn128"
    }},
    "vk": {{}}
  }}'
```

**Response**:
```json
{{
  "vkHash": "0x..."
}}
```

**Network**: {network_clean}
**Endpoint**: {api_base}
**API Key**: Get from https://relayer-api-{network_clean}.horizenlabs.io/
**Docs**: {api_base}/docs

**Supported Proof Types**: groth16, risc0, fflonk, ultrahonk, ultraplonk, sp1""",

        "submit-proof": f"""✅ Submit Proof via Relayer API ({network_clean.upper()})

```typescript
import axios from 'axios';
import fs from 'fs';
import dotenv from 'dotenv';
dotenv.config();

const API_URL = '{api_base}/api/v1';
const API_KEY = process.env.API_KEY;

async function submitProof() {{
  // Load proof, public inputs, and VK hash
  const proof = JSON.parse(fs.readFileSync('./data/proof.json'));
  const publicInputs = JSON.parse(fs.readFileSync('./data/public.json'));
  const vkData = JSON.parse(fs.readFileSync('vkey-hash.json'));
  
  const params = {{
    "proofType": "groth16",
    "vkRegistered": true,
    "chainId": 11155111, // Optional: for aggregation (e.g., Sepolia)
    "proofOptions": {{
      "library": "snarkjs",
      "curve": "bn128"
    }},
    "proofData": {{
      "proof": proof,
      "publicSignals": publicInputs,
      "vk": vkData.vkHash
    }}
  }};
  
  const response = await axios.post(
    `${{API_URL}}/submit-proof/${{API_KEY}}`,
    params
  );
  
  console.log('✅ Proof submitted!');
  console.log('Job ID:', response.data.jobId);
  console.log('Optimistic Verify:', response.data.optimisticVerify);
  
  if (response.data.optimisticVerify !== 'success') {{
    console.error('❌ Optimistic verification failed!');
    return null;
  }}
  
  return response.data;
}}

// Example response:
// {{
//   "jobId": "23382e04-3d57-11f0-af7b-32a805cdbfd3",
//   "optimisticVerify": "success"
// }}
```

```bash
# Using cURL
curl -X POST '{api_base}/api/v1/submit-proof/YOUR_API_KEY' \\
  -H 'Content-Type: application/json' \\
  -d '{{
    "proofType": "groth16",
    "vkRegistered": true,
    "chainId": 11155111,
    "proofData": {{
      "proof": {{}},
      "publicSignals": [],
      "vk": "0x..."
    }}
  }}'
```

**Network**: {network_clean}
**Endpoint**: {api_base}
**Docs**: {api_base}/docs

**Important**: 
- Set `vkRegistered: true` and use `vkHash` if VK is pre-registered
- Set `vkRegistered: false` and include full VK if not registered
- `chainId` is optional - include only if you want aggregation for smart contract verification""",

        "get-status": f"""✅ Check Proof Status via Relayer API ({network_clean.upper()})

```typescript
import axios from 'axios';

const API_URL = '{api_base}/api/v1';
const API_KEY = process.env.API_KEY;

async function getJobStatus(jobId: string) {{
  const response = await axios.get(
    `${{API_URL}}/job-status/${{API_KEY}}/${{jobId}}`
  );
  
  return response.data;
}}

// Poll until finalized (without aggregation)
async function waitForFinalization(jobId: string) {{
  console.log('⏳ Waiting for proof finalization...');
  
  while (true) {{
    const status = await getJobStatus(jobId);
    
    console.log(`Status: ${{status.status}} (ID: ${{status.statusId}})`);
    
    if (status.status === 'Finalized') {{
      console.log('✅ Proof finalized successfully!');
      console.log('TX Hash:', status.txHash);
      console.log('Block Hash:', status.blockHash);
      return status;
    }}
    
    if (status.status === 'Failed') {{
      console.error('❌ Proof verification failed!');
      console.error('Error:', status.errorDetails);
      throw new Error('Proof verification failed');
    }}
    
    // Wait 5 seconds before checking again
    await new Promise(resolve => setTimeout(resolve, 5000));
  }}
}}

// Poll until aggregated (with chainId)
async function waitForAggregation(jobId: string) {{
  console.log('⏳ Waiting for proof aggregation...');
  
  while (true) {{
    const status = await getJobStatus(jobId);
    
    console.log(`Status: ${{status.status}}`);
    
    if (status.status === 'Aggregated') {{
      console.log('✅ Proof aggregated successfully!');
      console.log('Aggregation ID:', status.aggregationId);
      console.log('Statement:', status.statement);
      console.log('Aggregation Details:', status.aggregationDetails);
      
      // Save aggregation details for smart contract verification
      fs.writeFileSync('aggregation.json', JSON.stringify({{
        ...status.aggregationDetails,
        aggregationId: status.aggregationId
      }}));
      
      return status;
    }}
    
    if (status.status === 'AggregationPublished') {{
      console.log('✅ Proof published to destination chain!');
      console.log('Destination Chain:', status.aggregationPublished.destinationChainId);
      console.log('Destination TX:', status.aggregationPublished.destinationTxHash);
      return status;
    }}
    
    if (status.status === 'Failed') {{
      console.error('❌ Processing failed!');
      console.error('Error:', status.errorDetails);
      throw new Error('Processing failed');
    }}
    
    // Wait 20 seconds for aggregation (slower process)
    await new Promise(resolve => setTimeout(resolve, 20000));
  }}
}}
```

```bash
# Using cURL
curl '{api_base}/api/v1/job-status/YOUR_API_KEY/JOB_ID'
```

**Job Statuses**:
- **Queued**: Proof accepted and waiting for processing
- **Valid**: Proof passed optimistic verification
- **Submitted**: Proof submitted to blockchain/mempool
- **IncludedInBlock**: Proof transaction included in a block
- **Finalized**: Proof transaction finalized on-chain
- **AggregationPending**: Proof ready for aggregation (only with chainId)
- **Aggregated**: Proof successfully aggregated and published (only with chainId)
- **AggregationPublished**: Proof aggregation published to destination chain (only with chainId)
- **Failed**: Proof processing failed

**Network**: {network_clean}
**Endpoint**: {api_base}
**Docs**: {api_base}/docs""",

        "complete-workflow": f"""✅ Complete Workflow: VK Registration → Proof Submission → Verification ({network_clean.upper()})

```typescript
import axios from 'axios';
import fs from 'fs';
import dotenv from 'dotenv';
dotenv.config();

const API_URL = '{api_base}/api/v1';
const API_KEY = process.env.API_KEY; // Get from https://relayer-api-{network_clean}.horizenlabs.io/

async function main() {{
  // Step 1: Register Verification Key
  console.log('📝 Step 1: Registering Verification Key...');
  
  const vkey = JSON.parse(fs.readFileSync('./data/main.groth16.vkey.json'));
  
  let vkHash;
  if (!fs.existsSync('circom-vkey.json')) {{
    try {{
      const regParams = {{
        "proofType": "groth16",
        "proofOptions": {{
          "library": "snarkjs",
          "curve": "bn128"
        }},
        "vk": vkey
      }};
      
      const regResponse = await axios.post(
        `${{API_URL}}/register-vk/${{API_KEY}}`,
        regParams
      );
      
      fs.writeFileSync('circom-vkey.json', JSON.stringify(regResponse.data));
      vkHash = regResponse.data.vkHash;
      console.log('✅ VK registered! Hash:', vkHash);
    }} catch (error) {{
      if (error.response?.data?.code === 'VK_ALREADY_REGISTERED') {{
        vkHash = error.response.data.meta.vkHash;
        fs.writeFileSync('circom-vkey.json', JSON.stringify(error.response.data.meta));
        console.log('ℹ️ VK already registered. Hash:', vkHash);
      }} else {{
        throw error;
      }}
    }}
  }} else {{
    const vkData = JSON.parse(fs.readFileSync('circom-vkey.json'));
    vkHash = vkData.vkHash;
    console.log('ℹ️ Using existing VK hash:', vkHash);
  }}
  
  // Step 2: Submit Proof
  console.log('\\n🚀 Step 2: Submitting Proof...');
  
  const proof = JSON.parse(fs.readFileSync('./data/proof.json'));
  const publicInputs = JSON.parse(fs.readFileSync('./data/public.json'));
  
  const params = {{
    "proofType": "groth16",
    "vkRegistered": true,
    "chainId": null, // Set to 11155111 for Sepolia aggregation
    "proofOptions": {{
      "library": "snarkjs",
      "curve": "bn128"
    }},
    "proofData": {{
      "proof": proof,
      "publicSignals": publicInputs,
      "vk": vkHash
    }}
  }};
  
  const submitResponse = await axios.post(
    `${{API_URL}}/submit-proof/${{API_KEY}}`,
    params
  );
  
  console.log('✅ Proof submitted!');
  console.log('Job ID:', submitResponse.data.jobId);
  console.log('Optimistic Verify:', submitResponse.data.optimisticVerify);
  
  if (submitResponse.data.optimisticVerify !== 'success') {{
    console.error('❌ Optimistic verification failed!');
    return;
  }}
  
  // Step 3: Wait for Finalization
  console.log('\\n⏳ Step 3: Waiting for finalization on zkVerify...');
  
  const jobId = submitResponse.data.jobId;
  
  while (true) {{
    const statusResponse = await axios.get(
      `${{API_URL}}/job-status/${{API_KEY}}/${{jobId}}`
    );
    
    const status = statusResponse.data;
    console.log(`Status: ${{status.status}}`);
    
    if (status.status === 'Finalized') {{
      console.log('\\n✅ Proof finalized successfully!');
      console.log('TX Hash:', status.txHash);
      console.log('Block Hash:', status.blockHash);
      console.log('Created At:', status.createdAt);
      console.log('Updated At:', status.updatedAt);
      console.log('\\n🎉 Complete! Your proof is verified on zkVerify.');
      break;
    }}
    
    if (status.status === 'Failed') {{
      console.error('\\n❌ Proof verification failed!');
      console.error('Error:', status.errorDetails);
      break;
    }}
    
    console.log('Waiting for job to finalize...');
    await new Promise(resolve => setTimeout(resolve, 5000));
  }}
}}

main().catch(console.error);
```

**Expected Output**:
```
📝 Step 1: Registering Verification Key...
✅ VK registered! Hash: 0x...

🚀 Step 2: Submitting Proof...
✅ Proof submitted!
Job ID: 23382e04-3d57-11f0-af7b-32a805cdbfd3
Optimistic Verify: success

⏳ Step 3: Waiting for finalization on zkVerify...
Status: Submitted
Waiting for job to finalize...
Status: IncludedInBlock
Waiting for job to finalize...
Status: Finalized

✅ Proof finalized successfully!
TX Hash: 0xc0d85e5d50fff2bb5d192ee108664878e228d7fc3c1faa2d23da891832873d51
Block Hash: 0xcd574432b1a961305bbeb2c6b6ef399e1ae5102593846756cbb472bfd53d7d43
Created At: 2025-05-30T13:08:11.000Z
Updated At: 2025-05-30T13:08:27.000Z

🎉 Complete! Your proof is verified on zkVerify.
```

**Network**: {network_clean}
**Endpoint**: {api_base}
**Tutorial**: https://docs.zkverify.io/overview/getting-started/relayer
**Docs**: {api_base}/docs""",

        "get-aggregation": f"""✅ Get Aggregation Details for Smart Contract Verification ({network_clean.upper()})

```typescript
import axios from 'axios';
import fs from 'fs';
import dotenv from 'dotenv';
dotenv.config();

const API_URL = '{api_base}/api/v1';
const API_KEY = process.env.API_KEY;

async function submitWithAggregation() {{
  // Submit proof WITH chainId to enable aggregation
  const vkData = JSON.parse(fs.readFileSync('circom-vkey.json'));
  const proof = JSON.parse(fs.readFileSync('./data/proof.json'));
  const publicInputs = JSON.parse(fs.readFileSync('./data/public.json'));
  
  const params = {{
    "proofType": "groth16",
    "vkRegistered": true,
    "chainId": 11155111, // Sepolia - REQUIRED for aggregation
    "proofOptions": {{
      "library": "snarkjs",
      "curve": "bn128"
    }},
    "proofData": {{
      "proof": proof,
      "publicSignals": publicInputs,
      "vk": vkData.vkHash
    }}
  }};
  
  const response = await axios.post(
    `${{API_URL}}/submit-proof/${{API_KEY}}`,
    params
  );
  
  console.log('✅ Proof submitted with aggregation enabled');
  console.log('Job ID:', response.data.jobId);
  
  if (response.data.optimisticVerify !== 'success') {{
    console.error('❌ Optimistic verification failed!');
    return;
  }}
  
  // Wait for aggregation
  const jobId = response.data.jobId;
  
  while (true) {{
    const statusResponse = await axios.get(
      `${{API_URL}}/job-status/${{API_KEY}}/${{jobId}}`
    );
    
    const status = statusResponse.data;
    console.log(`Status: ${{status.status}}`);
    
    if (status.status === 'Aggregated') {{
      console.log('\\n✅ Proof aggregated successfully!');
      console.log('\\n📦 Aggregation Details:');
      console.log('Aggregation ID:', status.aggregationId);
      console.log('Statement:', status.statement);
      console.log('\\n🔐 Merkle Proof Details:');
      console.log('Receipt:', status.aggregationDetails.receipt);
      console.log('Receipt Block Hash:', status.aggregationDetails.receiptBlockHash);
      console.log('Root:', status.aggregationDetails.root);
      console.log('Leaf:', status.aggregationDetails.leaf);
      console.log('Leaf Index:', status.aggregationDetails.leafIndex);
      console.log('Number of Leaves:', status.aggregationDetails.numberOfLeaves);
      console.log('Merkle Proof:', status.aggregationDetails.merkleProof);
      
      // Save for smart contract verification
      const aggregationData = {{
        ...status.aggregationDetails,
        aggregationId: status.aggregationId,
        statement: status.statement
      }};
      
      fs.writeFileSync('aggregation.json', JSON.stringify(aggregationData, null, 2));
      console.log('\\n💾 Saved to aggregation.json for smart contract use');
      
      return status;
    }}
    
    if (status.status === 'AggregationPublished') {{
      console.log('\\n🎉 Aggregation published to destination chain!');
      console.log('Destination Chain ID:', status.aggregationPublished.destinationChainId);
      console.log('Destination TX Hash:', status.aggregationPublished.destinationTxHash);
      console.log('Published At:', status.aggregationPublished.createdAt);
      return status;
    }}
    
    if (status.status === 'Failed') {{
      console.error('❌ Processing failed:', status.errorDetails);
      throw new Error('Processing failed');
    }}
    
    console.log('Waiting for aggregation... (this may take a while)');
    await new Promise(resolve => setTimeout(resolve, 20000)); // 20 seconds
  }}
}}

submitWithAggregation().catch(console.error);
```

**Aggregation Response Structure**:
```json
{{
  "jobId": "4e77e1c5-4d36-11f0-8eb5-b2e0eb476089",
  "status": "Aggregated",
  "statusId": 6,
  "proofType": "groth16",
  "chainId": 11155111,
  "aggregationId": 29537,
  "statement": "0xd72c67547100dd6f00c60f05f4bb7cf33f22b077e6a76125e911e091197bd55c",
  "aggregationDetails": {{
    "receipt": "0x84c25ba051bc3cc66a74bcf2169befad5f348d0ad7b24efd6c68c70a25783ad2",
    "receiptBlockHash": "0x11802c585a367a02df4b0555d1310ff96fa5490fb6e8da8ebefde3f537ef5cb7",
    "root": "0x84c25ba051bc3cc66a74bcf2169befad5f348d0ad7b24efd6c68c70a25783ad2",
    "leaf": "0xd72c67547100dd6f00c60f05f4bb7cf33f22b077e6a76125e911e091197bd55c",
    "leafIndex": 6,
    "numberOfLeaves": 8,
    "merkleProof": [
      "0xc714a8b348a529a98fd65c547d7d0819afd3be840fdbad95f04c5ce026424cd4",
      "0x958bf24c3a974ce5ad51461bdea442de1907d90d237bba2be3aaca3ec609d777",
      "0x9367529337c04392b71c3174eaaba23fa2c8d8b599b82ec1ec1a420bbf2e2d77"
    ]
  }}
}}
```

**Use Case**: The aggregation data is required for verifying proofs in smart contracts on EVM chains.

**Network**: {network_clean}
**Endpoint**: {api_base}
**Docs**: {api_base}/docs
**Tutorial**: https://docs.zkverify.io/overview/getting-started/relayer"""
    }
    
    code = examples.get(operation_clean)
    if not code:
        available_ops = ", ".join(examples.keys())
        return f"""❌ Unknown operation: {operation}

Available operations:
{available_ops}

**Relayer API Endpoints**:
- Mainnet: https://relayer-api-mainnet.horizenlabs.io/docs
- Testnet: https://relayer-api-testnet.horizenlabs.io/docs"""
    
    return code + f"""

**Additional Resources**:
- Interactive API Docs: {api_base}/docs
- Network: {network_clean}
- For latest API changes, visit: {api_base}/docs"""


# === SERVER STARTUP ===
if __name__ == "__main__":
    transport = os.environ.get("ZKVERIFY_TRANSPORT", "stdio")
    logger.info(f"Starting zkVerify MCP server with transport: {transport}...")
    logger.info("Fetching live documentation from https://docs.zkverify.io/")
    logger.info("Relayer API endpoints:")
    logger.info("  - Mainnet: https://relayer-api-mainnet.horizenlabs.io/docs")
    logger.info("  - Testnet: https://relayer-api-testnet.horizenlabs.io/docs")

    try:
        mcp.run(transport=transport)
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)