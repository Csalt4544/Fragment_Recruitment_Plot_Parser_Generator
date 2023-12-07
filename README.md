# Fragment_Recruitment_Plot_Parser_Generator
This Python program suite (v1.0) can be utilized to parse through fragment recruitment alignment files generated from either FR-HIT standard output .sop files or any alignment program that may generate a correctly formatted .sam file. Information from parsing is used to create a fragment recruitment plot based on position within the sample genome and percent identity to the reference genome. The sam_FRP.py and sop_FRP.py scripts were designed to accept one command line argument while the sop_composite_FRP_v2.py script was designed to accept four command line arguments. An additional script Converter.py based on BioPython is included to convert FASTQ format sequence files to FASTA format sequence files for use when using certain alignment programs. The converter accepts two command line arguments (original file name/extension and the converted file name/extension).

### Requirements and Dependencies
The Python scripts were created to run using Python 3.0. Two dependencies can be found through the repository: Matplotlib and Biopython. To install the Matplotlib and BioPython libraries, please run the following commands in terminal:

`pip install matplotlib`

`pip install biopython`

### Example Usage

An example command for the sop_composite_FRP_v2.py script may look like:

`$ python ./sop_composite_FRP_v2.py file1.sop file2.sop file3.sop file4.sop graph_title_string`

### Other Information

These scripts and code are free distributed under the GNU 3.0 Public License.
