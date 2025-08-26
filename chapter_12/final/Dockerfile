# Start with Python 3.12 as base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Create a non-root user and group to run the application
# and install dependencies for healthcheck.
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser

# Copy requirements file and install dependencies
# (We do this first to leverage Docker's layer caching)
COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY --chown=appuser:appgroup . .

# Switch to the non-root user
USER appuser

# Expose the port Streamlit runs on
EXPOSE 8501

# Set Streamlit to run in headless mode and enable health checks
ENV STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_SCRIPTHEALTHCHECKENABLED=true

# Add a healthcheck to the container
HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${STREAMLIT_SERVER_PORT}/healthz || exit 1

# Command to run when the container starts
CMD ["streamlit", "run", "main.py"]
