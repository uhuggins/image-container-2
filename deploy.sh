docker build -t image-detection .
docker tag image-detection gcr.io/cloud-functions-356320/image-detection:1.0.0
docker -- push gcr.io/cloud-functions-356320/image-detection:1.0.0
gcloud alpha run deploy  --image="gcr.io/cloud-functions-356320/image-detection:1.0.0" --region="us-central1" --platform managed  --memory=32Gi --port=8000  --allow-unauthenticated

#docker run -d -p 8000:8000 image-detection  ## Run the container locally
docker run -d -p 8000:8000 image-detection