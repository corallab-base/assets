import importlib.resources

def get_resource_path(path):
    if hasattr(importlib.resources, "files"):
        return importlib.resources.files("corallab_assets").joinpath(path)
    else:
        result = None

        ## ONE METHOD:
        # path_parts = path.split("/")
        # module = ".".join(["corallab_assets"] + path_parts[:-1])
        # f = path_parts[-1]
        # with importlib.resources.path(module, f) as f:
        #     result = f

        with importlib.resources.path("corallab_assets", "") as f:
            result = f

        return result.joinpath(path)
