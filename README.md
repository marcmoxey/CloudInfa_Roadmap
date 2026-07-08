# Cloud Engineer Roadmap

A self-paced, hands-on roadmap from Software Engineer to Cloud Infrastructure / Platform Engineer — built entirely on real hardware I own and operate.

**Current status:** Stage 3 (AWS) in progress · Stages 1-2 complete

---

## The Setup

| Device | Role |
|--------|------|
| Beelink SER PRO (Ryzen 5 5625U, 16GB, 500GB) | Home lab server — all roadmap projects |
| Ubuntu Server 26.04 LTS | OS — SSH-only, no GUI |
| Tailscale | Remote SSH access from anywhere |

Everything in this repo was built on real hardware and tested against real servers — not sandboxes that disappear after a tutorial.

---

## Roadmap

### ✅ Stage 1 — Linux Server (Complete)
Set up a production-style Ubuntu Server from scratch.

- Installed Ubuntu Server 26.04 LTS on bare metal
- Configured static IP via Netplan (`192.168.0.52`)
- Set up `ufw` firewall (SSH only, deny by default)
- Installed Tailscale for remote SSH from anywhere (`100.108.108.86`)
- Wrote `disk-usage.sh` — hourly cron job that logs disk usage and warns when above 80%

**Skills:** Linux CLI, SSH, Bash scripting, Netplan, ufw, cron, Tailscale

---

### ✅ Stage 2 — Python Automation (Complete)
Built a real CLI tool that SSHes into remote servers and reports health metrics.

- Completed Automate the Boring Stuff (3rd ed.) chapters 1-19
- Covered: regex, file I/O, argparse, JSON/CSV, subprocess, datetime, Paramiko
- Built `labcheck.py` — a Python CLI tool that:
  - SSHes into any remote Linux server via Paramiko
  - Runs `df`, `free`, and `uptime` remotely
  - Parses output with regex
  - Prints a clean health report
  - Supports both password auth (Beelink) and key-based auth (EC2 `.pem`)

```bash
# Against Beelink (password auth)
python3 labcheck.py --host 100.108.108.86 --user mmoxey

# Against EC2 (key-based auth)
python3 labcheck.py --host <ec2-ip> --user ubuntu --key /path/to/key.pem
```

**Skills:** Python, argparse, Paramiko, regex, getpass, datetime, exception handling

---

### 🔵 Stage 3 — AWS (In Progress)
Standing up the same infrastructure in the cloud.

- AWS CLI configured with IAM least-privilege user
- EC2 instance launched, SSH'd into, terminated
- S3 bucket created, files uploaded/downloaded, deleted
- `s3_audit.py` — Boto3 script that scans all S3 buckets and flags any with public access enabled

**In progress:** VPC, IAM roles, load balancer, complete Boto3 audit scripts

**Skills (so far):** EC2, S3, IAM, AWS CLI, Boto3

---

### 🔲 Stage 4 — Terraform + IaC
Rebuild everything from Stage 3 as code. One command to provision, one to destroy.

- Terraform modules for EC2, S3, VPC, IAM
- IaC scanning with Checkov and tfsec
- Ansible playbook for Beelink configuration management
- Terraform Associate exam

---

### 🔲 Stage 5 — Docker + Kubernetes
Turn the Beelink into a small Kubernetes cluster.

- k3s on the Beelink
- Helm charts, Pod Security Standards, OPA Gatekeeper
- External Secrets Operator (AWS Secrets Manager → k3s pods)
- Container image scanning with Trivy

---

### 🔲 Stage 6 — CI/CD Pipeline
Push code → Beelink redeploys itself automatically.

- GitHub Actions: test → GitLeaks → Semgrep → Trivy → Checkov → build → push
- ArgoCD GitOps deployment
- Pipeline fails the build on critical CVEs, leaked secrets, or SAST findings

---

### 🔲 Stage 7 — Monitoring + Observability
- Prometheus + Grafana (dashboards, alerting)
- Falco (runtime security monitoring)
- Python app instrumented with Prometheus metrics

---

### 🔲 Stage 8 — Security Audit + Portfolio
- Full audit of Beelink, AWS IAM, Kubernetes cluster
- AWS Config rules for compliance as code
- All findings documented with before/after
- Backstage IDP (Platform Engineering path)

---

## Repository Structure

```
Stage_001/          # Bash scripts — disk monitoring, server setup
Stage_002/          # Python — labcheck CLI tool, practice files, journal
Stage_003/          # AWS — Boto3 scripts, EC2/S3/VPC work
Stage_004/          # (coming) Terraform + Ansible
Stage_005/          # (coming) Docker + Kubernetes manifests
Stage_006/          # (coming) GitHub Actions + ArgoCD
Stage_007/          # (coming) Prometheus + Grafana + Falco
Stage_008/          # (coming) Security audit + portfolio cleanup
```

---

## Career Target

Building toward **Cloud Engineer / Platform Engineering** roles in NYC

**Certifications in progress:**
- AWS Solutions Architect Associate (SAA-C03) — studying alongside Stage 3
- Terraform Associate — after Stage 4
- CKA (Certified Kubernetes Administrator) — after Stage 5

---


