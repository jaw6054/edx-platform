"""
Portfolio views.
"""

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import ensure_csrf_cookie

from lms.djangoapps.courseware.courses import get_course_with_access
from lms.djangoapps.courseware.views.views import CourseTabView

from openedx.core.djangoapps.plugin_api.views import EdxFragmentView
from opaque_keys.edx.keys import CourseKey
from util.views import ensure_valid_course_key

from web_fragments.fragment import Fragment


class GenericTabView(CourseTabView):
    """
    Provides a blank page that acts as its own tab in courseware for displaying content.
    """
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(cache_control(no_cache=True, no_store=True, must_revalidate=True))
    @method_decorator(ensure_valid_course_key)
    def get(self, request, course_id, **kwargs):
        """
        Displays a generic tab for the specified course.
        """
        return super(GenericTabView, self).get(request, course_id, 'courseware', **kwargs)

    def render_to_fragment(self, request, course=None, tab=None, **kwargs):
        """
        Render out the bootstrap page.
        """
        context = {
            'course': course,
            'user': request.user,
            'uses_bootstrap': True,
            'tab_name': 'portfolio_project',
        }
        html = render_to_string('portfolio_project/generic_tab.html', context)
        return Fragment(html)
