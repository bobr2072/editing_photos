import os


class Settings:

    path = 'imgs'
    path_out = 'imgs_edited'

    def path_to_edited_img(filename):

        clean_name = os.path.splitext(filename)[0]
        return os.path.join(Settings.path_out, f'{clean_name}_edited.jpg')
