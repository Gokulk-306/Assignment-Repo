#!/bin/bash

echo "========================================="
echo "  Infra Automation Setup Starting..."
echo "========================================="

# Step 1: Check Docker
if ! command -v docker &> /dev/null
then
    echo "Docker not installed. Installing..."
    sudo apt-get update && sudo apt-get install -y docker.io
    sudo systemctl enable docker
    sudo systemctl start docker
fi

# Step 2: Check Docker Compose
if ! command -v docker-compose &> /dev/null
then
    echo "docker-compose not found. Installing..."
    sudo apt-get install -y docker-compose
fi

echo "Building sample-app image..."
docker-compose build sample-app

echo "Starting containers..."
docker-compose up -d

echo "Waiting for app to start..."
sleep 5

echo "================ Health Checks ================"

echo "- Checking Flask App:"
curl -s http://localhost/health

echo "- Checking Nginx:"
curl -I http://localhost/

echo "- Checking Redis:"
docker exec redis redis-cli ping

echo "- Jenkins Initial Admin Password:"
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

echo "================ Containers Running ================"
docker ps

echo "Logs:"
docker-compose logs -f
