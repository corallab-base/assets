import importlib.resources

def get_resource_path(path):
    if hasattr(importlib.resources, "files"):
        return importlib.resources.files("corallab_assets").joinpath(path)
    else:
        result = None

        with importlib.resources.path("corallab_assets", "") as f:
            result = f

        return result.joinpath(path)
