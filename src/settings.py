from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Large Wind Turbines (by Duke Dataplus2020)"
PROJECT_NAME_FULL: str = "Synthetic Overhead Images and Ground Truth Labels of Large Wind Turbines"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Energy(is_used=False)]
CATEGORY: Category = Category.EnergyAndUtilities(extra=[Category.Aerial(), Category.Satellite()], is_original_dataset=False)

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2020-07-31"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://figshare.com/articles/dataset/Synthetic_Overhead_Images_and_Ground_Truth_Labels_of_Large_Wind_Turbines/12744902"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 666818
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/synthetic-overhead-images-and-ground-truth-Labels-of-large-wind-turbines"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://figshare.com/ndownloader/files/24118220"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = "https://doi.org/10.6084/m9.figshare.12744902.v1"
AUTHORS: Optional[List[str]] = None
AUTHORS_CONTACTS: Optional[List[str]] = ["https://figshare.com/authors/Duke_Dataplus2020/9190670"]


ORGANIZATION_NAME: Optional[Union[str, List[str]]] = ["Duke Dataplus2020"]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = ["https://bigdata.duke.edu/participate/data-plus/"]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
