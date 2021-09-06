# Google-Vertex-AI


gcloud builds submit --tag gcr.io/sascha-playground-doit/vertex-build . --timeout=15m

gcloud builds submit --no-source --timeout=60m --config build/pipeline-deployment.yaml