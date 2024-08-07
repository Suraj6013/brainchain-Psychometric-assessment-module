# assessment/admin.py

from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.utils.html import format_html
from .models import Assessment, Question, Option
from .forms import CSVImportForm
import pandas as pd

class AssessmentAdmin(admin.ModelAdmin):
    change_list_template = "admin/assessment_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.import_csv),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            df = pd.read_csv(csv_file)
            for _, row in df.iterrows():
                question = Question.objects.create(
                    assessment_id=row['assessment_id'],
                    name=row['name'],
                    description=row['description'],
                    question_type=row['question_type'],
                )
                options = row['options'].split('|')
                for option_text in options:
                    Option.objects.create(question=question, text=option_text)
            self.message_user(request, "CSV file has been imported successfully")
            return redirect("..")
        form = CSVImportForm()
        return render(
            request, "admin/csv_form.html", {"form": form}
        )

    def import_csv_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Import CSV</a>', "import-csv/"
        )

    import_csv_button.short_description = "Import CSV"
    import_csv_button.allow_tags = True

    list_display = ["title", "description", "created_at", "import_csv_button"]

admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Question)
admin.site.register(Option)
