from enum import Enum

class ResponseSignal(Enum):
    """Enum for response signals."""
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_TOO_LARGE = "file_size_too_large"
    FILE_UPLOADED_SUCCESSFULLY = "file_uploaded_successfully"
    FILE_UPLOADED_FAILED = "file_uploaded_failed"
    FILE_VALIDATION_SUCCESS = "file_validation_success"
