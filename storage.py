from pathlib import Path

class Storage:
    def __init__(self, storagePath: Path):
        self.storage_path: Path = storagePath

    def get(self, filename: str) -> Path:
        path = self.__get_image_path(filename)
        if self.__validate_image_path(path):
            return self.storage_path / filename
            
    def delete(self, filename: str):
        path = self.get_image_path(filename)
        if self.validate_image_path(path):
            path.unlink()

    def list(self):
        return sorted(self.storage_path.glob("*.jpg"))
    
    def __get_image_path(self, image_id: str):
        return self.storage_path / image_id
    
    def __validate_image_path(self, path: str):
        return path.exists()
            
        
    
