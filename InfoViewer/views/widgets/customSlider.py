import npyscreen


class CustomSlider(npyscreen.TitleSliderPercent):
    def __init__(self, *args, **keywords):
        if "accuracy" not in keywords:
            keywords.update({"accuracy": 0})
        if "max_height" not in keywords:
            keywords.update({"max_height": 1})
        if "begin_entry_at" not in keywords and "name" in keywords:
            # Set the start of the slider dynamic
            # +3 is necessary, else the widget would render in two lines
            keywords.update({"begin_entry_at": len(keywords["name"]) + 3})
        super(CustomSlider, self).__init__(*args, **keywords)

    def update(self, clear=False):
        value = self.value
        if value > 90:
            self.entry_widget.color = 'DANGER'
        elif value > 50:
            self.entry_widget.color = 'WARNING'
        else:
            self.entry_widget.color = 'GOOD'
        super(CustomSlider, self).update(clear)
