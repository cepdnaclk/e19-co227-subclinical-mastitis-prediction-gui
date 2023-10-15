from django import forms

class CustomInputWidget(forms.Widget):
    def __init__(self, attrs=None, input_type='text', width='6', label='', pop_text='', placeholder = '', *args, **kwargs):
        self.input_type = input_type
        self.width = width
        self.label = label
        self.pop_text = pop_text
        self.placeholder = placeholder
        self.attrs = attrs
        super().__init__(attrs, *args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        input_html = ""

        value_exist = f"value='{value}'" if value else ""

        if self.attrs:
            for attr_name, attr_value in self.attrs.items():
                input_html = input_html.replace('>', f' {attr_name}="{attr_value}">')
        

        if self.input_type == 'text':
            input_html = f"""
                <input type="text" class="form-control" name="{name}" id="{name}" aria-describedby="{name}_help" placeholder="{self.placeholder}" {value_exist} required>
            """
        elif self.input_type == 'number':
            input_html = f"""
                <input type="number" class="form-control" name="{name}" id="{name}" aria-describedby="{name}_help" placeholder="{self.placeholder}" {value_exist} required>
            """
        elif self.input_type == 'textarea':
            input_html = f"""
                <textarea class="form-control" name="{name}" id="{name}" rows="3" placeholder="{self.placeholder}" >{value_exist}</textarea>
            """

        return f"""
            <div class="form-group col-md-{self.width}">
                <div class="mb-3">
                    <label for="{name}" class="form-label">{self.label}</label>
                    <a tabindex="0" class="fas fa-question-circle fa-xs" role="button" data-bs-trigger="focus" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="right" data-bs-content="{self.pop_text}"></a>
                    {input_html}
                    <small id="{name}_help" class="form-text text-danger"></small>
                </div>
            </div>
        """