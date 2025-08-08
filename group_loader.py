import boto3
import yaml
from dataclasses import dataclass, field
from typing import List

dataclass
class Group:
    name: str
    id: str
    members: List[str] = field(default_factory=list)

def read_groups_from_s3(bucket: str, key: str) -> List[Group]:
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    data = yaml.safe_load(content)

    groups = []
    for group_dict in data.get('groups', []):
        name = group_dict.get('name')
        gid = group_dict.get('id')
        members = group_dict.get('members', [])  # Default to empty list if not present
        group = Group(name=name, id=gid, members=members)
        groups.append(group)
    return groups