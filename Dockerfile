# Use Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Ensure Python prints logs immediately
ENV PYTHONUNBUFFERED=1

# Optional: default transport for MCP server (stdio for Cursor/Claude)
ENV ZKVERIFY_TRANSPORT=stdio

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all server files
COPY . .

# Create non-root user and set permissions
RUN useradd -m -u 1000 mcpuser && \
    chown -R mcpuser:mcpuser /app

# Switch to non-root user
USER mcpuser

# Start the server
ENTRYPOINT ["python", "zkverify_server.py"]
