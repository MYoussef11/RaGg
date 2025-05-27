from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os

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

    def generate_unique_filepath(self, original_filename: str, project_id: str):

        # Generate a unique filename using the project ID and original filename
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_filename = self.get_cleaned_filename(
            original_filename=original_filename
            )
        
        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_filename
        )

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_filename
            )

        return new_file_path, random_key + "_" + cleaned_filename

    def get_cleaned_filename(self, original_filename: str):
        # Remove any special characters and spaces from the filename, except for underscores and .
        cleaned_filename = re.sub(r'[^\w.]', '', original_filename.strip())

        # replace spaces with underscores
        cleaned_filename = cleaned_filename.replace(" ", "_")

        return cleaned_filename
    
        