if [ -z "$RESEARCHTOOLS_PYTHON_PATH" ]
then
    export RESEARCHTOOLS_PYTHON_PATH=$RESEARCH_TOOLS_DIR/
    export PYTHONPATH=$RESEARCHTOOLS_PYTHON_PATH:$PYTHONPATH
fi

alias bib-merge="python3 ${RESEARCH_TOOLS_DIR}/researchtools/bibtex/merge_bibtex.py"
alias scopus-csv-filter="python3 ${RESEARCH_TOOLS_DIR}/researchtools/scopus/filter_csv.py"
