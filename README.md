# EXACT-Sync
Rest API sync with the EXACT Server https://github.com/ChristianMarzahl/Exact


## Example Notebooks

In the folder examples or:
https://colab.research.google.com/drive/1nOTyAVwzBDMSEAdgjbdpe7isGfeVpusK

### Basic features:

#### Get image set information
```python
username="Demo"
password="demodemo"
serverurl="http://127.0.0.1:8000/"
target_folder = Path('examples/images/') 

manager = ExactManager(username=username,  password=password, serverurl=serverurl)
imageset = manager.retrieve_imagesets()
```

#### Upload image to image set

```python
manager.upload_image_to_imageset(imageset_id=image_set['id'], filename="example.png")
```

##### Donwload image from image set

```python
id = image['id']
name = image['name']
image_path = target_folder/name
manager.download_image(id, image_path, None)# , original_image=True
```

#### Download image annotations 

```python
id = image['id']
annotations = manager.retrieve_annotations(id)
```

## Pip

pip install EXCAT-Sync

