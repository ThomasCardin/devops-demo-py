# Devops-demo-py

## Test .github/workflows/push-dockerfile.yml with act

```bash
act workflow_call -s GITHUB_TOKEN=<GITHUB-TOKEN> -W .github/workflows/push-dockerfile.yml --eventpath .github/event.json
```