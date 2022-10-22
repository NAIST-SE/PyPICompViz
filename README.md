# Research Artifact - Visualizing Contributor Code Competency for PyPI Libraries: Preliminary Results

This is a research artifact for the 29th Asia-Pacific Software Engineering Conference (APSEC 2022) 
paper "**Visualizing Contributor Code Competency for PyPI Libraries: Preliminary Results**".

This is the visualization based on [Treemap Charts](https://plotly.com/python/treemaps/) to show the relationship between proficient code, contributors, and files in four PyPI projects. 
Analyzing four PyPI projects, we are able to explore which files contain more elegant code, and which contributors committed to these files. 
Our results show that most files contain more basic competency files, and that not every contributor contributes competent code. 
We show how are visualization is able to summarize such information, and opens up different possibilities for understanding how to make elegant contributions.



## Data Resources for study

| Analyzed project                            | #dependencies |
| :-----------------------------------------: | :-----------: |
| [Requests](https://github.com/psf/requests) | 41.2K         |
| [Flask](https://github.com/pallets/flask)   | 5.5K          |
| [Jinja2](https://github.com/pallets/jinja)  | 6.16K         |
| [Pytz](https://github.com/stub42/pytz)      | 4.41K         |

## Dataset
Our dataset for each four projects:
- Requests dataset: `dataset_flask.csv`
- Flask dataset: `dataset_flask.csv`
- Jinja2 dataset: `dataset_jinja2.csv`
- Pytz dataset: `dataset_pytz.csv`

# Visualization

In this study, we design the tree map to show two visualizations, which have different patterns of categories.
- File-level visualization. The file level visualization follows the category pattern as Project → Filename → Competency Score
- Contributor-level visualization. The contributor level visualization follows the category pattern as Project → Contributor → Competency Score

Note that the area size refers to the number of elements of competency found in each file.

# Authors
- Indira Febriyanti
- Raula Gaikovina Kula
- Ruksit Rojpaisarnkit
- Kanchanok Kannee
- Yusuf Sulistyo Nugroho
- Kenichi Matsumoto
