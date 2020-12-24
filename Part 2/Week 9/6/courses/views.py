from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
import requests
import json
import re

from courses.models import Courses


def make_update():
    url = 'https://openedu.ru/course/'
    html = requests.get(url).text

    pattern_course = r"(COURSES = )(.*)(;\n)"
    courses = re.findall(pattern_course, html)[0][1]
    courses_json = json.loads(courses)
    for course in courses_json:
        course_db = courses_json[course]["title"]
        Courses.objects.create(title=course_db)


class MainPage(View):
    def get(self, request):
        make_update()
        context = Courses.objects.values()
        return render(request, "index.html", {"courses": context})