## Overview

This repository is a hands-on DevOps practice project designed to simulate a **realistic software delivery lifecycle**, from local development to containerization and Kubernetes deployment, driven by **GitHub Actions CI pipelines**.

The goal of this project was **not** to build a complex application, but to **practice DevOps fundamentals correctly**:

* Git workflow
* CI pipeline design
* Docker image build strategy
* Environment separation
* Kubernetes deployment basics
* Infrastructure-aware thinking

This project represents how modern teams ship software in production environments.

---

## What Was Built

* A **minimal backend application** (FastAPI / Python)
* PostgreSQL integration for persistence
* Automated **CI pipeline with GitHub Actions**
* **Dockerized application**
* **Kubernetes deployment** using Minikube
* Structured **Git branching strategy** (feature → develop → release → main)

---

## Project Structure

```text
.
├── app/                  # Application source code
├── tests/                # Unit tests
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Local development support
├── k8s/                  # Kubernetes manifests
│   ├── app.yaml
│   └── postgres.yaml
├── .github/workflows/
│   └── ci.yml             # CI pipeline definition
├── requirements.txt
└── README.md
```

---

## Git & Branching Strategy

This project follows a **production-like Git flow**:

* **main**

  * Represents production
  * Always stable
* **develop**

  * Pre-production / integration branch
* **feature/***

  * Short-lived feature branches
* **release/***

  * Release preparation branches

### Flow

```text
feature/* → develop → release/* → main
```

Each merge triggers the CI pipeline to validate the code.

---

## CI Pipeline (GitHub Actions)

The CI pipeline is defined in `.github/workflows/ci.yml` and runs automatically on:

* Push to:

  * `main`
  * `develop`
  * `feature/*`
  * `release/*`
* Pull Requests to:

  * `main`
  * `develop`

### Pipeline Stages

1. **Test**

   * Install dependencies
   * Start PostgreSQL service
   * Run unit tests
2. **Build**

   * Build the application
   * Validate application startup
3. **Docker Build**

   * Build Docker image
   * Ensure image is reproducible

This mirrors what real teams expect before accepting code into shared branches.

---

## Containerization

The application is packaged using **Docker**:

* Multi-stage friendly structure
* Environment-driven configuration
* Ready for CI and Kubernetes usage

Docker images are built during CI to ensure:

* Build reproducibility
* No hidden local dependencies
* Deployment consistency

---

## Kubernetes Deployment (Minikube)

To simulate a production-like runtime environment:

* **Minikube** is used locally
* Kubernetes manifests define:

  * Application Deployment
  * Service exposure
  * PostgreSQL Deployment
* Secrets and environment variables are used for configuration

This step connects CI concepts with **runtime operations**, closing the DevOps loop.

---

## What This Project Taught Me (DevOps Focus)

This project helped me practice and internalize:

* Designing CI pipelines instead of copy-pasting YAML
* Understanding **why** pipelines run on specific branches
* Separating concerns: test vs build vs container
* Treating Docker images as deployable artifacts
* Connecting CI output to Kubernetes deployment
* Debugging pipeline failures and environment mismatches
* Thinking in terms of **systems**, not just code

Most importantly, it reinforced the DevOps mindset:

> You don’t ship code — you ship reliable systems.
