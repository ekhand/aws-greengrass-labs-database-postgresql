from pathlib import Path

HOST_PORT_KEY = "HostPort"
HOST_VOLUME_KEY = "HostVolume"
CONTAINER_IMAGE_KEY = "ContainerImage"
CONTAINER_NAME_KEY = "ContainerName"
CONTAINER_MAPPING_KEY = "ContainerMapping"
DB_CREDENTIAL_SECRET_KEY = "DBCredentialSecret"
POSTGRES_USERNAME_KEY = "POSTGRES_USER"
POSTGRES_PASSWORD_KEY = "POSTGRES_PASSWORD"
POSTGRES_USERNAME_FILE_KEY = "POSTGRES_USER_FILE"
POSTGRES_PASSWORD_FILE_KEY = "POSTGRES_PASSWORD_FILE"
DEFAULT_HOST_PORT = "5432"
DEFAULT_CONTAINER_NAME = "greengrass_postgresql"
DEFAULT_HOST_VOLUME = Path().joinpath("postgresql").resolve()
DEFAULT_CONTAINER_PORT = "5432/tcp"
DEFAULT_DB_NAME = "postgres"
POSTGRES_COMMAND_DO_NOT_CHANGE = "postgres"
POSTGRES_DB_KEY = "POSTGRES_DB"
DEFAULT_CONTAINER_VOLUME = "/var/lib/postgresql/data"
DEFAULT_CONTAINER_IMAGE = "postgres:alpine3.16"
POSTGRES_SERVER_CONFIGURATION_FILES_KEY = "ConfigurationFiles"
SUPPORTED_CONFIGURATION_FILES = {"postgresql.conf": "config_file", "pg_hba.conf": "hba_file", "pg_ident.conf": "ident_file"}
CUSTOM_FILES = "/custom_files"
SECRETS_KEY = "secrets"
