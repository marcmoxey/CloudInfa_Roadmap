
---

## Date: 07/18/2026


**IAM — Identity & Access Management:**

- Global service (not region-specific)
- **Root account** — created by default, should never be used or shared for daily work
- **Users** — individual people in an organization; can be organized into groups

**IAM Permissions:**

- Users/groups get assigned JSON documents called **policies**
- Policies define what a user CAN do
- Core principle: **least privilege** — never grant more permission than the user actually needs

**Policy inheritance:**

- Attach a policy at the GROUP level → every member inherits it
- **Inline policies** — attached directly to ONE specific user only
- If a user belongs to multiple groups, they inherit ALL policies from ALL their groups

**Policy JSON structure:**

```json
{
  "Version": "2012-10-17",
  "Id": "optional-policy-id",
  "Statement": [
    {
      "Sid": "optional-statement-id",
      "Effect": "Allow",
      "Principal": "...",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::my-bucket/*"],
      "Condition": { }
    }
  ]
}
```

**IAM Password Policy + MFA:**

- Set minimum length, require specific character types, allow password changes, force periodic password changes, prevent password reuse
- **MFA** = something you know (password) + something you have (device) — if the password is compromised, the account still isn't
- MFA device types: Virtual MFA device, U2F security key, hardware key fob, hardware key fob for GovCloud specifically

**How users access AWS:**

- **Console** — password + MFA
- **CLI** — protected by access keys
- **SDK** — code-based access, also protected by access keys
- Access Key ID = like a username, Secret Access Key = like a password — both are secrets, never share

**IAM Roles (for AWS services, not people):**

- Assigns permissions to a SERVICE rather than a user
- Common examples: EC2 instance roles, Lambda function roles, CloudFormation roles

**IAM Security Tools:**

- **IAM Credentials Report** (account-level) — lists all users and their credential status
- **IAM Access Advisor** (user-level) — shows which service permissions a user has and when they last used each one; useful for tightening overly broad permissions

**IAM Best Practices:**

- Never use root except for initial account setup
- One physical person = one IAM user (no shared logins)
- Assign users to groups, assign permissions to groups (not individual users directly)
- Enforce a strong password policy + MFA
- Use roles for AWS services, not hardcoded credentials
- Use access keys only for CLI/SDK programmatic access
- Regularly audit with IAM Credentials Report + Access Advisor

**Learned:** This is the theory behind everything I already did hands-on setting up `marc-cli`: I created an IAM user specifically for CLI use (not console), attached `AdministratorAccess` directly rather than through a group (technically against best practice for a real team environment, but fine for a personal single-user lab), and generated access keys specifically for CLI authentication — exactly matching "Access Keys are protected... user manages their own access keys" from these notes.

The least-privilege principle explains why Stage 4 will eventually require me to scale back from `AdministratorAccess` to a scoped-down policy — starting broad and manually tightening based on IAM Access Advisor data (what I actually used) is a legitimate, real-world approach to reaching least privilege, not just a theoretical ideal.

---


