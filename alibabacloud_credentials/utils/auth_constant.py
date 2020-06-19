import os

try:
    DEFAULT_CREDENTIALS_FILE_PATH = os.environ['HOME'] + "/.alibabacloud/credentials.ini"
except KeyError:
    DEFAULT_CREDENTIALS_FILE_PATH = os.environ['HOMEPATH'] + "/.alibabacloud/credentials.ini"

INI_ACCESS_KEY_ID = "access_key_id"
INI_ACCESS_KEY_IDSECRET = "access_key_secret"
INI_TYPE = "type"
INI_TYPE_RAM = "ecs_ram_role"
INI_TYPE_ARN = "ram_role_arn"
INI_TYPE_KEY_PAIR = "rsa_key_pair"
INI_PUBLIC_KEY_ID = "public_key_id"
INI_PRIVATE_KEY_FILE = "private_key_file"
INI_PRIVATE_KEY = "private_key"
INI_ROLE_NAME = "role_name"
INI_ROLE_SESSION_NAME = "role_session_name"
INI_ROLE_ARN = "role_arn"
INI_POLICY = "policy"
TSC_VALID_TIME_SECONDS = 3600
DEFAULT_REGION = "region_id"
INI_ENABLE = "enable"
ACCESS_KEY = "access_key"
STS = "sts"
ECS_RAM_ROLE = "ecs_ram_role"
RAM_ROLE_ARN = "ram_role_arn"
RSA_KEY_PAIR = "rsa_key_pair"
BEARER = "bearer"