# EXACT-Sync
Rest API sync with the EXACT Server https://github.com/ChristianMarzahl/Exact

[Browsable-API](https://documenter.getpostman.com/view/11308910/TVYF6xZo)

## Example Notebooks

In the folder examples

## Pip

pip install EXCAT-Sync

## Tests

with a lot of implementation examples
/exact_sync/v1/test


### Basic features:

#### Connect to server

```python
configuration = Configuration()
configuration.username = 'exact'
configuration.password = 'exact'
configuration.host = "http://127.0.0.1:8000"

client = ApiClient(configuration)

image_sets_api = ImageSetsApi(client)
annotations_api = AnnotationsApi(client)
annotation_types_api = AnnotationTypesApi(client)
images_api = ImagesApi(client)
product_api = ProductsApi(client)
team_api = TeamsApi(client)
```


#### Get image set information
```python
image_sets = image_sets_api.list_image_sets(name="cluster_asthma_imageset")
image_sets
```

#### Upload image to image set

```python
image_type = int(Image.ImageSourceTypes.DEFAULT)
image = images_api.create_image(file_path=target_file, image_type=image_type, image_set=image_set.id).results[0]
```

##### Donwload image from image set

```python
images_api.download_image(id=image_id, target_path=image_path, original_image=True)
```

#### Download image annotations 

```python
annotations_api.list_annotations(pagination=False, async_req=True, image=image.id)
```


