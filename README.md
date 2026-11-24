# Bioinformatics Algorithms Coursework

Python solutions to bioinformatics algorithm problems from the [Rosalind](https://rosalind.info/problems/list-view/?location=bioinformatics-textbook-track) textbook track, completed for an undergraduate bioinformatics course at Shahjalal University of Science and Technology. Each solution reads a Rosalind input file and writes the answer.

## Topics covered

| Location | Problems |
|---|---|
| `Chapter_1.ipynb` – `Chapter_3.ipynb` | Pattern counting, frequent words, reverse complement and other Chapter 1–3 problems (ba1–ba3), partly using Biopython |
| `lab day 1`, `lab day 2` | Introductory lab notebook and script |
| `lab day 3` | Genome skew, clump finding, median string, profile-most-probable k-mer, GreedyMotifSearch |
| `lab day 4` | RandomizedMotifSearch, GibbsSampler, k-mer composition, genome-path reconstruction, overlap graph, De Bruijn graphs |
| `lab day 5` | RNA translation, peptide encoding, theoretical spectrum, peptide counting, Eulerian cycle, string reconstruction, contig generation |
| `lab day 6` | Cyclic peptide scoring, spectral convolution, Leaderboard and Convolution cyclopeptide sequencing, suffix array, trie construction and matching |
| `lab day 7` | Burrows–Wheeler transform and inversion, last-to-first mapping, BWT pattern matching, suffix-array pattern matching |

Each lab folder contains the individual `.py` solutions, the Rosalind dataset files (`rosalind_*.txt`) and a notebook combining that day's work.

## Running a solution

```bash
git clone https://github.com/hasansust32/Bio-informatics_Assignment.git
cd "Bio-informatics_Assignment/lab day 7"
pip install biopython        # only needed by some notebook cells
python "1. Construct the Burrows-Wheeler Transform of a String.py"
```

Scripts expect their `rosalind_*.txt` input in the working directory.

## Author

**S M Mahamudul Hasan** · [GitHub](https://github.com/hasansust32) · [Portfolio](https://www.hasansm.com/)
