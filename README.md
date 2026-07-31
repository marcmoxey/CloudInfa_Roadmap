# Cloud Infrastructure Roadmap

A self-paced, hands-on roadmap from Software Engineer to Cloud Infrastructure / Site Reliability Engineer — built entirely on real hardware I own and operate.

**Current status:** Stage 3 (AWS) — exam prep phase · Stages 1-2 complete

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
python3 labcheck.py --host <ec2-ip> --user ec2-user --key /path/to/key.pem
```

Tested successfully against both a home server and a live AWS EC2 instance in the same run.

**Skills:** Python, argparse, Paramiko, regex, getpass, datetime, exception handling

---

### 🔵 Stage 3 — AWS (Exam Prep)
Standing up real infrastructure in the cloud, now studying for AWS Solutions Architect Associate.

- AWS CLI configured with an IAM user (`marc-cli`)
- EC2 instances launched, SSH'd into, and terminated (both Ubuntu and Amazon Linux)
- S3 bucket created, files uploaded/downloaded, deleted
- `s3_audit.py` — Boto3 script that scans all S3 buckets and flags any with public access enabled
- `EC2_audit.py` — Boto3 script that scans **every AWS region** for running EC2 instances and reports a total count
- **IAM least-privilege tested hands-on:** scoped an IAM user down to `ReadOnlyAccess`, confirmed reads succeeded and writes returned `Access Denied`
- **Custom VPC built from scratch:** VPC → public subnet → Internet Gateway → route table (`0.0.0.0/0` → IGW) → EC2 launched inside it → SSH confirmed working end-to-end
- **VPC Peering configured** between the custom VPC and the account's default VPC, with routes added on both sides and connectivity confirmed via `curl` between instances

**Currently:** full sequential review of AWS SAA course content + practice exams, ahead of sitting the AWS SAA-C03 exam.

**Skills:** EC2, S3, VPC (subnets, route tables, IGW, peering), IAM (users, least-privilege policies), AWS CLI, Boto3, multi-region scripting

---

### 🔲 Stage 4 — Terraform + IaC
Rebuild everything from Stage 3 as code. One command to provision, one to destroy.

- Terraform modules for EC2, S3, VPC, IAM
- IaC scanning with Checkov and tfsec
- Ansible playbook for Beelink configuration management
- Terraform Associate exam
- CompTIA Security+ study (parallel track — keeps govtech/DMV market open)

---

### 🔲 Stage 5 — Docker + Kubernetes
Turn the Beelink into a small Kubernetes cluster.

- k3s on the Beelink
- Helm charts, Pod Security Standards, OPA Gatekeeper
- External Secrets Operator (AWS Secrets Manager → k3s pods)
- Container image scanning with Trivy
- Deploy a game server (Minecraft/Valheim) with autoscaling tuned for player load

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
- Defined SLOs for the game server workload; disaster recovery drill with timed restore-from-backup
- Incident postmortem documentation

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
Stage_003/          # AWS — Boto3 scripts (s3_audit.py, EC2_audit.py), VPC/IAM work
Stage_004/          # (coming) Terraform + Ansible
Stage_005/          # (coming) Docker + Kubernetes manifests
Stage_006/          # (coming) GitHub Actions + ArgoCD
Stage_007/          # (coming) Prometheus + Grafana + Falco
Stage_008/          # (coming) Security audit + portfolio cleanup
Python.md           # Python learning journal — real bugs, real fixes
```

---

## Career Target

Building toward **Cloud Infrastructure / Site Reliability Engineering**, with a specific interest in gaming and media infrastructure — scaling, monitoring, and disaster recovery for systems under real user load.

**Primary market:** NYC private sector · **Secondary:** DC/Northern Virginia (govtech) and Austin, TX

Expected job search: Stage 5-6 (approx. November 2026)

**Certifications:**
- AWS Solutions Architect Associate (SAA-C03) — in progress
- Terraform Associate — after Stage 4
- CompTIA Security+ — parallel track for DMV/govtech
- CKA (Certified Kubernetes Administrator) — after Stage 5

---

## Security Notes

- No credentials, API keys, or `.pem` files are committed to this repo
- `labcheck.py` uses `getpass` for password input — never stores credentials
- AWS access keys stored in `~/.aws/credentials` (not in repo)
- IAM least-privilege practiced hands-on (see Stage 3) — not just theoretical

