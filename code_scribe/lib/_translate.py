# Prompt engineering for building diffusion stencils for constant and variable coefficient equation

# Import libraries
import os, sys, toml, json, importlib

from typing import Optional
from alive_progress import alive_bar


def save_prompt(mapping, prompt):

    chat_template = toml.load(prompt)["chat"]
    print("Saving custom prompts per file")

    with alive_bar(len(mapping[0]), bar="blocks") as bar:

        for fsource, draft, ptoml in zip(mapping[0], mapping[3], mapping[4]):

            bar.text(fsource)
            bar()

            source_code = []
            draft_code = []

            with open(fsource, "r") as sfile:

                is_comment = False
                for line in sfile.readlines():
                    is_comment = False

                    if line.strip().lower().startswith(("c", "!!", "!")) and (
                        not line.strip().lower().startswith(("complex"))
                    ):
                        is_comment = True

                    if not is_comment:
                        source_code.append(line)

            if os.path.isfile(draft):
                with open(draft) as dfile:
                    for line in dfile.readlines():
                        draft_code.append(line)

            saved_prompt = chat_template[-1]["content"]
            chat_template[-1]["content"] += (
                "\n" + "<source>\n" + "".join(source_code) + "</source>"
            )
            if draft_code:
                chat_template[-1]["content"] += (
                    "\n\n" + "<draft>\n" + "".join(draft_code) + "</draft>"
                )

            with open(ptoml, "w") as pdest:
                for instance in chat_template:
                    pdest.write("[[chat]]\n")
                    pdest.write(f'role = "{instance["role"]}"\n')
                    pdest.write(f'content = """\n{instance["content"]}"""\n\n')

            chat_template[-1]["content"] = saved_prompt


def translate(mapping, model, prompt):

    transformers = importlib.import_module("transformers")
    torch = importlib.import_module("torch")

    max_new_tokens = 4096
    batch_size = 8
    max_length = None
    chat_template = toml.load(prompt)["chat"]

    print("Starting neural conversion process")

    tokenizer = transformers.AutoTokenizer.from_pretrained(model)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        # torch_dtype=torch.float16,
        device=-1,
    )

    with alive_bar(len(mapping[0]), bar="blocks") as bar:

        for fsource, csource, finterface, draft in zip(
            mapping[0], mapping[1], mapping[2], mapping[3]
        ):

            bar.text(fsource)
            bar()

            if not os.path.isfile(csource):

                source_code = []
                draft_code = []

                with open(fsource, "r") as sfile:

                    is_comment = False
                    for line in sfile.readlines():
                        is_comment = False

                        if line.strip().lower().startswith(("c", "!!", "!")) and (
                            not line.strip().lower().startswith(("complex"))
                        ):
                            is_comment = True

                        if not is_comment:
                            source_code.append(line)

                if os.path.isfile(draft):
                    with open(draft) as dfile:
                        for line in dfile.readlines():
                            draft_code.append(line)

                with open(csource, "w") as cdest, open(finterface, "w") as fdest:

                    saved_prompt = chat_template[-1]["content"]

                    chat_template[-1]["content"] += (
                        "\n" + "<source>\n" + "".join(source_code) + "</source>"
                    )

                    if draft_code:
                        chat_template[-1]["content"] += (
                            "\n\n" + "<draft>\n" + "".join(draft_code) + "</draft>"
                        )

                    results = pipeline(
                        chat_template,
                        max_new_tokens=max_new_tokens,
                        max_length=max_length,
                        batch_size=batch_size,
                        # temperature=temperature,
                        # top_p=top_p,
                        # do_sample=True,
                        eos_token_id=tokenizer.eos_token_id,
                        pad_token_id=50256,
                    )

                    for result in results:
                        cdest.write(result["generated_text"][-1]["content"])
                        # code_block_indices = []
                        # for index, line in enumerate(output_lines):
                        #    if line[:2] == "```":
                        #        code_block_indices.append(index)
                        #
                        # if len(code_block_indices) > 2:
                        #    api.display_output(
                        #        "More than one code blocks in LLM output"
                        #    )
                        #    raise NotImplementedError
                        #
                        # for index, line in enumerate(output_lines):
                        #    if (
                        #        index < code_block_indices[0]
                        #        or index > code_block_indices[1]
                        #    ):
                        #        destination.write(f'// {line}"\n"')
                        #    else:
                        #        destination.write(f'{line}"\n"')
                    chat_template[-1]["content"] = saved_prompt

            else:
                continue
