Dataset **Large Wind Turbines (by Duke Dataplus2020)** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/6/q/jq/Vo23NY8HIlDH0FgPsVSy2KJh1QxVsA1NfnT1NvhkU05EKY3u2vIvnj2MIgRSOszCUUwfXxQyXeSf2O2iM6pz2d4f1ZUcizlCQI7GAut5HZrZokINuryebjzQGlcz.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Large Wind Turbines (by Duke Dataplus2020)', dst_path='~/dtools/datasets/Large Wind Turbines (by Duke Dataplus2020).tar')
```
The data in original format can be 🔗[downloaded here](https://figshare.com/ndownloader/files/24118220)