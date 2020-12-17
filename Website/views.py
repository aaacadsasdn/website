from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "a"
        return ctxt


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_travel"] = 15555
        ctxt["skills"] = [
            "tinko",
            "desuwa"
        ]
        return ctxt
