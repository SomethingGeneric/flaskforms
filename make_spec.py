from form_generator import form_generator
import yaml

fg = form_generator()

spec_fn = input("Output filename: ")

action = ""

components = []

while action != "exit":
    action = input("(A)dd component, or 'exit'? : ")
    if action != 'exit':
        new_comp = {
            "component": "something",
            "form_id": "some_id",
            "help_text": "something useful"
        }
        comp_type = ""
        if not fg.check_component(comp_type):
            comp_type = input("Component type? : ")
        new_comp['component'] = comp_type
        new_comp['form_id'] = input("form id? : ")
        if fg.has_help_text(comp_type):
            new_comp['help_text'] = input("Help text? : ")
        components.append(new_comp)

with open(spec_fn, "w") as f:
    f.write(yaml.dump(components))
