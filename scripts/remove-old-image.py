"""
This script is based on this documentation: 
https://docs.github.com/en/rest/packages/packages?apiVersion=2022-11-28
"""

import os
import requests
from requests.auth import HTTPBasicAuth

def removed_previous_commit_sha_image(user, registry, pr_tag, github_token, container_name, current_commit):
    auth = HTTPBasicAuth(user, github_token)

    container_path = f"{registry}/{container_name}:{pr_tag}"
    org = registry.split("/")[1]

    # Get the digest
    url_get_digest = f"https://api.github.com/orgs/{org}/packages/container/{container_name}/versions"
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(url_get_digest, headers=headers, auth=auth)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error getting the digests for image {container_path} : {e}")
        exit(1)

    # Find the digest with the corresponding tag and delete the previous one
    digest = None
    for version in response.json():
        if pr_tag in version['metadata']['container']['tags'] and current_commit not in version['metadata']['container']['tags']:
            digest = version['digest']
            break

    if not digest:
        print(f"Container name {container_name} not found or the only digest found was the current one. If that is the case, you can ignore this error.")
        exit(1)
    else:
        print(f"Digest found for tag {container_path}: {digest}")

    # Get all tags for this digest
    url_get_tags = f"https://api.github.com/orgs/{org}/packages/container/{container_name}/versions"
    response = requests.get(url_get_tags, headers=headers, auth=auth)
    response.raise_for_status()

    # Delete the old container (based on the digest)
    for version in response.json():
        if version['digest'] == digest:
            for tag in version['metadata']['container']['tags']:
                url_delete_tag = f"https://api.github.com/orgs/{org}/packages/container/{container_name}/versions/{version['id']}"
                response = requests.delete(url_delete_tag, headers=headers, auth=auth)
                if response.status_code == 204:
                    print(f"Tag {tag} delete succesfully.")
                else:
                    print(f"Error delete the tag {tag}: {response.status_code}")

if __name__ == "__main__":
    registry = os.getenv("REGISTRY")
    github_token = os.getenv("GITHUB_TOKEN")
    container_name = os.getenv("CONTAINER_NAME")
    pr_tag = os.getenv("PR_TAG")
    user = os.getenv("USER")
    current_commit = os.getenv("CURRENT_COMMIT")

    removed_previous_commit_sha_image(user, registry, pr_tag, github_token, container_name)