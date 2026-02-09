#!/bin/bash

podman build -t old-core-plaintext:demo --platform linux/amd64 -f old-core-bank/Dockerfile .
podman tag localhost/old-core-plaintext:demo quay.io/natthaphat_k/old-core-plaintext:latest
podman push quay.io/natthaphat_k/old-core-plaintext:latest

podman build -t new-core-json:demo --platform linux/amd64 -f new-core-bank/Dockerfile .
podman tag localhost/new-core-json:demo quay.io/natthaphat_k/new-core-json:latest
podman push quay.io/natthaphat_k/new-core-json:latest