import boto3

s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()
buckets = response['Buckets']

print(f'Found {len(buckets)} bucket(s)\n')

for bucket in buckets:
    name = bucket['Name']
    
    # Check if public access is blocked
    try:
        public_access = s3.get_public_access_block(Bucket=name)
        config = public_access['PublicAccessBlockConfiguration']
        
        is_blocked = all([
            config['BlockPublicAcls'],
            config['IgnorePublicAcls'],
            config['BlockPublicPolicy'],
            config['RestrictPublicBuckets'],
        ])
        
        status = 'Private' if is_blocked else 'PUBLIC - REVIEW NEEDED'
        
    except Exception:
        status = 'No public access block configured'
    
    print(f'{name}: {status}')