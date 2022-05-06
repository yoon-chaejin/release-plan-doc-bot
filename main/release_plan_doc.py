from main.file import File


class ReleasePlanDoc:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            exec(f'self.{key} = "{value}"')

