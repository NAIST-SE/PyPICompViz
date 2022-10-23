# Research Artifact - Visualizing Contributor Code Competency for PyPI Libraries: Preliminary Results

> This is a research artifact for the 29th Asia-Pacific Software Engineering Conference (APSEC 2022)  paper "**Visualizing Contributor Code Competency for PyPI Libraries: Preliminary Results**".

This artefact is about the visualization based on [Treemap Charts](https://plotly.com/python/treemaps/) to show the relationship between proficient code, contributors, and files in four PyPI projects. 

## Abstract

Python is known to be used by beginners to professional programmers. Python provides functionality to its community of users through PyPI libraries, that allow developers to reuse functionalities to an application. However, it is unknown the extent to which these PyPI libraries require proficient code in their implementation. We conjecture that PyPI contributors may decide to implement more advanced Pythonic code, or stick with more basic Python code. Are complex codes only committed by few contributors, or only to specific files? The new idea in this paper is to confirm who and where complex code is implemented. Hence, we present a visualization to show the relationship between proficient code, contributors, and files. Analyzing four PyPI projects, we are able to explore which files contain more elegant code, and which contributors committed to these files. Our results show that most files contain more basic competency files, and that not every contributor contributes competent code. We show how our visualization is able to summarize such information, and opens up different possibilities for understanding how to make elegant contributions.



## Original dataset resources

| Analyzed project                            | #dependencies |
| :-----------------------------------------: | :-----------: |
| [Requests](https://github.com/psf/requests) | 41.2K         |
| [Flask](https://github.com/pallets/flask)   | 5.5K          |
| [Jinja2](https://github.com/pallets/jinja)  | 6.16K         |
| [Pytz](https://github.com/stub42/pytz)      | 4.41K         |

# Contents
## Dataset
Our dataset for each four projects:
- Requests dataset: `dataset_flask.csv`
- Flask dataset: `dataset_flask.csv`
- Jinja2 dataset: `dataset_jinja2.csv`
- Pytz dataset: `dataset_pytz.csv`

## Visualization

In this study, we design the tree map to show two visualizations, which have different patterns of categories. 

- `file-level_visualization.py`. The file level visualization follows the category pattern as **Project → Filename → Competency Score**
- `contributor-level visualization.py`. The contributor level visualization follows the category pattern as **Project → Contributor → Competency Score**

Note that the area size refers to the number of elements of competency found in each file.

# Visualization Preview
## Visualization at the File-Level. 
green color represents the A and B competency, purple represents the C1 - Effective, and red represents the C2 - Mastery.

- Requests

![Requests_file](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/requests_file.png)

- Flask

![Flask_file](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/flask_file.png)

- Jinja2

![Jinja2_file](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/jinja2_file.png)

- Pytz

![Pytz_file](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/pytz_file.png)

## Visualization at the Contributor-Level. 
green color represents the A and B competency, purple represents the C1 - Effective, and red represents the C2 - Mastery.

- Requests

![Requests_cont](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/requests_cont.png)

- Flask

![Flask_cont](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/flask_cont.png)

- Jinja2

![Jinja2_cont](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/jinja_cont.png)

- Pytz

![Pytz_cont](https://github.com/NAIST-SE/PyPICompViz/blob/main/visualization/preview/pytz_cont.png)


# Authors
- Indira Febriyanti
- [Raula Gaikovina Kula](https://raux.github.io/)
- Ruksit Rojpaisarnkit
- Kanchanok Kannee
- [Yusuf Sulistyo Nugroho](https://yusufsn.github.io/)
- [Kenichi Matsumoto](https://matsumotokenichi.github.io/)
