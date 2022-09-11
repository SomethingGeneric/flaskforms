import os, yaml, sys


class form_generator:
    def __init__(self):
        self.components_dir = "components/"

    def make_form(self, output_fname, spec_fname):
        if os.path.exists(spec_fname):
            objs = yaml.safe_load(open(spec_fname).read())
            html = "<form>"

            for obj in objs:
                if not self.check_component(obj['component']):
                    print(f"No such component: {obj['component']}")
                    sys.exit(1)
                else:
                    component_html = self.get_component(obj['component'])
                    new = component_html.replace("FORM_ID", obj['form_id'])
                    if 'FORM_HELP_TEXT' in new:
                        new = new.replace("FORM_HELP_TEXT", obj['help_text'])
                    html += new

            html += "<button type=\"submit\" class=\"btn btn-primary\">Submit</button></form>"

            with open(output_fname, "w") as f:
                f.write(html)

    def get_component(self, name):
        return open(f"{self.components_dir}/{name}.html").read()

    def check_component(self, name):
        if not os.path.exists(f"{self.components_dir}/{name}.html"):
            return False
        return True

    def has_help_text(self, name):
        if self.check_component(name):
            html = self.get_component(name)
            if "FORM_HELP_TEXT" in html:
                return True
        return False

