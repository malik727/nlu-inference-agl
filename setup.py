import io
import os

from setuptools import setup, find_packages

packages = [p for p in find_packages()
            if "tests" not in p and "debug" not in p]

root = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(root, "nlu_inference_agl", "__about__.py"),
             encoding="utf8") as f:
    about = dict()
    exec(f.read(), about)

required = [
    "deprecation>=2.0,<3.0",
    "enum34>=1.1,<2.0; python_version<'3.4'",
    "funcsigs>=1.0,<2.0; python_version<'3.4'",
    "future>=0.16,<0.18",
    "numpy>=1.15,<2.0",
    "num2words>=0.5.6,<0.6",
    "pathlib>=1.0,<2.0; python_version<'3.4'",
    "pyaml>=17.0,<20.0",
    "requests>=2.0,<3.0",
    "scipy>=1.0,<2.0",
    "threadpoolctl>=2.0.0; python_version>='3.6'",
    "scikit-learn>=0.20,<0.21; python_version<'3.6'",
    "scikit-learn==0.22.2.post1; python_version>='3.6'",
    "sklearn-crfsuite>=0.3.6,<0.4",
]

extras_require = {
    "metrics": [
        "snips-nlu-metrics>=0.14.1,<0.15",
    ]
}

setup(name=about["__title__"],
      description=about["__summary__"],
    #   long_description=readme,
      version=about["__version__"],
      author=about["__author__"],
      author_email=about["__email__"],
      license=about["__license__"],
      url=about["__github_url__"],
      project_urls={
        #   "Documentation": about["__doc_url__"],
          "Source": about["__github_url__"],
          "Tracker": about["__tracker_url__"],
      },
      install_requires=required,
      extras_require=extras_require,
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
      ],
      keywords="nlu nlp language machine learning text processing intent",
      packages=packages,
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
      include_package_data=True,
      entry_points={
          "console_scripts": [
              "nlu-inference-agl=nlu_inference_agl.cli:main"
          ]
      },
      zip_safe=False)