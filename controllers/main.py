import time

from odoo import http
from odoo.http import request


class ELearning(http.Controller):
    @http.route(['/elearning/snippet'], type="json", auth="public",
                website=True)
    def elearning_snippet(self, products_per_slide=3):
        course_obj = request.env['slide.channel'].sudo().search(
            [], order='create_date DESC')
        print(course_obj, "course_obj")
        courses = []
        for course in course_obj:
            # print(courses.read([]))
            items = course.read(
                ['name', 'description_short', 'slide_last_update',
                               'id'])[0]
            items['image'] = request.env['website'].image_url(course,
                                                              'image_512')

            courses.append(items)
        # print(courses)
        # grouping the sold products
        sold_group = []
        sold_list = []
        for index, record in enumerate(courses, 1):
            sold_list.append(record)
            if index % products_per_slide == 0:
                sold_group.append(sold_list)
                sold_list = []
        if any(sold_list):
            sold_group.append(sold_list)

        values = {
            "objects": sold_group,
            "products_per_slide": products_per_slide,
            "num_slides": len(sold_group),
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
