from .models import Song
from ...utils import bench_setup

class ModelValidate:

    def setup(self):
        bench_setup()
        self.model = Song(name="abc")
    
    def time_model_validate(self):
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()
        self.model.full_clean()