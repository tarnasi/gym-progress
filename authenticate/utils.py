from time import time


def user_avatars(instance, filename):
    # file will be uploaded to MEDIA_ROOT / users/<id>_<timestamp>
    post_id = instance.id
    timestamp = str(int(time()))
    ext_position = filename.rfind('.') + 1
    extension = filename[ext_position:]
    return f'users/{post_id}_{timestamp}.{extension}'
