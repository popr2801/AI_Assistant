from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    password_hash = models.CharField(max_length = 256)
    
class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'files')
    uploaded_file = models.FileField(upload_to='uploads/')
    file_content = models.TextField(default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def get_file_name(self):
        return self.uploaded_file.name.split('/')[-1]
    

