import boto3

def get_encryption_key():
    """Fetch encryption key securely from AWS KMS."""
    kms_client = boto3.client('kms')
    response = kms_client.generate_data_key(KeyId='your-key-id', KeySpec='AES_256')
    return response['Plaintext']
