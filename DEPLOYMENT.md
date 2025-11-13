# Archon V1 Production Deployment Guide

This document outlines the high-level process for deploying the Archon V1 application to a production environment.

## **Prerequisites**

1.  A production-ready server (e.g., a VM from AWS, GCP, DigitalOcean).
2.  Docker and Docker Compose installed on the server.
3.  A managed PostgreSQL database (e.g., AWS RDS, DigitalOcean Managed Database). Using a managed database is strongly recommended over running PostgreSQL in a container for production.
4.  A domain name configured to point to the server's IP address.
5.  A reverse proxy like Nginx or Caddy configured on the server to handle SSL and route traffic.

## **Deployment Steps**

1.  **Configure Environment Variables:**
    *   Create a `.env` file in the `server` directory on the production server.
    *   Set the `DATABASE_URL` to the connection string for your managed PostgreSQL database.
    *   Set the `JWT_SECRET_KEY` to a long, complex, randomly generated string. **Do not use the development key.**
    *   Set `FLASK_ENV` to `production`.

2.  **Build Production Docker Images:**
    *   On your local machine or in a CI/CD pipeline, build the production-ready Docker images:
        ```bash
        docker-compose -f docker-compose.prod.yml build
        ```
    *   (Note: A `docker-compose.prod.yml` would need to be created, which would build the React app into static files and serve them via Nginx).

3.  **Push Images to a Registry:**
    *   Push the built images to a container registry like Docker Hub, AWS ECR, or Google Container Registry.
        ```bash
        docker-compose -f docker-compose.prod.yml push
        ```

4.  **Deploy on the Server:**
    *   SSH into the production server.
    *   Pull the latest images from the registry:
        ```bash
        docker-compose -f docker-compose.prod.yml pull
        ```
    *   Start the application in detached mode:
        ```bash
        docker-compose -f docker-compose.prod.yml up -d
        ```

5.  **Run Database Migrations:**
    *   Once the server container is running, run the database migrations to set up the production schema:
        ```bash
        docker-compose exec server flask db upgrade
        ```

6.  **Configure Reverse Proxy:**
    *   Configure your reverse proxy (e.g., Nginx) to route traffic to the appropriate containers:
        *   Requests to `yourdomain.com/api/*` should be proxied to the Flask server running on port 5000.
        *   All other requests should be served by the container serving the static React files.
    *   Ensure SSL is enabled and configured correctly (e.g., using Let's Encrypt).

This provides a high-level overview. A real production deployment would require more detailed configuration for logging, monitoring, and security.
