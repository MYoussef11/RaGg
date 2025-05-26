from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal

class DataController(BaseController):

    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # 1024 * 1024, for MB conversion
    
    def validate_uploaded_file(self, file: UploadFile):

        contents = file.file.read()  # read file content
        file_size = len(contents)    # get size in bytes

        # Reset file pointer if needed for later usage
        file.file.seek(0)

        # Validate content type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        # Validate size
        if file_size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_TOO_LARGE.value

        return True, ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value
