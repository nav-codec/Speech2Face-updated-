import pkg_resources

# List of packages to check
packages_to_check = [
    'h5py',
    'pandas',
    'numpy',
    'dlib',
    'scipy',
    'scikit-image',
    'scikit-learn',
    'matplotlib',
    'Pillow',
    'imageio',
    'imagesize',
    'python-dateutil',
    'pytest',
    'librosa',
    'numba',
    'numexpr',
    'pickleshare',
    'audioread',
    'yt-dlp',
    'face-recognition',
    'face-recognition-models',
    'Keras-Applications',
    'Keras-Preprocessing',
    'tensorboard',
    'tensorflow-gpu',
    'tensorflow-estimator',
    'ffmpeg',
    'keras',
    'keras_vggface'
]

# Get the installed packages
installed_packages = pkg_resources.working_set
installed_packages_dict = {i.key: i.version for i in installed_packages}

# Check for inconsistencies
for package in packages_to_check:
    if package in installed_packages_dict:
        print(f"{package}=={installed_packages_dict[package]}")
    else:
        print(f"{package} is not installed.")
