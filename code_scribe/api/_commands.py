"""Command line interface for Jobrunner"""

import os
from code_scribe import lib


def index(root_dir):
    """
    API command for creating an index for directory tree
    """
    lib.create_scribe_yaml(root_dir)
    return f"Project structure saved to scribe.yaml."


def draft(fortran_file, root_dir):
    """
    API command for creating a draft files
    """
    item_index_list = lib.create_indexes(root_dir)
    message = lib.annotate_fortran_file(fortran_file, item_index_list)
    return message


def translate(filelist, seed_prompt, model, save_prompts):
    """
    API command for creating a draft files
    """
    mapping = lib.create_src_mapping(filelist)
    lib.prompt_translate(mapping, seed_prompt, model=model, save_prompts=save_prompts)
