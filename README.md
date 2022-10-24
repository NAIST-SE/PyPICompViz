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
Green color represents the A and B competency, purple represents the C1 - Effective, and red represents the C2 - Mastery.

**(1) Requests_file**

<p align = "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/cfe46eaf826b4379985c08db7fdd0d55?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/requests_file.png"></a>
</p>

**(2) Flask_file**

<p align = "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/670b10207c2c440bb29f3f49a5316247?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/flask_file.png"></a>
</p>

**(3) Jinja2_file**

<p align = "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/ddb3a6a05f0a4eda855f2866e10557bc?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/jinja2_file.png"></a>
</p>

**(4) Pytz_file**

<p align= "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/48b50d54a88246dba77dff1f83829607?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/pytz_file.png"></a>
</p>

## Visualization at the Contributor-Level. 
Green color represents the A and B competency, purple represents the C1 - Effective, and red represents the C2 - Mastery.

**(1) Requests_contributor**

<p align= "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/66bd7ccc43c14d98b7c42988a2ceee98?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/requests_cont.png"></a>
</p>

**(2) Flask_contributor**

<p align= "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/da98b4991a4f47c98ea169168771a661?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/flask_cont.png"></a>
</p>

**(3) Jinja2_contributor**

<p align = "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/dc6034853563471e8beb9bc7a9b2e7d4?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/jinja_cont.png"></a>
</p>

**(4) Pytz_contributor**

<p align = "center">
  <a href="https://embed.deepnote.com/27fa03af-3e44-4642-9edc-1e3cf35050ba/068d0cb90f52431cb2b5ce282761fe46/5ef8e0d8f5954203949ebf10cbe0eb8d?height=600"><img width="80%" src="https://naist-se.github.io/PyPICompViz/visualization/preview/pytz_cont.png"></a>
</p>

# Authors
- Indira Febriyanti
- [Raula Gaikovina Kula](https://raux.github.io/)
- Ruksit Rojpaisarnkit
- Kanchanok Kannee
- [Yusuf Sulistyo Nugroho](https://yusufsn.github.io/)
- [Kenichi Matsumoto](https://matsumotokenichi.github.io/)
