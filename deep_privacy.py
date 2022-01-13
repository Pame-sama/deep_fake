#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('git clone https://github.com/hukkelas/DeepPrivacy')
get_ipython().system(' cd DeepPrivacy')


# In[2]:


get_ipython().system('wget -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh')
get_ipython().system('chmod +x Anaconda3-5.1.0-Linux-x86_64.sh')
get_ipython().system('bash ./Anaconda3-5.1.0-Linux-x86_64.sh -b -f -p /usr/local')
get_ipython().system('conda install pytorch torchvision cudatoolkit=10.0 -c pytorch -y')
get_ipython().system('conda install cython numpy scikit-learn>=0.2 matplotlib pandas tqdm tflib autopep8 moviepy opencv-python requests -y ')
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages/')


# In[4]:


get_ipython().run_cell_magic('writefile', 'setup.sh', '\ngit clone https://github.com/NVIDIA/apex\ncd apex\npip install -v --no-cache-dir ./')


# In[5]:


get_ipython().system(' mv DeepPrivacy/deep_privacy . && mkdir -p models/large/checkpoints && mv DeepPrivacy/models/isvc_large/config.yml models/large')
# Download checkpoint and save it to models/large/checkpoints


# In[6]:


get_ipython().system('sh setup.sh')


# 

# In[8]:


from google.colab import auth
auth.authenticate_user()
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
import matplotlib.pyplot as plt

drive_service = build('drive', 'v3')

def download_file(file_id, filepath):
    request = drive_service.files().get_media(fileId=file_id)
    downloaded = io.BytesIO()
    downloader = MediaIoBaseDownload(downloaded, request)
    done = False
    while done is False:
        # _ is a placeholder for a progress object that we ignore.
        # (Our file is small, so we skip reporting progress.)
        _, done = downloader.next_chunk()

    downloaded.seek(0)
    with open(filepath, "wb") as fp:
        fp.write(downloaded.read())
    #rint('Downloaded file contents are: {}'.format(downloaded.read()))
download_file("101g6XHACr0cwgXBf8LgFfNrHR3OPLBHv", "models/large/checkpoints/step_40000000.ckpt")


# In[9]:


get_ipython().system(' mkdir deep_privacy/detection/dsfd/weights')
download_file("1WeXlNYsM6dMP3xQQELI-4gxhwKUQxc3-", "deep_privacy/detection/dsfd/weights/WIDERFace_DSFD_RES152.pth")


# In[10]:


get_ipython().system(' ls ')


# In[11]:


from deep_privacy.config_parser import load_config
from deep_privacy.inference import infer, deep_privacy_anonymizer
import torch


# In[12]:


config = load_config("models/large/config.yml")
checkpoint = torch.load("models/large/checkpoints/step_40000000.ckpt")
generator = infer.init_generator(config, checkpoint)


# In[13]:


anonymizer = deep_privacy_anonymizer.DeepPrivacyAnonymizer(generator,
                                                           batch_size=32,
                                                           use_static_z=True,
                                                           keypoint_threshold=.1,
                                                           face_threshold=.6)


# # Anonymize images
# 

# In[14]:


# Download images
get_ipython().system(' mkdir images')
get_ipython().system(' wget https://www1.pictures.stylebistro.com/gi/Lupita+Nyong+o+Short+Hairstyles+Side+Parted+ZG8osyjW8YQl.jpg -O images/example.jpg')
plt.imshow(plt.imread("images/example.jpg"))


# In[15]:


anonymizer.anonymize_image_paths(["images/example.jpg"], ["images/example_anonymized.jpg"])


# In[16]:


plt.figure(figsize=(8,16))
plt.imshow(plt.imread("images/example_anonymized.jpg"))


# In[17]:


plt.figure(figsize=(16,40))
plt.imshow(plt.imread("images/example_anonymized_detected_left_anonymized_right.jpg"))


# In[ ]:




