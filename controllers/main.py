import time

from odoo import http
from odoo.http import request


class ELearning(http.Controller):
    @http.route(['/elearning/snippet'], type="json", auth="public",
                website=True)
    def elearning_snippet(self, products_per_slide=3):
        course_obj = request.env['slide.channel'].sudo().search(
            [], order='create_date DESC')
        # print(course_obj, "course_obj")
        courses = []
        for course in course_obj:
            # print(courses.read([]))
            items = course.read(
                ['name', 'description_short', 'slide_last_update',
                 'create_date', 'id'])[0]
            items['image'] = request.env['website'].image_url(course,
                                                              'image_1920')

            courses.append(items)
        # print(courses)
        course_group = []
        course_list = []
        for index, record in enumerate(courses, 1):
            course_list.append(record)
            if index % products_per_slide == 0:
                course_group.append(course_list)
                course_list = []
        if any(course_list):
            course_group.append(course_list)

        values = {
            "objects": course_group,
            "products_per_slide": products_per_slide,
            "num_slides": len(course_group),
            "uniqueId": "pc-%d" % int(time.time() * 10000),
        }
        response = http.Response(
            template='elearning_snippet.elearning_snippets', qcontext=values)
        return response.render()

        # last working li = [] for item in course_obj: print(item) # name =
        # item.name course1 = {"course_name": item.name, "course_id":
        # item.id, "promote_strategy": item.promote_strategy, "description":
        # item.description_short } li.append(course1) print(li) response =
        # http.Response(template='elearning_snippet.elearning_snippets',
        # qcontext=vals) return li

    # @http.route(['/course1'], type='http', auth='public',
    #             website=True)
    # def click(self, **post):
    #     # id = post['course1']
    #     return request.redirect(
    #         "slides/"+str(1))
