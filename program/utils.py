from time import time


def program_images(instance, filename):
    # file will be uploaded to MEDIA_ROOT / programs/<id>_<timestamp>
    program_id = instance.id
    timestamp = str(int(time()))
    ext_position = filename.rfind('.') + 1
    extension = filename[ext_position:]
    return f'programs/{program_id}_{timestamp}.{extension}'
